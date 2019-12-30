# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'country_choose.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 67)
        self.countrylineedit = QtWidgets.QLineEdit(Dialog)
        self.countrylineedit.setGeometry(QtCore.QRect(80, 20, 151, 25))
        self.countrylineedit.setReadOnly(True)
        self.countrylineedit.setObjectName("countrylineedit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label.setObjectName("label")
        self.choosepushbutton = QtWidgets.QPushButton(Dialog)
        self.choosepushbutton.setGeometry(QtCore.QRect(240, 20, 80, 26))
        self.choosepushbutton.setObjectName("choosepushbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Country: "))
        self.choosepushbutton.setText(_translate("Dialog", "Choose"))
