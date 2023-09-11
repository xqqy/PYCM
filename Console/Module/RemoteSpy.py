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

from PySide6.QtGui import QImage, QPixmap
import socket
import struct
from queue import Queue
from threading import Thread
import zlib
import logging
from Module.Packages import RemoteSpyFlag


class RemoteSpy(object):
    socket_port = None
    socket_obj = None
    socket_conn = None

    def __init__(self, parent, socket_port):
        self.parent = parent
        self.socket_port = socket_port
        self.command_queue = Queue()
        self.working = False
        self.__init_socket_obj()

    def __init_socket_obj(self):
        self.socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_obj.bind(('', self.socket_port))
        self.socket_obj.listen(1)

    def stop(self):
        if not self.socket_conn:
            return
        try:
            socket_data = struct.pack('!i', RemoteSpyFlag.RemoteSpyStop)
            self.socket_conn.send(socket_data)
        except ConnectionResetError:
            return
        except Exception as e:
            logging.warning(f'Failed to tell client to stop screen spy: f{e}')

    def start(self):
        recv_header_size = struct.calcsize('!2i')
        while self.working:
            try:
                self.socket_conn, socket_addr = self.socket_obj.accept()
                while self.working:
                    socket_data = self.socket_conn.recv(recv_header_size)
                    if not socket_data:
                        break
                    unpacked_flag, unpacked_data = struct.unpack('!2i', socket_data)
                    if unpacked_flag == RemoteSpyFlag.RemoteSpyStop:
                        break
                    elif unpacked_flag == RemoteSpyFlag.PackInfo:
                        payload_size = unpacked_data
                        frame = b''
                        while len(frame) < payload_size:
                            payload_part = self.socket_conn.recv(payload_size)
                            frame += payload_part
                        frame = zlib.decompress(frame)
                        frame = QImage.fromData(frame)
                        self.parent.frame_received.emit(QPixmap.fromImage(frame))
                self.socket_conn.close()
                self.socket_conn = None
            except ConnectionResetError:
                continue
            except Exception as e:
                logging.warning(f'Failed to decode socket data: {e}')
