# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SendMessageUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_SendMessageForm(object):
    def setupUi(self, SendMessageForm):
        if not SendMessageForm.objectName():
            SendMessageForm.setObjectName(u"SendMessageForm")
        SendMessageForm.resize(416, 420)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SendMessageForm.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(SendMessageForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.message_area = QTextBrowser(SendMessageForm)
        self.message_area.setObjectName(u"message_area")
        font = QFont()
        font.setPointSize(10)
        self.message_area.setFont(font)
        self.message_area.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.message_area)

        self.send_message_layout = QHBoxLayout()
        self.send_message_layout.setObjectName(u"send_message_layout")
        self.message_input = QLineEdit(SendMessageForm)
        self.message_input.setObjectName(u"message_input")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_input.sizePolicy().hasHeightForWidth())
        self.message_input.setSizePolicy(sizePolicy)

        self.send_message_layout.addWidget(self.message_input)

        self.send = QPushButton(SendMessageForm)
        self.send.setObjectName(u"send")
        self.send.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.send.sizePolicy().hasHeightForWidth())
        self.send.setSizePolicy(sizePolicy1)
        self.send.setMaximumSize(QSize(80, 16777215))
        self.send.setFont(font)

        self.send_message_layout.addWidget(self.send)


        self.verticalLayout.addLayout(self.send_message_layout)


        self.retranslateUi(SendMessageForm)
        self.send.clicked.connect(SendMessageForm.send_message)
        self.message_input.textChanged.connect(SendMessageForm.update_input_text)
        self.message_input.returnPressed.connect(self.send.click)

        QMetaObject.connectSlotsByName(SendMessageForm)
    # setupUi

    def retranslateUi(self, SendMessageForm):
        SendMessageForm.setWindowTitle(QCoreApplication.translate("SendMessageForm", u"Messaging", None))
        self.send.setText(QCoreApplication.translate("SendMessageForm", u"Send", None))
    # retranslateUi

