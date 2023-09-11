# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileReceiveUI.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from Resources import Resources_rc

class Ui_FileReceiveDialog(object):
    def setupUi(self, FileReceiveDialog):
        if not FileReceiveDialog.objectName():
            FileReceiveDialog.setObjectName(u"FileReceiveDialog")
        FileReceiveDialog.resize(530, 311)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileReceiveDialog.sizePolicy().hasHeightForWidth())
        FileReceiveDialog.setSizePolicy(sizePolicy)
        FileReceiveDialog.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        FileReceiveDialog.setWindowIcon(icon)
        self.main_layout = QVBoxLayout(FileReceiveDialog)
        self.main_layout.setObjectName(u"main_layout")
        self.receive_folder_layout = QHBoxLayout()
        self.receive_folder_layout.setObjectName(u"receive_folder_layout")
        self.receive_folder_label = QLabel(FileReceiveDialog)
        self.receive_folder_label.setObjectName(u"receive_folder_label")

        self.receive_folder_layout.addWidget(self.receive_folder_label)

        self.receive_folder = QLineEdit(FileReceiveDialog)
        self.receive_folder.setObjectName(u"receive_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.receive_folder.sizePolicy().hasHeightForWidth())
        self.receive_folder.setSizePolicy(sizePolicy1)
        self.receive_folder.setReadOnly(True)

        self.receive_folder_layout.addWidget(self.receive_folder)

        self.receive_folder_change = QPushButton(FileReceiveDialog)
        self.receive_folder_change.setObjectName(u"receive_folder_change")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.receive_folder_change.sizePolicy().hasHeightForWidth())
        self.receive_folder_change.setSizePolicy(sizePolicy2)

        self.receive_folder_layout.addWidget(self.receive_folder_change)

        self.receive_folder_open = QPushButton(FileReceiveDialog)
        self.receive_folder_open.setObjectName(u"receive_folder_open")
        sizePolicy2.setHeightForWidth(self.receive_folder_open.sizePolicy().hasHeightForWidth())
        self.receive_folder_open.setSizePolicy(sizePolicy2)

        self.receive_folder_layout.addWidget(self.receive_folder_open)


        self.main_layout.addLayout(self.receive_folder_layout)

        self.received_files = QTableWidget(FileReceiveDialog)
        if (self.received_files.columnCount() < 2):
            self.received_files.setColumnCount(2)
        font = QFont()
        font.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.received_files.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.received_files.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.received_files.setObjectName(u"received_files")
        self.received_files.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.received_files.setAlternatingRowColors(True)
        self.received_files.setSelectionMode(QAbstractItemView.SingleSelection)
        self.received_files.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.received_files.verticalHeader().setVisible(False)

        self.main_layout.addWidget(self.received_files)

        self.show_selected_file_guide = QLabel(FileReceiveDialog)
        self.show_selected_file_guide.setObjectName(u"show_selected_file_guide")
        self.show_selected_file_guide.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(self.show_selected_file_guide)


        self.retranslateUi(FileReceiveDialog)
        self.receive_folder_change.clicked.connect(FileReceiveDialog.change_receive_folder)
        self.receive_folder_open.clicked.connect(FileReceiveDialog.open_receive_folder)
        self.received_files.itemDoubleClicked.connect(FileReceiveDialog.open_selected_file)

        QMetaObject.connectSlotsByName(FileReceiveDialog)
    # setupUi

    def retranslateUi(self, FileReceiveDialog):
        FileReceiveDialog.setWindowTitle(QCoreApplication.translate("FileReceiveDialog", u"File Receive", None))
        self.receive_folder_label.setText(QCoreApplication.translate("FileReceiveDialog", u"Receive Folder: ", None))
        self.receive_folder_change.setText(QCoreApplication.translate("FileReceiveDialog", u"Change", None))
        self.receive_folder_open.setText(QCoreApplication.translate("FileReceiveDialog", u"Open", None))
        ___qtablewidgetitem = self.received_files.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FileReceiveDialog", u"File Name", None));
        ___qtablewidgetitem1 = self.received_files.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FileReceiveDialog", u"From", None));
        self.show_selected_file_guide.setText(QCoreApplication.translate("FileReceiveDialog", u"Double click the row to open file", None))
    # retranslateUi

