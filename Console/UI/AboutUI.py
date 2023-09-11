# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutUI.ui'
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
    QGroupBox, QLabel, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(487, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(AboutDialog)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(25, 20, 25, 20)
        self.title_layout = QVBoxLayout()
        self.title_layout.setSpacing(0)
        self.title_layout.setObjectName(u"title_layout")
        self.productName = QLabel(AboutDialog)
        self.productName.setObjectName(u"productName")
        font = QFont()
        font.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font.setPointSize(13)
        font.setBold(True)
        self.productName.setFont(font)
        self.productName.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.productName)

        self.buildInfo = QLabel(AboutDialog)
        self.buildInfo.setObjectName(u"buildInfo")
        font1 = QFont()
        font1.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        self.buildInfo.setFont(font1)
        self.buildInfo.setAlignment(Qt.AlignCenter)

        self.title_layout.addWidget(self.buildInfo)

        self.project_home = QLabel(AboutDialog)
        self.project_home.setObjectName(u"project_home")
        self.project_home.setFont(font1)
        self.project_home.setText(u"<html><head/><body><p><a href=\"https://github.com/yangzhongtian001/PYCM\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/yangzhongtian001/PYCM</span></a></p></body></html>")
        self.project_home.setAlignment(Qt.AlignCenter)
        self.project_home.setOpenExternalLinks(True)

        self.title_layout.addWidget(self.project_home)

        self.thanks_info = QLabel(AboutDialog)
        self.thanks_info.setObjectName(u"thanks_info")
        self.thanks_info.setText(u"<html><head/><body><p>RichardYangZT(<a href=\"www.52pojie.cn\"><span style=\" text-decoration: underline; color:#0000ff;\">www.52pojie.cn</span></a>)</p></body></html>")
        self.thanks_info.setAlignment(Qt.AlignCenter)
        self.thanks_info.setOpenExternalLinks(True)

        self.title_layout.addWidget(self.thanks_info)


        self.main_layout.addLayout(self.title_layout)

        self.license_group = QGroupBox(AboutDialog)
        self.license_group.setObjectName(u"license_group")
        self.license_group.setFont(font1)
        self.license_group.setAlignment(Qt.AlignCenter)
        self.license_group_layout = QVBoxLayout(self.license_group)
        self.license_group_layout.setObjectName(u"license_group_layout")
        self.license_view = QTextBrowser(self.license_group)
        self.license_view.setObjectName(u"license_view")
        font2 = QFont()
        font2.setFamilies([u"\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53"])
        font2.setBold(True)
        self.license_view.setFont(font2)
        self.license_view.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53','\u963f\u91cc\u5df4\u5df4\u666e\u60e0\u4f53'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:10pt; font-weight:400;\">This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or at your option any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';"
                        " font-size:10pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:10pt; font-weight:400;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun'; font-size:10pt; font-weight:400;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:10pt; font-weight:400;\">You should have received a copy of the GNU General Public License along with this program. If not, see &lt;</span><a href=\""
                        "https://www.gnu.org/licenses/\"><span style=\" font-family:'SimSun'; font-size:10pt; font-weight:400; text-decoration: underline; color:#0000ff;\">https://www.gnu.org/licenses/</span></a><span style=\" font-family:'SimSun'; font-size:10pt; font-weight:400;\">&gt;.</span></p></body></html>")
        self.license_view.setOpenExternalLinks(True)

        self.license_group_layout.addWidget(self.license_view)


        self.main_layout.addWidget(self.license_group)

        self.operation_buttons = QDialogButtonBox(AboutDialog)
        self.operation_buttons.setObjectName(u"operation_buttons")
        self.operation_buttons.setOrientation(Qt.Horizontal)
        self.operation_buttons.setStandardButtons(QDialogButtonBox.Ok)
        self.operation_buttons.setCenterButtons(True)

        self.main_layout.addWidget(self.operation_buttons)


        self.retranslateUi(AboutDialog)
        self.operation_buttons.accepted.connect(AboutDialog.accept)
        self.operation_buttons.rejected.connect(AboutDialog.reject)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.productName.setText(QCoreApplication.translate("AboutDialog", u"PYCM Console", None))
        self.buildInfo.setText(QCoreApplication.translate("AboutDialog", u"No build info", None))
        self.license_group.setTitle(QCoreApplication.translate("AboutDialog", u"GNU General Public License", None))
    # retranslateUi

