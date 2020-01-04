# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web_browser.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1023, 576)
        self.browser = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.browser.setGeometry(QtCore.QRect(39, 79, 961, 471))
        self.browser.setMinimumSize(QtCore.QSize(961, 0))
        self.browser.setObjectName("browser")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 10, 521, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.UrlLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.UrlLineEdit.setObjectName("UrlLineEdit")
        self.horizontalLayout.addWidget(self.UrlLineEdit)
        self.SubmitPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SubmitPushButton.setObjectName("SubmitPushButton")
        self.horizontalLayout.addWidget(self.SubmitPushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL: "))
        self.SubmitPushButton.setText(_translate("Dialog", "Go"))
from PyQt5 import QtWebEngineWidgets
