# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteCommandGroupAddUI.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_RemoteCommandGroupAddDialog(object):
    def setupUi(self, RemoteCommandGroupAddDialog):
        if not RemoteCommandGroupAddDialog.objectName():
            RemoteCommandGroupAddDialog.setObjectName(u"RemoteCommandGroupAddDialog")
        RemoteCommandGroupAddDialog.resize(343, 284)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RemoteCommandGroupAddDialog.sizePolicy().hasHeightForWidth())
        RemoteCommandGroupAddDialog.setSizePolicy(sizePolicy)
        RemoteCommandGroupAddDialog.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        RemoteCommandGroupAddDialog.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(RemoteCommandGroupAddDialog)
        self.main_layout.setObjectName(u"main_layout")
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_label = QLabel(RemoteCommandGroupAddDialog)
        self.title_label.setObjectName(u"title_label")

        self.title_layout.addWidget(self.title_label)

        self.title = QLineEdit(RemoteCommandGroupAddDialog)
        self.title.setObjectName(u"title")

        self.title_layout.addWidget(self.title)


        self.main_layout.addLayout(self.title_layout)

        self.command_layout = QHBoxLayout()
        self.command_layout.setObjectName(u"command_layout")
        self.command_label = QLabel(RemoteCommandGroupAddDialog)
        self.command_label.setObjectName(u"command_label")

        self.command_layout.addWidget(self.command_label)

        self.command = QPlainTextEdit(RemoteCommandGroupAddDialog)
        self.command.setObjectName(u"command")

        self.command_layout.addWidget(self.command)


        self.main_layout.addLayout(self.command_layout)

        self.button_box = QDialogButtonBox(RemoteCommandGroupAddDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.button_box.setCenterButtons(True)

        self.main_layout.addWidget(self.button_box)


        self.retranslateUi(RemoteCommandGroupAddDialog)
        self.button_box.accepted.connect(RemoteCommandGroupAddDialog.accept)
        self.button_box.rejected.connect(RemoteCommandGroupAddDialog.reject)

        QMetaObject.connectSlotsByName(RemoteCommandGroupAddDialog)
    # setupUi

    def retranslateUi(self, RemoteCommandGroupAddDialog):
        RemoteCommandGroupAddDialog.setWindowTitle(QCoreApplication.translate("RemoteCommandGroupAddDialog", u"Add Remote Command", None))
        self.title_label.setText(QCoreApplication.translate("RemoteCommandGroupAddDialog", u"Name", None))
        self.command_label.setText(QCoreApplication.translate("RemoteCommandGroupAddDialog", u"Command", None))
    # retranslateUi

