# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 223)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.label_2.setObjectName("label_2")
        self.num1 = QtWidgets.QLineEdit(Dialog)
        self.num1.setGeometry(QtCore.QRect(140, 30, 113, 25))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(Dialog)
        self.num2.setGeometry(QtCore.QRect(140, 70, 113, 25))
        self.num2.setObjectName("num2")
        self.plus = QtWidgets.QPushButton(Dialog)
        self.plus.setGeometry(QtCore.QRect(10, 130, 80, 26))
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(Dialog)
        self.minus.setGeometry(QtCore.QRect(100, 130, 80, 26))
        self.minus.setObjectName("minus")
        self.mul = QtWidgets.QPushButton(Dialog)
        self.mul.setGeometry(QtCore.QRect(190, 130, 80, 26))
        self.mul.setObjectName("mul")
        self.div = QtWidgets.QPushButton(Dialog)
        self.div.setGeometry(QtCore.QRect(280, 130, 80, 26))
        self.div.setObjectName("div")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(60, 190, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.Result.setFont(font)
        self.Result.setText("")
        self.Result.setObjectName("Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "First number   :"))
        self.label_2.setText(_translate("Dialog", "Second number :"))
        self.plus.setText(_translate("Dialog", "+"))
        self.minus.setText(_translate("Dialog", "-"))
        self.mul.setText(_translate("Dialog", "*"))
        self.div.setText(_translate("Dialog", "/"))
