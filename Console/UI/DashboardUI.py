# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)
from Resources import Resources_rc

class Ui_DashboardForm(object):
    def setupUi(self, DashboardForm):
        if not DashboardForm.objectName():
            DashboardForm.setObjectName(u"DashboardForm")
        DashboardForm.resize(937, 635)
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        DashboardForm.setWindowIcon(icon)
        self.client_sort = QAction(DashboardForm)
        self.client_sort.setObjectName(u"client_sort")
        self.client_select_all = QAction(DashboardForm)
        self.client_select_all.setObjectName(u"client_select_all")
        self.client_scroll_in = QAction(DashboardForm)
        self.client_scroll_in.setObjectName(u"client_scroll_in")
        self.client_scroll_out = QAction(DashboardForm)
        self.client_scroll_out.setObjectName(u"client_scroll_out")
        self.client_rename = QAction(DashboardForm)
        self.client_rename.setObjectName(u"client_rename")
        self.about = QAction(DashboardForm)
        self.about.setObjectName(u"about")
        self.central_widget = QWidget(DashboardForm)
        self.central_widget.setObjectName(u"central_widget")
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setSpacing(4)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.central_widget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 35, 45, 255), stop:1 rgba(69, 83, 100, 255));\n"
"color: rgb(255, 255, 255);\n"
"padding-top: 5px;\n"
"padding-bottom: 5px;\n"
"")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setMargin(6)

        self.central_layout.addWidget(self.title)

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(7)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(11, 3, 11, 11)
        self.frame_header = QFrame(self.central_widget)
        self.frame_header.setObjectName(u"frame_header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_header.sizePolicy().hasHeightForWidth())
        self.frame_header.setSizePolicy(sizePolicy)
        self.frame_header.setMinimumSize(QSize(0, 0))
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Plain)
        self.frame_header_layout = QHBoxLayout(self.frame_header)
        self.frame_header_layout.setSpacing(8)
        self.frame_header_layout.setObjectName(u"frame_header_layout")
        self.frame_header_layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_broadcast = QPushButton(self.frame_header)
        self.toggle_broadcast.setObjectName(u"toggle_broadcast")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggle_broadcast.sizePolicy().hasHeightForWidth())
        self.toggle_broadcast.setSizePolicy(sizePolicy1)
        self.toggle_broadcast.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.toggle_broadcast.setFont(font1)
        self.toggle_broadcast.setCheckable(True)
        self.toggle_broadcast.setChecked(False)

        self.frame_header_layout.addWidget(self.toggle_broadcast)

        self.remote_spy = QPushButton(self.frame_header)
        self.remote_spy.setObjectName(u"remote_spy")
        sizePolicy1.setHeightForWidth(self.remote_spy.sizePolicy().hasHeightForWidth())
        self.remote_spy.setSizePolicy(sizePolicy1)
        self.remote_spy.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(12)
        self.remote_spy.setFont(font2)
        self.remote_spy.setCheckable(True)

        self.frame_header_layout.addWidget(self.remote_spy)

        self.remote_command = QPushButton(self.frame_header)
        self.remote_command.setObjectName(u"remote_command")
        sizePolicy1.setHeightForWidth(self.remote_command.sizePolicy().hasHeightForWidth())
        self.remote_command.setSizePolicy(sizePolicy1)
        self.remote_command.setMinimumSize(QSize(0, 0))
        self.remote_command.setFont(font2)

        self.frame_header_layout.addWidget(self.remote_command)

        self.file_share = QPushButton(self.frame_header)
        self.file_share.setObjectName(u"file_share")
        sizePolicy1.setHeightForWidth(self.file_share.sizePolicy().hasHeightForWidth())
        self.file_share.setSizePolicy(sizePolicy1)
        self.file_share.setMinimumSize(QSize(0, 0))
        self.file_share.setFont(font2)

        self.frame_header_layout.addWidget(self.file_share)


        self.main_layout.addWidget(self.frame_header)

        self.frame_body = QFrame(self.central_widget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setFrameShape(QFrame.NoFrame)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.frame_body_layout = QVBoxLayout(self.frame_body)
        self.frame_body_layout.setObjectName(u"frame_body_layout")
        self.frame_body_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_body_splitter = QSplitter(self.frame_body)
        self.frame_body_splitter.setObjectName(u"frame_body_splitter")
        self.frame_body_splitter.setOrientation(Qt.Horizontal)
        self.frame_body_splitter.setHandleWidth(4)
        self.desktop_widget_container = QWidget(self.frame_body_splitter)
        self.desktop_widget_container.setObjectName(u"desktop_widget_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(8)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.desktop_widget_container.sizePolicy().hasHeightForWidth())
        self.desktop_widget_container.setSizePolicy(sizePolicy2)
        self.desktop_widget_container_layout = QVBoxLayout(self.desktop_widget_container)
        self.desktop_widget_container_layout.setObjectName(u"desktop_widget_container_layout")
        self.desktop_widget_container_layout.setContentsMargins(0, 0, 5, 0)
        self.desktop_layout = QListWidget(self.desktop_widget_container)
        self.desktop_layout.setObjectName(u"desktop_layout")
        font3 = QFont()
        font3.setPointSize(10)
        self.desktop_layout.setFont(font3)
        self.desktop_layout.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.desktop_layout.setProperty("showDropIndicator", False)
        self.desktop_layout.setDragDropMode(QAbstractItemView.DragDrop)
        self.desktop_layout.setDefaultDropAction(Qt.IgnoreAction)
        self.desktop_layout.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.desktop_layout.setIconSize(QSize(240, 135))
        self.desktop_layout.setMovement(QListView.Free)
        self.desktop_layout.setResizeMode(QListView.Adjust)
        self.desktop_layout.setViewMode(QListView.IconMode)

        self.desktop_widget_container_layout.addWidget(self.desktop_layout)

        self.frame_body_splitter.addWidget(self.desktop_widget_container)
        self.log_widget_container = QWidget(self.frame_body_splitter)
        self.log_widget_container.setObjectName(u"log_widget_container")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.log_widget_container.sizePolicy().hasHeightForWidth())
        self.log_widget_container.setSizePolicy(sizePolicy3)
        self.log_widget_container_layout = QVBoxLayout(self.log_widget_container)
        self.log_widget_container_layout.setObjectName(u"log_widget_container_layout")
        self.log_widget_container_layout.setContentsMargins(5, 0, 0, 0)
        self.log_area = QTextBrowser(self.log_widget_container)
        self.log_area.setObjectName(u"log_area")
        self.log_area.setFont(font3)
        self.log_area.setReadOnly(True)
        self.log_area.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.log_area.setOpenLinks(False)

        self.log_widget_container_layout.addWidget(self.log_area)

        self.action_buttons_layout_2 = QHBoxLayout()
        self.action_buttons_layout_2.setObjectName(u"action_buttons_layout_2")
        self.file_receive_config = QPushButton(self.log_widget_container)
        self.file_receive_config.setObjectName(u"file_receive_config")

        self.action_buttons_layout_2.addWidget(self.file_receive_config)

        self.client_quit = QPushButton(self.log_widget_container)
        self.client_quit.setObjectName(u"client_quit")

        self.action_buttons_layout_2.addWidget(self.client_quit)


        self.log_widget_container_layout.addLayout(self.action_buttons_layout_2)

        self.action_buttons_layout_1 = QHBoxLayout()
        self.action_buttons_layout_1.setObjectName(u"action_buttons_layout_1")
        self.send_message_button = QPushButton(self.log_widget_container)
        self.send_message_button.setObjectName(u"send_message_button")
        sizePolicy1.setHeightForWidth(self.send_message_button.sizePolicy().hasHeightForWidth())
        self.send_message_button.setSizePolicy(sizePolicy1)
        self.send_message_button.setMaximumSize(QSize(16777215, 16777215))

        self.action_buttons_layout_1.addWidget(self.send_message_button)

        self.clear_log_area = QPushButton(self.log_widget_container)
        self.clear_log_area.setObjectName(u"clear_log_area")
        sizePolicy1.setHeightForWidth(self.clear_log_area.sizePolicy().hasHeightForWidth())
        self.clear_log_area.setSizePolicy(sizePolicy1)

        self.action_buttons_layout_1.addWidget(self.clear_log_area)


        self.log_widget_container_layout.addLayout(self.action_buttons_layout_1)

        self.frame_body_splitter.addWidget(self.log_widget_container)

        self.frame_body_layout.addWidget(self.frame_body_splitter)


        self.main_layout.addWidget(self.frame_body)

        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 30)

        self.central_layout.addLayout(self.main_layout)

        DashboardForm.setCentralWidget(self.central_widget)
        self.tool_bar = QToolBar(DashboardForm)
        self.tool_bar.setObjectName(u"tool_bar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tool_bar.sizePolicy().hasHeightForWidth())
        self.tool_bar.setSizePolicy(sizePolicy4)
        self.tool_bar.setMinimumSize(QSize(0, 0))
        self.tool_bar.setBaseSize(QSize(0, 0))
        self.tool_bar.setWindowTitle(u"toolBar")
        self.tool_bar.setStyleSheet(u"height: 20px")
        self.tool_bar.setMovable(False)
        self.tool_bar.setAllowedAreas(Qt.BottomToolBarArea)
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.tool_bar.setFloatable(False)
        DashboardForm.addToolBar(Qt.BottomToolBarArea, self.tool_bar)

        self.tool_bar.addAction(self.client_sort)
        self.tool_bar.addAction(self.client_select_all)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.client_rename)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.client_scroll_in)
        self.tool_bar.addAction(self.client_scroll_out)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.about)

        self.retranslateUi(DashboardForm)
        self.client_select_all.triggered.connect(self.desktop_layout.selectAll)
        self.client_sort.triggered.connect(self.desktop_layout.doItemsLayout)
        self.client_scroll_in.triggered.connect(DashboardForm.client_scroll_in)
        self.client_scroll_out.triggered.connect(DashboardForm.client_scroll_out)
        self.send_message_button.clicked.connect(DashboardForm.send_message)
        self.toggle_broadcast.clicked["bool"].connect(DashboardForm.toggle_broadcast)
        self.remote_command.clicked.connect(DashboardForm.remote_command)
        self.remote_spy.clicked["bool"].connect(DashboardForm.toggle_remote_spy)
        self.client_rename.triggered.connect(DashboardForm.client_rename)
        self.about.triggered.connect(DashboardForm.show_about)
        self.file_receive_config.clicked.connect(DashboardForm.show_file_receive)
        self.client_quit.clicked.connect(DashboardForm.client_quit)
        self.clear_log_area.clicked.connect(self.log_area.clear)
        self.log_area.anchorClicked.connect(DashboardForm.show_file_receive)
        self.file_share.clicked.connect(DashboardForm.show_file_server)

        QMetaObject.connectSlotsByName(DashboardForm)
    # setupUi

    def retranslateUi(self, DashboardForm):
        DashboardForm.setWindowTitle(QCoreApplication.translate("DashboardForm", u"PYCM Dashboard", None))
        self.client_sort.setText(QCoreApplication.translate("DashboardForm", u"Arrange Client", None))
        self.client_select_all.setText(QCoreApplication.translate("DashboardForm", u"Select All", None))
        self.client_scroll_in.setText(QCoreApplication.translate("DashboardForm", u"Zoom In", None))
        self.client_scroll_out.setText(QCoreApplication.translate("DashboardForm", u"Zoom Out", None))
        self.client_rename.setText(QCoreApplication.translate("DashboardForm", u"Rename", None))
        self.about.setText(QCoreApplication.translate("DashboardForm", u"About", None))
        self.title.setText(QCoreApplication.translate("DashboardForm", u"Python Classroom Management System", None))
        self.toggle_broadcast.setText(QCoreApplication.translate("DashboardForm", u"Screen Broadcast", None))
        self.remote_spy.setText(QCoreApplication.translate("DashboardForm", u"Remote View", None))
        self.remote_command.setText(QCoreApplication.translate("DashboardForm", u"Remote Command", None))
        self.file_share.setText(QCoreApplication.translate("DashboardForm", u"File Share", None))
        self.file_receive_config.setText(QCoreApplication.translate("DashboardForm", u"File Receive", None))
        self.client_quit.setText(QCoreApplication.translate("DashboardForm", u"Quit Client", None))
        self.send_message_button.setText(QCoreApplication.translate("DashboardForm", u"Messaging", None))
        self.clear_log_area.setText(QCoreApplication.translate("DashboardForm", u"Clear Log", None))
    # retranslateUi

