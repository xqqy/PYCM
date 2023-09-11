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

from PySide6.QtCore import QObject, QBuffer, QIODevice
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QImage, QPainter, QCursor
##from PySide6.sip import voidptr
from Module.Packages import ScreenBroadcastFlag
import socket
import struct
import zlib
import logging


class ScreenBroadcast(QObject):
    def __init__(self, parent, current_ip, socket_ip, socket_port, socket_buffer, quality=60):
        super(ScreenBroadcast, self).__init__()
        self.parent = parent
        self.current_ip = current_ip
        self.socket_ip = socket_ip
        self.socket_port = socket_port
        self.socket_buffer = socket_buffer
        self.quality = quality
        self.socket_obj = None
        self.working = False
        self.init_socket_obj()

    def init_socket_obj(self):
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket_obj.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.socket_buffer)
        self.socket_obj.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(self.socket_ip) + socket.inet_aton(self.current_ip)
        )

    def start(self):
        pack_index = 0
        payload_size = self.socket_buffer - struct.calcsize('!2i')
        target = (self.socket_ip, self.socket_port)
        cursor = QCursor()
        cursor_icon = QImage(':/Core/Core/Pointer.png')
        painter = QPainter()
        screen = QApplication.primaryScreen()
        while self.working:
            try:
                cursor_pos = cursor.pos()
                # noinspection PyTypeChecker
                img = screen.grabWindow(0)
                painter.begin(img)
                painter.drawImage(cursor_pos, cursor_icon)
                painter.end()
                buffer = QBuffer()
                buffer.open(QIODevice.ReadWrite)
                img.save(buffer, 'JPEG', quality=self.quality)
                img_encoded = zlib.compress(bytes(buffer.data()))
                buffer.close()
                rounds = len(img_encoded) // payload_size
                looped_size = rounds * payload_size
                header = struct.pack('!4i', ScreenBroadcastFlag.PackInfo, pack_index, len(img_encoded), rounds)
                self.socket_obj.sendto(header, target)
                for i in range(rounds):
                    pack = img_encoded[i * payload_size: (i + 1) * payload_size]
                    data = struct.pack(f'!2i{payload_size}s', ScreenBroadcastFlag.PackData, len(pack), pack)
                    self.socket_obj.sendto(data, target)
                if looped_size < len(img_encoded):
                    pack = img_encoded[looped_size:]
                    data = struct.pack(f'!2i{payload_size}s', ScreenBroadcastFlag.PackData, len(pack), pack)
                    self.socket_obj.sendto(data, target)
                pack_index = (pack_index + 1) % 1000
            except Exception as e:
                logging.warning(f'Screen send thread unexpected error: {e}')
