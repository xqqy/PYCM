# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginUI.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from Resources import Resources_rc

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.setWindowModality(Qt.ApplicationModal)
        LoginForm.resize(331, 211)
        LoginForm.setMinimumSize(QSize(331, 211))
        LoginForm.setMaximumSize(QSize(331, 211))
        icon = QIcon()
        icon.addFile(u":/Core/Core/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginForm.setWindowIcon(icon)
        self.username = QLineEdit(LoginForm)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(124, 61, 181, 31))
        font = QFont()
        font.setPointSize(10)
        self.username.setFont(font)
        self.password = QLineEdit(LoginForm)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(124, 101, 181, 31))
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.Password)
        self.title = QLabel(LoginForm)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(24, 12, 261, 41))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.label_username = QLabel(LoginForm)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(24, 61, 101, 31))
        self.label_username.setFont(font)
        self.label_password = QLabel(LoginForm)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(24, 101, 101, 31))
        self.label_password.setFont(font)
        self.label_password.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.login_button = QPushButton(LoginForm)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(24, 150, 281, 41))
        font2 = QFont()
        font2.setPointSize(11)
        self.login_button.setFont(font2)
        self.title.raise_()
        self.label_username.raise_()
        self.label_password.raise_()
        self.login_button.raise_()
        self.password.raise_()
        self.username.raise_()

        self.retranslateUi(LoginForm)
        self.login_button.clicked.connect(LoginForm.login)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"PYCM Login", None))
        self.username.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Default: admin", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginForm", u"Default: 123456", None))
        self.title.setText(QCoreApplication.translate("LoginForm", u"PYCM Login", None))
        self.label_username.setText(QCoreApplication.translate("LoginForm", u"Username:", None))
        self.label_password.setText(QCoreApplication.translate("LoginForm", u"Password:", None))
        self.login_button.setText(QCoreApplication.translate("LoginForm", u"Login", None))
#if QT_CONFIG(shortcut)
        self.login_button.setShortcut(QCoreApplication.translate("LoginForm", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

