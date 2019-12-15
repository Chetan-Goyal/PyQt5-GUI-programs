# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_name.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 142)
        self.Response = QtWidgets.QLineEdit(Dialog)
        self.Response.setGeometry(QtCore.QRect(180, 30, 113, 25))
        self.Response.setText("")
        self.Response.setObjectName("Response")
        self.FinalOutput = QtWidgets.QLabel(Dialog)
        self.FinalOutput.setGeometry(QtCore.QRect(110, 90, 171, 20))
        self.FinalOutput.setText("")
        self.FinalOutput.setObjectName("FinalOutput")
        self.SubmitButton = QtWidgets.QPushButton(Dialog)
        self.SubmitButton.setGeometry(QtCore.QRect(300, 30, 61, 26))
        self.SubmitButton.setObjectName("SubmitButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 121, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SubmitButton.setText(_translate("Dialog", "Submit"))
        self.label_2.setText(_translate("Dialog", "Enter your Name: "))
