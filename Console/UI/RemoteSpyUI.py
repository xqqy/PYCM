# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteSpyUI.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
from Resources import Resources_rc

class Ui_RemoteSpy(object):
    def setupUi(self, RemoteSpy):
        if not RemoteSpy.objectName():
            RemoteSpy.setObjectName(u"RemoteSpy")
        RemoteSpy.resize(971, 598)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RemoteSpy.sizePolicy().hasHeightForWidth())
        RemoteSpy.setSizePolicy(sizePolicy)
        RemoteSpy.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        RemoteSpy.setWindowIcon(icon)
        self.screen_display = QLabel(RemoteSpy)
        self.screen_display.setObjectName(u"screen_display")
        self.screen_display.setGeometry(QRect(0, 0, 421, 341))
        self.screen_display.setMouseTracking(True)
        self.screen_display.setScaledContents(True)

        self.retranslateUi(RemoteSpy)

        QMetaObject.connectSlotsByName(RemoteSpy)
    # setupUi

    def retranslateUi(self, RemoteSpy):
        RemoteSpy.setWindowTitle(QCoreApplication.translate("RemoteSpy", u"Remote View", None))
        self.screen_display.setText("")
    # retranslateUi

