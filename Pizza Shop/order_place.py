# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_place.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 90, 160, 124))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.EC = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.EC.setFont(font)
        self.EC.setObjectName("EC")
        self.verticalLayout.addWidget(self.EC)
        self.TB = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TB.setFont(font)
        self.TB.setObjectName("TB")
        self.verticalLayout.addWidget(self.TB)
        self.CLC = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.CLC.setFont(font)
        self.CLC.setObjectName("CLC")
        self.verticalLayout.addWidget(self.CLC)
        self.HTB = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.HTB.setFont(font)
        self.HTB.setObjectName("HTB")
        self.verticalLayout.addWidget(self.HTB)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 31))
        self.label.setMinimumSize(QtCore.QSize(211, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 160, 92))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.regular = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.regular.setObjectName("regular")
        self.verticalLayout_2.addWidget(self.regular)
        self.medium = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.medium.setObjectName("medium")
        self.verticalLayout_2.addWidget(self.medium)
        self.large = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.large.setObjectName("large")
        self.verticalLayout_2.addWidget(self.large)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(30, 250, 321, 31))
        self.Result.setText("")
        self.Result.setObjectName("Result")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.EC.setText(_translate("Dialog", "Extra Cheese          $ 0.99"))
        self.TB.setText(_translate("Dialog", "Toppings Blast      $ 1.49"))
        self.CLC.setText(_translate("Dialog", "Choco Lava Cake  $ 2.99"))
        self.HTB.setText(_translate("Dialog", "Hand-tossed Base $ 0.49"))
        self.label.setText(_translate("Dialog", "Order Placing Form"))
        self.regular.setText(_translate("Dialog", "Regular   $ 3.99"))
        self.medium.setText(_translate("Dialog", "Medium  $ 6.99"))
        self.large.setText(_translate("Dialog", "Large       $ 8.49"))
        self.label_2.setText(_translate("Dialog", "PIZZA"))
        self.label_3.setText(_translate("Dialog", "Add-ons"))