# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_data.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 470)
        font = QtGui.QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(20, 360, 351, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        self.Result.setFont(font)
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Submit = QtWidgets.QPushButton(Dialog)
        self.Submit.setGeometry(QtCore.QRect(410, 30, 71, 21))
        self.Submit.setObjectName("Submit")
        self.Name = QtWidgets.QLineEdit(Dialog)
        self.Name.setGeometry(QtCore.QRect(200, 30, 201, 21))
        self.Name.setObjectName("Name")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 110, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Male = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Male.setAutoRepeat(False)
        self.Male.setObjectName("Male")
        self.verticalLayout_2.addWidget(self.Male)
        self.Female = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Female.setObjectName("Female")
        self.verticalLayout_2.addWidget(self.Female)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 250, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.kid = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.kid.setObjectName("kid")
        self.verticalLayout_3.addWidget(self.kid)
        self.teenager = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.teenager.setObjectName("teenager")
        self.verticalLayout_3.addWidget(self.teenager)
        self.adult = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.adult.setObjectName("adult")
        self.verticalLayout_3.addWidget(self.adult)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose your Gender"))
        self.label_2.setText(_translate("Dialog", "Choose your Age Group"))
        self.label_4.setText(_translate("Dialog", "Enter your name: "))
        self.Submit.setText(_translate("Dialog", "Submit"))
        self.Male.setText(_translate("Dialog", "Male"))
        self.Female.setText(_translate("Dialog", "Female"))
        self.kid.setText(_translate("Dialog", "<12 Years"))
        self.teenager.setText(_translate("Dialog", "12 to 18 Years"))
        self.adult.setText(_translate("Dialog", ">18 Years"))
