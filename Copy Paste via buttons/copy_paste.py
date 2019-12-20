# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copy_paste.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 312)
        self.Input = QtWidgets.QLineEdit(Dialog)
        self.Input.setGeometry(QtCore.QRect(10, 10, 491, 51))
        self.Input.setObjectName("Input")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 70, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.Output = QtWidgets.QLineEdit(Dialog)
        self.Output.setGeometry(QtCore.QRect(10, 190, 491, 111))
        self.Output.setObjectName("Output")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 150, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.pressed.connect(self.Input.selectAll)
        self.pushButton.released.connect(self.Input.copy)
        self.pushButton_2.clicked.connect(self.Output.paste)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Copy"))
        self.pushButton_2.setText(_translate("Dialog", "Paste"))
