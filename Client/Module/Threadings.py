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

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from Module.ClassBroadcast import ClassBroadcast
from Module.NetworkDiscover import NetworkDiscover
from Module.ScreenBroadcast import ScreenBroadcast
from Module.RemoteSpy import RemoteSpy


class ClassBroadcastThread(QThread):
    message_received = Signal(str)
    reset_all = Signal()
    toggle_screen_broadcats = Signal(bool)
    start_remote_spy = Signal()
    quit_self = Signal()
    client_file_received = Signal()
    toggle_file_server = Signal(bool, str)

    def __init__(self, config):
        super(ClassBroadcastThread, self).__init__()
        self.current_ip = config.get_item('Network/Local/IP')
        self.socket_ip = config.get_item('Network/ClassBroadcast/IP')
        self.socket_port = config.get_item('Network/ClassBroadcast/Port')
        self.socket_buffer = config.get_item('Network/ClassBroadcast/Buffer')
        self.socket = ClassBroadcast(self, self.current_ip, self.socket_ip, self.socket_port, self.socket_buffer)

    def run(self):
        self.socket.start()


class NetworkDiscoverThread(QThread):
    server_info = Signal(str, bool, bool, str)

    def __init__(self, config):
        super(NetworkDiscoverThread, self).__init__()
        self.current_ip = config.get_item('Network/Local/IP')
        self.socket_ip = config.get_item('Network/NetworkDiscover/IP')
        self.socket_port = config.get_item('Network/NetworkDiscover/Port')
        self.socket = NetworkDiscover(self.current_ip, self.socket_ip, self.socket_port)

    def run(self):
        server_ip, screen_broadcast, file_server, file_server_password = self.socket.wait_for_console()
        self.server_info.emit(server_ip, screen_broadcast, file_server, file_server_password)


class ScreenBroadcastThread(QThread):
    frame_received = Signal(QPixmap)

    def __init__(self, config):
        super(ScreenBroadcastThread, self).__init__()
        self.current_ip = config.get_item('Network/Local/IP')
        self.socket_ip = config.get_item('Network/ScreenBroadcast/IP')
        self.socket_port = config.get_item('Network/ScreenBroadcast/Port')
        self.socket_buffer = config.get_item('Network/ScreenBroadcast/Buffer')
        self.socket = ScreenBroadcast(self, self.current_ip, self.socket_ip, self.socket_port, self.socket_buffer)

    def run(self):
        self.socket.working = True
        self.socket.start()

    def safe_stop(self):
        self.socket.working = False
        self.terminate()


class RemoteSpyThread(QThread):
    def __init__(self, config):
        super(RemoteSpyThread, self).__init__()
        self.socket_ip = None
        self.socket_port = config.get_item('Network/RemoteSpy/Port')
        self.socket = RemoteSpy(self.socket_port)

    def set_socket_ip(self, socket_ip):
        self.socket_ip = socket_ip
        self.socket.set_socket_ip(self.socket_ip)

    def safe_stop(self):
        self.socket.stop()
        self.wait()

    def run(self):
        if self.socket_ip is not None:
            self.socket.init_socket_obj()
            self.socket.set_socket_ip(self.socket_ip)
        self.socket.working = True
        self.socket.start()
