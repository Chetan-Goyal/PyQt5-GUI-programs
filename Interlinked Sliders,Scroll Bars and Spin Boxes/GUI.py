# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 213)
        self.SB = QtWidgets.QSpinBox(Dialog)
        self.SB.setGeometry(QtCore.QRect(30, 10, 54, 25))
        self.SB.setObjectName("SB")
        self.HS = QtWidgets.QSlider(Dialog)
        self.HS.setGeometry(QtCore.QRect(20, 70, 160, 16))
        self.HS.setOrientation(QtCore.Qt.Horizontal)
        self.HS.setObjectName("HS")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 140, 230, 20))
        self.label.setObjectName("label")
        self.VS = QtWidgets.QSlider(Dialog)
        self.VS.setGeometry(QtCore.QRect(300, 20, 16, 160))
        self.VS.setOrientation(QtCore.Qt.Vertical)
        self.VS.setObjectName("VS")
        self.HSB = QtWidgets.QScrollBar(Dialog)
        self.HSB.setGeometry(QtCore.QRect(20, 120, 160, 16))
        self.HSB.setOrientation(QtCore.Qt.Horizontal)
        self.HSB.setObjectName("HSB")
        self.VSB = QtWidgets.QScrollBar(Dialog)
        self.VSB.setGeometry(QtCore.QRect(260, 20, 16, 160))
        self.VSB.setOrientation(QtCore.Qt.Vertical)
        self.VSB.setObjectName("VSB")
        self.DSB = QtWidgets.QDoubleSpinBox(Dialog)
        self.DSB.setGeometry(QtCore.QRect(150, 10, 62, 25))
        self.DSB.setObjectName("DSB")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 70, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 130, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 190, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 180, 30, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 180, 40, 15))
        self.label_6.setObjectName("label_6")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(40, 180, 111, 21))
        self.Result.setText("")
        self.Result.setObjectName("Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "HORIZONTAL SCROLL BAR (HSB)"))
        self.label_2.setText(_translate("Dialog", "SPIN BOX"))
        self.label_3.setText(_translate("Dialog", "DOUBLE SPIN BOX"))
        self.label_4.setText(_translate("Dialog", "HORIZONTAL SLIDER (HS)"))
        self.label_5.setText(_translate("Dialog", "VSB"))
        self.label_6.setText(_translate("Dialog", "VS"))
