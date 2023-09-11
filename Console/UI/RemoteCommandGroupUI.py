# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteCommandGroupUI.ui'
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
    QGroupBox, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from Resources import Resources_rc

class Ui_RemoteCommandGroupDialog(object):
    def setupUi(self, RemoteCommandGroupDialog):
        if not RemoteCommandGroupDialog.objectName():
            RemoteCommandGroupDialog.setObjectName(u"RemoteCommandGroupDialog")
        RemoteCommandGroupDialog.resize(390, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RemoteCommandGroupDialog.sizePolicy().hasHeightForWidth())
        RemoteCommandGroupDialog.setSizePolicy(sizePolicy)
        RemoteCommandGroupDialog.setMinimumSize(QSize(390, 350))
        RemoteCommandGroupDialog.setMaximumSize(QSize(390, 350))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        RemoteCommandGroupDialog.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(RemoteCommandGroupDialog)
        self.main_layout.setObjectName(u"main_layout")
        self.command_group = QGroupBox(RemoteCommandGroupDialog)
        self.command_group.setObjectName(u"command_group")
        self.command_group_layout = QHBoxLayout(self.command_group)
        self.command_group_layout.setObjectName(u"command_group_layout")
        self.command_group_layout.setContentsMargins(11, 11, 11, 11)
        self.command_select = QListWidget(self.command_group)
        self.command_select.setObjectName(u"command_select")
        font = QFont()
        font.setBold(True)
        self.command_select.setFont(font)

        self.command_group_layout.addWidget(self.command_select)

        self.command_edit_layout = QVBoxLayout()
        self.command_edit_layout.setObjectName(u"command_edit_layout")
        self.command_add = QPushButton(self.command_group)
        self.command_add.setObjectName(u"command_add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.command_add.sizePolicy().hasHeightForWidth())
        self.command_add.setSizePolicy(sizePolicy1)
        self.command_add.setMinimumSize(QSize(30, 30))
        self.command_add.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.command_add.setFont(font1)
        self.command_add.setText(u"+")

        self.command_edit_layout.addWidget(self.command_add)

        self.command_remove = QPushButton(self.command_group)
        self.command_remove.setObjectName(u"command_remove")
        sizePolicy.setHeightForWidth(self.command_remove.sizePolicy().hasHeightForWidth())
        self.command_remove.setSizePolicy(sizePolicy)
        self.command_remove.setMinimumSize(QSize(30, 30))
        self.command_remove.setMaximumSize(QSize(30, 30))
        self.command_remove.setFont(font1)
        self.command_remove.setText(u"-")

        self.command_edit_layout.addWidget(self.command_remove)

        self.vertical_spacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.command_edit_layout.addItem(self.vertical_spacer)


        self.command_group_layout.addLayout(self.command_edit_layout)

        self.command_group_layout.setStretch(0, 10)
        self.command_group_layout.setStretch(1, 1)

        self.main_layout.addWidget(self.command_group)

        self.operation_buttons = QDialogButtonBox(RemoteCommandGroupDialog)
        self.operation_buttons.setObjectName(u"operation_buttons")
        self.operation_buttons.setOrientation(Qt.Horizontal)
        self.operation_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.operation_buttons.setCenterButtons(True)

        self.main_layout.addWidget(self.operation_buttons)

        self.main_layout.setStretch(0, 5)

        self.retranslateUi(RemoteCommandGroupDialog)
        self.operation_buttons.accepted.connect(RemoteCommandGroupDialog.accept)
        self.operation_buttons.rejected.connect(RemoteCommandGroupDialog.reject)
        self.command_add.clicked.connect(RemoteCommandGroupDialog.add_command)
        self.command_remove.clicked.connect(RemoteCommandGroupDialog.remove_command)

        QMetaObject.connectSlotsByName(RemoteCommandGroupDialog)
    # setupUi

    def retranslateUi(self, RemoteCommandGroupDialog):
        RemoteCommandGroupDialog.setWindowTitle(QCoreApplication.translate("RemoteCommandGroupDialog", u"Remote Command", None))
        self.command_group.setTitle(QCoreApplication.translate("RemoteCommandGroupDialog", u"Command Select", None))
    # retranslateUi

