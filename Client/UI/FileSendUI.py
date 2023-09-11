# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileSendUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_FileSendForm(object):
    def setupUi(self, FileSendForm):
        if not FileSendForm.objectName():
            FileSendForm.setObjectName(u"FileSendForm")
        FileSendForm.setWindowModality(Qt.ApplicationModal)
        FileSendForm.resize(499, 338)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FileSendForm.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(FileSendForm)
        self.main_layout.setObjectName(u"main_layout")
        self.header_layout = QHBoxLayout()
        self.header_layout.setSpacing(0)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(2, 2, 2, 2)
        self.add_file_button = QPushButton(FileSendForm)
        self.add_file_button.setObjectName(u"add_file_button")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_file_button.sizePolicy().hasHeightForWidth())
        self.add_file_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.add_file_button.setFont(font)

        self.header_layout.addWidget(self.add_file_button)

        self.delete_file_button = QPushButton(FileSendForm)
        self.delete_file_button.setObjectName(u"delete_file_button")
        sizePolicy.setHeightForWidth(self.delete_file_button.sizePolicy().hasHeightForWidth())
        self.delete_file_button.setSizePolicy(sizePolicy)
        self.delete_file_button.setFont(font)

        self.header_layout.addWidget(self.delete_file_button)

        self.submit_file_button = QPushButton(FileSendForm)
        self.submit_file_button.setObjectName(u"submit_file_button")
        sizePolicy.setHeightForWidth(self.submit_file_button.sizePolicy().hasHeightForWidth())
        self.submit_file_button.setSizePolicy(sizePolicy)
        self.submit_file_button.setFont(font)

        self.header_layout.addWidget(self.submit_file_button)


        self.main_layout.addLayout(self.header_layout)

        self.file_list_container_widget = QWidget(FileSendForm)
        self.file_list_container_widget.setObjectName(u"file_list_container_widget")
        self.file_list_container = QVBoxLayout(self.file_list_container_widget)
        self.file_list_container.setObjectName(u"file_list_container")
        self.file_list_container.setContentsMargins(0, 0, 0, 0)

        self.main_layout.addWidget(self.file_list_container_widget)

        self.progress_layout = QHBoxLayout()
        self.progress_layout.setObjectName(u"progress_layout")
        self.file_send_progress_label = QLabel(FileSendForm)
        self.file_send_progress_label.setObjectName(u"file_send_progress_label")

        self.progress_layout.addWidget(self.file_send_progress_label)

        self.file_send_progress_bar = QProgressBar(FileSendForm)
        self.file_send_progress_bar.setObjectName(u"file_send_progress_bar")
        self.file_send_progress_bar.setFont(font)
        self.file_send_progress_bar.setValue(0)
        self.file_send_progress_bar.setTextVisible(True)
        self.file_send_progress_bar.setOrientation(Qt.Horizontal)

        self.progress_layout.addWidget(self.file_send_progress_bar)


        self.main_layout.addLayout(self.progress_layout)

        self.main_layout.setStretch(1, 1)

        self.retranslateUi(FileSendForm)
        self.delete_file_button.clicked.connect(FileSendForm.delete_selected_files)
        self.add_file_button.clicked.connect(FileSendForm.show_add_file_dialog)
        self.submit_file_button.clicked.connect(FileSendForm.send_all)

        QMetaObject.connectSlotsByName(FileSendForm)
    # setupUi

    def retranslateUi(self, FileSendForm):
        FileSendForm.setWindowTitle(QCoreApplication.translate("FileSendForm", u"Submit Files", None))
        self.add_file_button.setText(QCoreApplication.translate("FileSendForm", u"Add Files", None))
        self.delete_file_button.setText(QCoreApplication.translate("FileSendForm", u"Remove Selected Files", None))
        self.submit_file_button.setText(QCoreApplication.translate("FileSendForm", u"Submit All Files", None))
        self.file_send_progress_label.setText(QCoreApplication.translate("FileSendForm", u"Ready", None))
    # retranslateUi

