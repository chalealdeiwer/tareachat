# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class LoginForm(object):
    def setupUi(self, loginForm):
        if not loginForm.objectName():
            loginForm.setObjectName(u"loginForm")
        loginForm.resize(316, 242)
        self.frame = QFrame(loginForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 316, 80))
        self.frame.setStyleSheet(u"background-color: #CBE896")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 316, 80))
        self.label.setStyleSheet(u"color: white;")
        self.label_2 = QLabel(loginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 120, 131, 16))
        self.usernameLineEdit = QLineEdit(loginForm)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(50, 140, 201, 22))
        self.joinButton = QPushButton(loginForm)
        self.joinButton.setObjectName(u"joinButton")
        self.joinButton.setGeometry(QRect(80, 180, 151, 23))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.joinButton.setFont(font)
        self.joinButton.setStyleSheet(u"color: white;\n"
"background-color: #A18276")

        self.retranslateUi(loginForm)

        QMetaObject.connectSlotsByName(loginForm)
    # setupUi

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(QCoreApplication.translate("loginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("loginForm", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#3b00a1;\">CHAT PYTHON</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("loginForm", u"NOMBRE DE USUARIO", None))
        self.joinButton.setText(QCoreApplication.translate("loginForm", u"Ingresar al Chat", None))
    # retranslateUi

