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

from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, \
    QFileIconProvider, QApplication, QFileDialog, QMessageBox
from PySide6.QtCore import Qt, QFileInfo, QThread, Signal, QCoreApplication
from PySide6.QtGui import QIcon, QDragEnterEvent, QDragMoveEvent, QDropEvent, QCloseEvent
import os
import zipfile
from io import BytesIO
from functools import partial
from .FileSendUI import Ui_FileSendForm


class FileCompressThread(QThread):
    file_buffer = Signal(bytes)
    file_finished = Signal(int)
    file_list = None

    def __init__(self, file_list):
        super(FileCompressThread, self).__init__()
        self.file_list = file_list

    def run(self):
        buffer = BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zfile:
            for index, file_path in enumerate(self.file_list):
                file_name = os.path.basename(file_path)
                zfile.write(file_path, file_name)
                self.file_finished.emit(index)
        self.file_buffer.emit(buffer.getvalue())


class FileSendThread(QThread):
    private_message_object = None
    buffer = None
    file_send_progress = Signal(float)

    def __init__(self, private_message_object, buffer):
        super(FileSendThread, self).__init__()
        self.private_message_object = private_message_object
        self.private_message_object.file_send_progress.connect(self.update_progress)
        self.buffer = buffer

    def update_progress(self, progress):
        self.file_send_progress.emit(progress)

    def run(self):
        self.private_message_object.send_file(self.buffer)


class DraggableQListWidget(QTableWidget):
    _translate = QCoreApplication.translate

    def __init__(self):
        super(DraggableQListWidget, self).__init__()
        self.setAcceptDrops(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels([self._translate('FileSendForm', 'File Name'),
                                        self._translate('FileSendForm', 'File Size'),
                                        self._translate('FileSendForm', 'Status')])
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.setColumnWidth(1, 120)
        self.setColumnWidth(2, 120)

    @staticmethod
    def parse_file_size(file_size):
        def str_of_size(integer, remainder, level):
            if integer >= 1024:
                remainder = integer % 1024
                integer //= 1024
                level += 1
                return str_of_size(integer, remainder, level)
            return integer, remainder, level

        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        integer, remainder, level = str_of_size(file_size, 0, 0)
        if level + 1 > len(units):
            level = -1
        return '{}.{:>03d} {}'.format(integer, remainder, units[level])

    def batch_add_files(self, files):
        for file_info in files:
            if not file_info.isFile():
                continue
            current_row = self.rowCount()
            icon = QIcon(QFileIconProvider().icon(file_info))
            file_name_and_icon = QTableWidgetItem(file_info.absoluteFilePath())
            file_name_and_icon.setIcon(icon)
            self.setRowCount(current_row + 1)
            self.setItem(current_row, 0, file_name_and_icon)
            self.setItem(current_row, 1, QTableWidgetItem(self.parse_file_size(file_info.size())))
            self.setItem(current_row, 2, QTableWidgetItem(self._translate('FileSendForm', 'Ready')))

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls:
            event.accept()
            files = [QFileInfo(url.toLocalFile()) for url in event.mimeData().urls()]
            self.batch_add_files(files)
        else:
            event.ignore()


class FileSendForm(QWidget):
    _translate = QCoreApplication.translate
    is_sending = False
    is_sent = False
    __compress_thread = None
    __file_send_thread = None
    parent = None

    def __init__(self, parent=None):
        super(FileSendForm, self).__init__()
        self.parent = parent
        self.ui = Ui_FileSendForm()
        self.ui.setupUi(self)
        self.__repaint_ui()

    def __repaint_ui(self):
        self.ui.file_list = DraggableQListWidget()
        self.ui.file_list_container.addWidget(self.ui.file_list)

    def show_add_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(self, self._translate('FileSendForm', 'Select Files'),
                                                os.path.expanduser('~'),
                                                self._translate('FileSendForm', 'All Files (*)'))
        if files:
            self.ui.file_list.batch_add_files(list(map(QFileInfo, files)))

    def delete_selected_files(self):
        selected_rows = list({item.row() for item in self.ui.file_list.selectedItems()})
        selected_rows.sort(reverse=True)
        for row in selected_rows:
            self.ui.file_list.removeRow(row)

    def send_all(self):
        file_list = [self.ui.file_list.item(row, 0).text() for row in range(self.ui.file_list.rowCount())]
        self.__compress_thread = FileCompressThread(file_list)
        self.__compress_thread.file_finished.connect(partial(self.update_status,
                                                             self._translate('FileSendForm', 'Compressed')))
        self.__compress_thread.file_buffer.connect(self.submit_compressed_file)
        self.is_sending = True
        self.ui.file_send_progress_label.setText(self._translate('FileSendForm', 'Compressing'))
        self.__compress_thread.start()

    def submit_compressed_file(self, file_buffer):
        self.is_sending = False
        self.__file_send_thread = FileSendThread(self.parent.private_message_object, file_buffer)
        self.__file_send_thread.file_send_progress.connect(self.update_send_status)
        self.__file_send_thread.start()

    def update_status(self, label, index):
        self.ui.file_list.item(index, 2).setText(label)
        current_row_count = self.ui.file_list.rowCount()
        if index + 1 < current_row_count:
            self.update_send_status((index + 1) / current_row_count)
        else:
            self.ui.file_send_progress_label.setText(self._translate('FileSendForm', 'Submitting'))
            self.update_send_status(0)

    def update_send_status(self, progress):
        progress = int(progress * 100)
        self.ui.file_send_progress_bar.setValue(progress)
        if progress >= 100 and not self.is_sent:
            self.is_sent = True
            self.ui.file_send_progress_bar.setMaximum(0)
            self.ui.file_send_progress_label.setText(self._translate('FileSendForm', 'Processing'))

    def file_received(self):
        self.ui.file_send_progress_bar.setMaximum(100)
        self.ui.file_send_progress_bar.setValue(100)
        self.ui.file_send_progress_label.setText(self._translate('FileSendForm', 'Finished'))
        QMessageBox.information(self, self._translate('FileSendForm', 'Info'),
                                self._translate('FileSendForm', 'Submit Success!'))
        self.is_sent = False
        self.close()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def closeEvent(self, event: QCloseEvent):
        if self.is_sending:
            event.ignore()
        else:
            self.ui.file_list.clearContents()
            self.ui.file_list.setRowCount(0)
            self.ui.file_send_progress_bar.setValue(0)
            self.hide()
            event.ignore()
