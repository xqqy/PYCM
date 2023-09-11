# -*- coding: utf-8 -*-
"""
    This file is part of PYCM project
    Copyright (C) 2021 Richard Yang  <zhongtian.yang@qq.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide6.QtWidgets import QWidget, QSystemTrayIcon, QMenu, QMessageBox, QApplication
from PySide6.QtCore import Qt, QPoint, QTimer, Signal, QCoreApplication
from PySide6.QtGui import QMouseEvent, QIcon, QCloseEvent,QAction, QGuiApplication
import socket
import platform
import subprocess

from .MainUI import Ui_MainForm
from .FileSend import FileSendForm
from .ScreenBroadcast import ScreenBroadcastForm
from .SendMessage import SendMessageForm
from .NetworkDeviceSelect import NetworkDeviceSelectForm
from .About import AboutDialog

from Module.Threadings import NetworkDiscoverThread, ClassBroadcastThread, ScreenBroadcastThread, RemoteSpyThread
from Module.PrivateMessage import PrivateMessage


# noinspection PyAttributeOutsideInit
class MainForm(QWidget):
    config = None
    net_discover_thread = None
    class_broadcast_thread = None
    screen_broadcast_thread = None
    remote_spy_thread = None
    private_message_object = None
    server_ip = None
    screen_spy_timer = QTimer()
    file_client_password = ''
    _start_pos = None
    _end_pos = None
    _is_tracking = False
    _force_quit = False
    _translate = QCoreApplication.translate

    def __init__(self, parent=None):
        super(MainForm, self).__init__()
        self.ui = Ui_MainForm()
        self.parent = parent
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(int(QGuiApplication.primaryScreen().availableGeometry().width() - 450), 65)
        self.screen_broadcast_window = ScreenBroadcastForm(parent)
        self.file_send_window = FileSendForm(self.parent)
        self.messaging_window = SendMessageForm(self.parent)
        self.init_tray()
        self.init_file_button()

    def load_network_device(self):
        devices = NetworkDeviceSelectForm.get_devices()
        default_device = self.parent.config.get_item('Network/Local/Device')
        for device in devices:
            if device[1]['NAME'] == default_device:
                return device[1]

    def init_threadings(self):
        self.net_discover_thread = NetworkDiscoverThread(self.config)
        self.class_broadcast_thread = ClassBroadcastThread(self.config)
        self.screen_broadcast_thread = ScreenBroadcastThread(self.config)
        self.remote_spy_thread = RemoteSpyThread(self.config)
        self.private_message_object = PrivateMessage(self.config)
        self.init_connections()
        self.net_discover_thread.start()

    def init_connections(self):
        self.net_discover_thread.server_info.connect(self.server_found)
        self.class_broadcast_thread.message_received.connect(self.message_received)
        self.class_broadcast_thread.reset_all.connect(self.reset_all_threadings)
        self.class_broadcast_thread.toggle_screen_broadcats.connect(self.__toggle_screen_broadcast)
        self.class_broadcast_thread.quit_self.connect(self.quit_self)
        self.class_broadcast_thread.start_remote_spy.connect(self.start_remote_spy)
        self.class_broadcast_thread.toggle_file_server.connect(self.toggle_file_client)
        self.screen_broadcast_thread.frame_received.connect(self.screen_broadcast_window.update_frame)
        self.screen_spy_timer.timeout.connect(self.private_message_object.screen_spy_send)

    def reset_all_threadings(self):
        self.screen_spy_timer.stop()
        self.class_broadcast_thread.quit()
        self.remote_spy_thread.safe_stop()
        self.class_broadcast_thread.wait()
        self.remote_spy_thread.wait()
        self.net_discover_thread = NetworkDiscoverThread(self.config)
        self.class_broadcast_thread = ClassBroadcastThread(self.config)
        self.remote_spy_thread = RemoteSpyThread(self.config)
        self.private_message_object = PrivateMessage(self.config)
        self.init_connections()
        self.ui.title_label.setText(self._translate('MainForm', 'PYCM Client - Offline'))
        self.update_tray_tooltip()
        self.ui.notify_button.setEnabled(False)
        self.ui.file_button.setEnabled(False)
        self.ui.private_message_button.setEnabled(False)
        self.server_ip = None
        self.net_discover_thread.start()

    # noinspection PyArgumentList
    def init_tray(self):
        self.tray_icon_menu = QMenu(self)
        self.tray_icon_menu.addAction(QAction(self._translate('MainForm', 'Show Tool Bar'), self, triggered=self.show))
        self.tray_icon_menu.addAction(QAction(self._translate('MainForm', 'Configure Network'),
                                              self, triggered=self.show_network_config_window))
        self.tray_icon_menu.addAction(QAction(self._translate('MainForm', 'About'),
                                              self, triggered=self.show_about))
        self.tray_icon_menu.addAction(QAction(self._translate('MainForm', 'Exit'), self, triggered=self.close))
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(':/Core/Core/Logo.png'))
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.activated.connect(self.iconActivated)
        self.update_tray_tooltip()
        self.tray_icon.show()

    # noinspection PyArgumentList
    def init_file_button(self):
        self.file_button_menu = QMenu()
        self.file_client_action = QAction(self._translate('MainForm', 'File Client'), self,
                                          triggered=self.show_file_client_window)
        self.file_client_action.setEnabled(False)
        file_send_action = QAction(self._translate('MainForm', 'Send File'), self,
                                   triggered=self.show_file_send_window)
        self.file_button_menu.addActions([self.file_client_action, file_send_action])
        self.ui.file_button.setMenu(self.file_button_menu)

    def show_network_config_window(self):
        reply = QMessageBox.question(self, self._translate('MainForm', 'Warning'),
                                     self._translate('MainForm',
                                                     'Are you sure to modify the network configuration? ' +
                                                     'This operation may cause the client to fail to start normally!'),
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            result = self.config.modify_network_device()
            if result:
                QMessageBox.information(self, self._translate('MainForm', 'Info'),
                                        self._translate('MainForm', 'Configuration success! ' +
                                                        'Please restart the client to take effect'),
                                        QMessageBox.Ok)

    def show_file_send_window(self):
        self.file_send_window = FileSendForm(self.parent)
        self.class_broadcast_thread.client_file_received.connect(self.file_send_window.file_received)
        self.file_send_window.show()

    def show_file_client_window(self):
        file_client_port = self.parent.config.get_item('Network/FileServer/Port')
        ftp_url = f'ftp://pycm:{self.file_client_password}@{self.server_ip}:{file_client_port}'
        system = platform.system().lower()
        if system == 'windows':
            subprocess.call(['explorer.exe', ftp_url], shell=False)
        elif system == 'darwin':
            subprocess.call(['open', ftp_url], shell=False)
        elif system == 'linux':
            subprocess.call(['xdg-open', ftp_url], shell=False)

    def show_messaging_window(self):
        self.messaging_window.show()

    def show_about(self):
        AboutDialog(self).exec()

    def start_remote_spy(self):
        self.remote_spy_thread.start()

    def message_received(self, message):
        icon = QSystemTrayIcon.MessageIcon()
        self.tray_icon.showMessage(self._translate('MainForm', 'Message'), message, icon, 1000)
        self.messaging_window.add_message(True, message)

    def notify_console(self):
        self.private_message_object.notify_console()

    def server_found(self, server_ip, screen_broadcast_status, file_server_status, file_server_password):
        self.server_ip = server_ip
        self.private_message_object.set_socket_ip(self.server_ip)
        self.remote_spy_thread.set_socket_ip(self.server_ip)
        self.private_message_object.online_notify()
        self.class_broadcast_thread.start()
        self.ui.title_label.setText(self._translate('MainForm', 'PYCM Client - Online'))
        self.update_tray_tooltip()
        self.ui.notify_button.setEnabled(True)
        self.ui.file_button.setEnabled(True)
        self.ui.private_message_button.setEnabled(True)
        self.screen_spy_timer.start(3000)
        if screen_broadcast_status:
            self.__toggle_screen_broadcast(True)
        if file_server_status:
            self.toggle_file_client(True, file_server_password)

    def init_network_device(self, device):
        self.config.save('Network/Local/IP', device['IP'])
        self.config.save('Network/Local/MAC', device['MAC'])

    def __toggle_screen_broadcast(self, work):
        self.screen_broadcast_thread.socket.working = work
        if work:
            self.screen_broadcast_thread.start()
            self.screen_broadcast_window.show()
        else:
            self.screen_broadcast_thread.safe_stop()
            self.screen_broadcast_window.hide()

    def update_tray_tooltip(self):
        local_ip = self.config.get_item('Network/Local/IP')
        if self.server_ip:
            online_status = self._translate('MainForm', 'Online')
        else:
            online_status = self._translate('MainForm', 'Offline')
        self.tray_icon.setToolTip(self._translate('MainForm', 'PYCM Client\n') +
                                  self._translate('MainForm', 'Local IP: %s\n') % local_ip +
                                  self._translate('MainForm', 'Status: %s') % online_status)

    def quit_self(self):
        self._force_quit = True
        self.close()

    def toggle_file_client(self, working, password):
        if working:
            self.file_client_password = password
            self.file_client_action.setEnabled(True)
        else:
            self.file_client_action.setEnabled(False)

    def mouseMoveEvent(self, e: QMouseEvent):
        if self._start_pos and self._is_tracking:
            self._end_pos = e.pos() - self._start_pos
            self.move(self.pos() + self._end_pos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._is_tracking = True
            self._start_pos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._is_tracking = False
            self._start_pos = None
            self._end_pos = None

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show()

    def closeEvent(self, event: QCloseEvent):
        if not self._force_quit:
            reply = QMessageBox.question(self, self._translate('MainForm', 'Warning'),
                                         self._translate('MainForm', 'Are you sure to exit?'),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply != QMessageBox.Yes:
                event.ignore()
                return
        if self.server_ip is not None:
            self.private_message_object.offline_notify()
        if self.tray_icon.isVisible():
            self.tray_icon.hide()
        self.tray_icon = None
        QApplication.instance().quit()
