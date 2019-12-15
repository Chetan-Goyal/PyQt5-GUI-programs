# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'age_group.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 218)
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(40, 30, 271, 21))
        self.Title.setObjectName("Title")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(80, 160, 211, 31))
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.kid = QtWidgets.QRadioButton(Dialog)
        self.kid.setGeometry(QtCore.QRect(70, 80, 211, 16))
        self.kid.setObjectName("kid")
        self.adult = QtWidgets.QRadioButton(Dialog)
        self.adult.setGeometry(QtCore.QRect(70, 120, 211, 16))
        self.adult.setObjectName("adult")
        self.teenager = QtWidgets.QRadioButton(Dialog)
        self.teenager.setGeometry(QtCore.QRect(70, 100, 211, 16))
        self.teenager.setObjectName("teenager")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Title.setText(_translate("Dialog", "Please choose your age group"))
        self.kid.setText(_translate("Dialog", "<13 Years "))
        self.adult.setText(_translate("Dialog", ">18 Years"))
        self.teenager.setText(_translate("Dialog", "13-18 Years"))
