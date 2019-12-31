# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'font_choose.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 300)
        self.FontPushButton = QtWidgets.QPushButton(Dialog)
        self.FontPushButton.setGeometry(QtCore.QRect(150, 30, 91, 26))
        self.FontPushButton.setObjectName("FontPushButton")
        self.Fontlabel = QtWidgets.QLabel(Dialog)
        self.Fontlabel.setGeometry(QtCore.QRect(30, 80, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK JP")
        font.setPointSize(13)
        self.Fontlabel.setFont(font)
        self.Fontlabel.setText("")
        self.Fontlabel.setObjectName("Fontlabel")
        self.Resulttextedit = QtWidgets.QTextEdit(Dialog)
        self.Resulttextedit.setGeometry(QtCore.QRect(10, 130, 381, 161))
        self.Resulttextedit.setObjectName("Resulttextedit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.FontPushButton.setText(_translate("Dialog", "Choose Font"))
