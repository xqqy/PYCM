# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName(u"MainForm")
        MainForm.resize(397, 65)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainForm.setWindowIcon(icon)
        self.action_send_file = QAction(MainForm)
        self.action_send_file.setObjectName(u"action_send_file")
        self.action_file_client = QAction(MainForm)
        self.action_file_client.setObjectName(u"action_file_client")
        self.main_layout = QVBoxLayout(MainForm)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(MainForm)
        self.main_container.setObjectName(u"main_container")
        self.main_container_layout = QVBoxLayout(self.main_container)
        self.main_container_layout.setSpacing(0)
        self.main_container_layout.setObjectName(u"main_container_layout")
        self.main_container_layout.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.main_container)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 229, 231, 255), stop:1 rgba(19, 12, 183, 255));\n"
"color: rgb(255, 255, 255);")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.main_container_layout.addWidget(self.title_label)

        self.tool_buttons_layout = QHBoxLayout()
        self.tool_buttons_layout.setSpacing(3)
        self.tool_buttons_layout.setObjectName(u"tool_buttons_layout")
        self.tool_buttons_layout.setContentsMargins(5, 3, 5, 5)
        self.notify_button = QPushButton(self.main_container)
        self.notify_button.setObjectName(u"notify_button")
        self.notify_button.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notify_button.sizePolicy().hasHeightForWidth())
        self.notify_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        self.notify_button.setFont(font1)

        self.tool_buttons_layout.addWidget(self.notify_button)

        self.file_button = QPushButton(self.main_container)
        self.file_button.setObjectName(u"file_button")
        self.file_button.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.file_button.sizePolicy().hasHeightForWidth())
        self.file_button.setSizePolicy(sizePolicy1)
        self.file_button.setFont(font1)

        self.tool_buttons_layout.addWidget(self.file_button)

        self.private_message_button = QPushButton(self.main_container)
        self.private_message_button.setObjectName(u"private_message_button")
        self.private_message_button.setEnabled(False)
        sizePolicy.setHeightForWidth(self.private_message_button.sizePolicy().hasHeightForWidth())
        self.private_message_button.setSizePolicy(sizePolicy)
        self.private_message_button.setFont(font1)

        self.tool_buttons_layout.addWidget(self.private_message_button)

        self.hide_button = QPushButton(self.main_container)
        self.hide_button.setObjectName(u"hide_button")
        sizePolicy1.setHeightForWidth(self.hide_button.sizePolicy().hasHeightForWidth())
        self.hide_button.setSizePolicy(sizePolicy1)
        self.hide_button.setFont(font1)

        self.tool_buttons_layout.addWidget(self.hide_button)

        self.tool_buttons_layout.setStretch(0, 1)
        self.tool_buttons_layout.setStretch(1, 1)
        self.tool_buttons_layout.setStretch(2, 1)
        self.tool_buttons_layout.setStretch(3, 1)

        self.main_container_layout.addLayout(self.tool_buttons_layout)


        self.main_layout.addWidget(self.main_container)


        self.retranslateUi(MainForm)
        self.notify_button.clicked.connect(MainForm.notify_console)
        self.hide_button.clicked.connect(MainForm.hide)
        self.private_message_button.clicked.connect(MainForm.show_messaging_window)

        QMetaObject.connectSlotsByName(MainForm)
    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(QCoreApplication.translate("MainForm", u"Client", None))
        self.action_send_file.setText(QCoreApplication.translate("MainForm", u"Send File", None))
        self.action_file_client.setText(QCoreApplication.translate("MainForm", u"File Client", None))
        self.title_label.setText(QCoreApplication.translate("MainForm", u"PYCM Client - Offline", None))
        self.notify_button.setText(QCoreApplication.translate("MainForm", u"Hands Up", None))
        self.file_button.setText(QCoreApplication.translate("MainForm", u"File", None))
        self.private_message_button.setText(QCoreApplication.translate("MainForm", u"Messaging", None))
        self.hide_button.setText(QCoreApplication.translate("MainForm", u"Hide", None))
    # retranslateUi

