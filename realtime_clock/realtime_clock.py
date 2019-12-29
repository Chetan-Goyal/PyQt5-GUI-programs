# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'realtime_clock.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(240, 171)
        self.clock = QtWidgets.QLCDNumber(Dialog)
        self.clock.setGeometry(QtCore.QRect(50, 50, 141, 71))
        self.clock.setDigitCount(8)
        self.clock.setObjectName("clock")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
