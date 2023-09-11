# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkDeviceSelectUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QSizePolicy, QWidget)
from Resources import Resources_rc

class Ui_NetworkDeviceSelectDialog(object):
    def setupUi(self, NetworkDeviceSelectDialog):
        if not NetworkDeviceSelectDialog.objectName():
            NetworkDeviceSelectDialog.setObjectName(u"NetworkDeviceSelectDialog")
        NetworkDeviceSelectDialog.resize(391, 111)
        NetworkDeviceSelectDialog.setMinimumSize(QSize(391, 111))
        NetworkDeviceSelectDialog.setMaximumSize(QSize(391, 111))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        NetworkDeviceSelectDialog.setWindowIcon(icon)
        self.operation_buttons = QDialogButtonBox(NetworkDeviceSelectDialog)
        self.operation_buttons.setObjectName(u"operation_buttons")
        self.operation_buttons.setGeometry(QRect(10, 60, 371, 41))
        self.operation_buttons.setOrientation(Qt.Horizontal)
        self.operation_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.operation_buttons.setCenterButtons(True)
        self.network_device_list = QComboBox(NetworkDeviceSelectDialog)
        self.network_device_list.setObjectName(u"network_device_list")
        self.network_device_list.setGeometry(QRect(20, 20, 351, 35))
        font = QFont()
        font.setPointSize(11)
        self.network_device_list.setFont(font)

        self.retranslateUi(NetworkDeviceSelectDialog)
        self.operation_buttons.accepted.connect(NetworkDeviceSelectDialog.accept)
        self.operation_buttons.rejected.connect(NetworkDeviceSelectDialog.reject)

        QMetaObject.connectSlotsByName(NetworkDeviceSelectDialog)
    # setupUi

    def retranslateUi(self, NetworkDeviceSelectDialog):
        NetworkDeviceSelectDialog.setWindowTitle(QCoreApplication.translate("NetworkDeviceSelectDialog", u"Network Settings", None))
    # retranslateUi

