# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScreenBroadcastUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_ScreenBroadcastForm(object):
    def setupUi(self, ScreenBroadcastForm):
        if not ScreenBroadcastForm.objectName():
            ScreenBroadcastForm.setObjectName(u"ScreenBroadcastForm")
        ScreenBroadcastForm.resize(1244, 827)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScreenBroadcastForm.sizePolicy().hasHeightForWidth())
        ScreenBroadcastForm.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        ScreenBroadcastForm.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(ScreenBroadcastForm)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(18, -1, 18, -1)
        self.control_box_layout = QHBoxLayout()
        self.control_box_layout.setObjectName(u"control_box_layout")
        self.freeze_frame = QPushButton(ScreenBroadcastForm)
        self.freeze_frame.setObjectName(u"freeze_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.freeze_frame.sizePolicy().hasHeightForWidth())
        self.freeze_frame.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.freeze_frame.setFont(font)
        self.freeze_frame.setCheckable(True)

        self.control_box_layout.addWidget(self.freeze_frame)

        self.full_screen = QPushButton(ScreenBroadcastForm)
        self.full_screen.setObjectName(u"full_screen")
        sizePolicy1.setHeightForWidth(self.full_screen.sizePolicy().hasHeightForWidth())
        self.full_screen.setSizePolicy(sizePolicy1)
        self.full_screen.setFont(font)
        self.full_screen.setCheckable(True)

        self.control_box_layout.addWidget(self.full_screen)

        self.screen_shot = QPushButton(ScreenBroadcastForm)
        self.screen_shot.setObjectName(u"screen_shot")
        sizePolicy1.setHeightForWidth(self.screen_shot.sizePolicy().hasHeightForWidth())
        self.screen_shot.setSizePolicy(sizePolicy1)
        self.screen_shot.setFont(font)

        self.control_box_layout.addWidget(self.screen_shot)

        self.always_on_top = QPushButton(ScreenBroadcastForm)
        self.always_on_top.setObjectName(u"always_on_top")
        sizePolicy1.setHeightForWidth(self.always_on_top.sizePolicy().hasHeightForWidth())
        self.always_on_top.setSizePolicy(sizePolicy1)
        self.always_on_top.setFont(font)
        self.always_on_top.setCheckable(True)
        self.always_on_top.setChecked(True)

        self.control_box_layout.addWidget(self.always_on_top)


        self.main_layout.addLayout(self.control_box_layout)

        self.screen_widget = QWidget(ScreenBroadcastForm)
        self.screen_widget.setObjectName(u"screen_widget")
        self.screen_widget.setStyleSheet(u"#screen_widget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(82, 229, 231, 255), stop:1 rgba(19, 12, 183, 255));\n"
"}")
        self.screen_display = QLabel(self.screen_widget)
        self.screen_display.setObjectName(u"screen_display")
        self.screen_display.setGeometry(QRect(0, 0, 421, 341))
        self.screen_display.setScaledContents(True)

        self.main_layout.addWidget(self.screen_widget)

        self.main_layout.setStretch(1, 50)

        self.retranslateUi(ScreenBroadcastForm)
        self.freeze_frame.clicked["bool"].connect(ScreenBroadcastForm.freeze_frame)
        self.full_screen.clicked["bool"].connect(ScreenBroadcastForm.show_full_screen)
        self.screen_shot.clicked.connect(ScreenBroadcastForm.screen_shot)
        self.always_on_top.clicked["bool"].connect(ScreenBroadcastForm.toggle_always_on_top)

        QMetaObject.connectSlotsByName(ScreenBroadcastForm)
    # setupUi

    def retranslateUi(self, ScreenBroadcastForm):
        ScreenBroadcastForm.setWindowTitle(QCoreApplication.translate("ScreenBroadcastForm", u"Screen Broadcast", None))
        self.freeze_frame.setText(QCoreApplication.translate("ScreenBroadcastForm", u"Freeze Screen", None))
        self.full_screen.setText(QCoreApplication.translate("ScreenBroadcastForm", u"Full Screen", None))
        self.screen_shot.setText(QCoreApplication.translate("ScreenBroadcastForm", u"Screen Shot", None))
        self.always_on_top.setText(QCoreApplication.translate("ScreenBroadcastForm", u"Always On Top", None))
        self.screen_display.setText("")
    # retranslateUi

