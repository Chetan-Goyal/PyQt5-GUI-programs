# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'font_changer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 313)
        self.font = QtWidgets.QFontComboBox(Dialog)
        self.font.setGeometry(QtCore.QRect(180, 20, 176, 25))
        self.font.setObjectName("font")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Samanata")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.output = QtWidgets.QTextEdit(Dialog)
        self.output.setGeometry(QtCore.QRect(100, 130, 291, 161))
        self.output.setObjectName("output")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose a font:"))
        self.label_2.setText(_translate("Dialog", "Type some text:"))
