# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SendMessageGroupUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QPlainTextEdit, QSizePolicy,
    QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_SendMessageGroupDialog(object):
    def setupUi(self, SendMessageGroupDialog):
        if not SendMessageGroupDialog.objectName():
            SendMessageGroupDialog.setObjectName(u"SendMessageGroupDialog")
        SendMessageGroupDialog.resize(349, 282)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SendMessageGroupDialog.sizePolicy().hasHeightForWidth())
        SendMessageGroupDialog.setSizePolicy(sizePolicy)
        SendMessageGroupDialog.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        SendMessageGroupDialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(SendMessageGroupDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.send_message_group = QGroupBox(SendMessageGroupDialog)
        self.send_message_group.setObjectName(u"send_message_group")
        self.horizontalLayout_2 = QHBoxLayout(self.send_message_group)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.send_message_input = QPlainTextEdit(self.send_message_group)
        self.send_message_input.setObjectName(u"send_message_input")
        font = QFont()
        font.setBold(True)
        self.send_message_input.setFont(font)

        self.horizontalLayout_2.addWidget(self.send_message_input)


        self.verticalLayout_3.addWidget(self.send_message_group)

        self.buttonBox = QDialogButtonBox(SendMessageGroupDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.buttonBox)

        self.verticalLayout_3.setStretch(0, 3)

        self.retranslateUi(SendMessageGroupDialog)
        self.buttonBox.accepted.connect(SendMessageGroupDialog.accept)
        self.buttonBox.rejected.connect(SendMessageGroupDialog.reject)

        QMetaObject.connectSlotsByName(SendMessageGroupDialog)
    # setupUi

    def retranslateUi(self, SendMessageGroupDialog):
        SendMessageGroupDialog.setWindowTitle(QCoreApplication.translate("SendMessageGroupDialog", u"Messaging", None))
        self.send_message_group.setTitle(QCoreApplication.translate("SendMessageGroupDialog", u"Message Input", None))
    # retranslateUi

