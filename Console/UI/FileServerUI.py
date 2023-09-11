# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileServerUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from Resources import Resources_rc

class Ui_FileServerForm(object):
    def setupUi(self, FileServerForm):
        if not FileServerForm.objectName():
            FileServerForm.setObjectName(u"FileServerForm")
        FileServerForm.resize(422, 91)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileServerForm.sizePolicy().hasHeightForWidth())
        FileServerForm.setSizePolicy(sizePolicy)
        FileServerForm.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FileServerForm.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(FileServerForm)
        self.main_layout.setObjectName(u"main_layout")
        self.working_folder_layout = QHBoxLayout()
        self.working_folder_layout.setObjectName(u"working_folder_layout")
        self.working_folder_label = QLabel(FileServerForm)
        self.working_folder_label.setObjectName(u"working_folder_label")

        self.working_folder_layout.addWidget(self.working_folder_label)

        self.working_folder = QLineEdit(FileServerForm)
        self.working_folder.setObjectName(u"working_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.working_folder.sizePolicy().hasHeightForWidth())
        self.working_folder.setSizePolicy(sizePolicy1)
        self.working_folder.setText(u"")
        self.working_folder.setReadOnly(True)

        self.working_folder_layout.addWidget(self.working_folder)

        self.working_folder_change = QPushButton(FileServerForm)
        self.working_folder_change.setObjectName(u"working_folder_change")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.working_folder_change.sizePolicy().hasHeightForWidth())
        self.working_folder_change.setSizePolicy(sizePolicy2)

        self.working_folder_layout.addWidget(self.working_folder_change)


        self.main_layout.addLayout(self.working_folder_layout)

        self.server_info_layout = QHBoxLayout()
        self.server_info_layout.setObjectName(u"server_info_layout")
        self.server_info = QLabel(FileServerForm)
        self.server_info.setObjectName(u"server_info")

        self.server_info_layout.addWidget(self.server_info)

        self.toggle_working = QPushButton(FileServerForm)
        self.toggle_working.setObjectName(u"toggle_working")
        sizePolicy2.setHeightForWidth(self.toggle_working.sizePolicy().hasHeightForWidth())
        self.toggle_working.setSizePolicy(sizePolicy2)

        self.server_info_layout.addWidget(self.toggle_working)


        self.main_layout.addLayout(self.server_info_layout)


        self.retranslateUi(FileServerForm)
        self.working_folder_change.clicked.connect(FileServerForm.change_working_folder)
        self.toggle_working.clicked.connect(FileServerForm.toggle_server)

        QMetaObject.connectSlotsByName(FileServerForm)
    # setupUi

    def retranslateUi(self, FileServerForm):
        FileServerForm.setWindowTitle(QCoreApplication.translate("FileServerForm", u"File Server", None))
        self.working_folder_label.setText(QCoreApplication.translate("FileServerForm", u"Target Folder: ", None))
        self.working_folder_change.setText(QCoreApplication.translate("FileServerForm", u"Change", None))
        self.server_info.setText(QCoreApplication.translate("FileServerForm", u"Server Status: Stopped", None))
        self.toggle_working.setText(QCoreApplication.translate("FileServerForm", u"Start", None))
    # retranslateUi

