# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csv-reader_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("padmaa-Bold.1.1")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(60, 80, 256, 192))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Data"))
