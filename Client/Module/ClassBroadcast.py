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

from PySide6.QtCore import QObject
import socket
import time
import struct
import base64
import pickle
import zlib
import subprocess
import logging
from Module.Packages import ClassBroadcastFlag


class ClassBroadcast(QObject):
    parent = None
    current_ip = None
    socket_ip = None
    socket_port = None
    socket_buffer_size = None
    socket_obj = None

    def __init__(self, parent, current_ip, socket_ip, socket_port, socket_buffer_size):
        super(ClassBroadcast, self).__init__(parent)
        self.parent = parent
        self.current_ip = current_ip
        self.socket_ip = socket_ip
        self.socket_port = socket_port
        self.socket_buffer_size = socket_buffer_size
        self.__init_socket_obj()

    def __init_socket_obj(self):
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket_obj.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.socket_buffer_size)
        self.socket_obj.bind(('', self.socket_port))
        self.socket_obj.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(self.socket_ip) + socket.inet_aton(self.current_ip)
        )

    @staticmethod
    def execute_remote_command(command):
        subprocess.call(command, shell=False)

    def batch_send_decode(self, unpacked_data):
        header_length = struct.calcsize('!iL')
        targets_length, chsum = struct.unpack('!iL', unpacked_data[:header_length])
        raw_data = unpacked_data[header_length:header_length + targets_length]
        if zlib.crc32(raw_data) != chsum:
            return None
        targets = pickle.loads(raw_data)
        if self.current_ip in targets:
            data = unpacked_data[header_length + targets_length:]
            return data
        return None

    def batch_data_handler(self, unpacked_flag, data):
        if unpacked_flag == ClassBroadcastFlag.Message:
            message = base64.b64decode(data).decode('utf-8')
            self.parent.message_received.emit(str(message))
        elif unpacked_flag == ClassBroadcastFlag.Command:
            message = base64.b64decode(data).decode('utf-8')
            self.execute_remote_command(str(message))
        elif unpacked_flag == ClassBroadcastFlag.RemoteSpyStart:
            self.parent.start_remote_spy.emit()
        elif unpacked_flag == ClassBroadcastFlag.RemoteQuit:
            self.parent.quit_self.emit()
            return
        elif unpacked_flag == ClassBroadcastFlag.ClientFileReceived:
            self.parent.client_file_received.emit()

    def start(self):
        payload_size = self.socket_buffer_size - struct.calcsize('!2i')
        while True:
            try:
                socket_data, socket_addr = self.socket_obj.recvfrom(self.socket_buffer_size)
                unpacked_flag, unpacked_length, unpacked_data = struct.unpack(f'!2i{payload_size}s', socket_data)
                unpacked_data = unpacked_data[:unpacked_length]
                if unpacked_flag in (
                        ClassBroadcastFlag.Message,
                        ClassBroadcastFlag.Command,
                        ClassBroadcastFlag.RemoteSpyStart,
                        ClassBroadcastFlag.RemoteQuit,
                        ClassBroadcastFlag.ClientFileReceived
                ):
                    data = self.batch_send_decode(unpacked_data)
                    if data is not None:
                        self.batch_data_handler(unpacked_flag, data)
                elif unpacked_flag == ClassBroadcastFlag.ToggleScreenBroadcast:
                    if unpacked_data[0] == ord('1'):
                        self.parent.toggle_screen_broadcats.emit(True)
                    elif unpacked_data[0] == ord('0'):
                        self.parent.toggle_screen_broadcats.emit(False)
                elif unpacked_flag == ClassBroadcastFlag.ConsoleQuit:
                    self.parent.reset_all.emit()
                    return
                elif unpacked_flag == ClassBroadcastFlag.ToggleFileServer:
                    if unpacked_data[0] == ord('1'):
                        self.parent.toggle_file_server.emit(True, unpacked_data[1:].decode())
                    elif unpacked_data[0] == ord('0'):
                        self.parent.toggle_file_server.emit(False, None)
            except Exception as e:
                logging.warning(f'Failed to decode socket data: {e}')
