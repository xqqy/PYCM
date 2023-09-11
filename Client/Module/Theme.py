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

from PySide6.QtCore import QCoreApplication, QFile, QTextStream, QDataStream, QStringConverter
from PySide6.QtGui import QColor, QPalette, QFontDatabase, QFont
import platform
import os


def _apply_os_patches():
    os_fix = ''
    if platform.system().lower() == 'darwin':
        os_fix = '''
        QDockWidget::title
        {{
            background-color: #455364;
            text-align: center;
            height: 12px;
        }}
        QTabBar::close-button {{
            padding: 2px;
        }}
        '''
    return os_fix


def _apply_version_patches():
    version_fix = ''
    major, minor, patch = int(major), int(minor), int(patch)
    if major == 5 and minor >= 14:
        version_fix = '''
        QMenu::item {
            padding: 4px 24px 4px 6px;
        }
        '''
    return version_fix


def _apply_application_patches():
    app = QCoreApplication.instance()
    app_palette = app.palette()
    app_palette.setColor(QPalette.Normal, QPalette.Link, QColor('#1A72BB'))
    app.setPalette(app_palette)


def _apply_application_font():
    QFontDatabase.addApplicationFont(':/Core/Fonts/Alibaba-PuHuiTi-Bold.ttf')
    QFontDatabase.addApplicationFont(':/Core/Fonts/Alibaba-PuHuiTi-Regular.ttf')
    app = QCoreApplication.instance()
    font = QFont('Alibaba PuHuiTi')
    font.setPointSize(9)
    app.setFont(font)


def load_stylesheet():
    qss_file = QFile(':/Core/Style.qss')
    qss_file.open(QFile.ReadOnly | QFile.Text)
    text_stream = QTextStream(qss_file)
    text_stream.setEncoding(QStringConverter.Utf8)
    stylesheet = text_stream.readAll()

    stylesheet += _apply_os_patches()
    #stylesheet += _apply_version_patches()
    _apply_application_patches()
    _apply_application_font()

    return stylesheet
