# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.emailLineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.emailLineEdit.setGeometry(QtCore.QRect(90, 10, 231, 25))
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.passwordLineEdit.setGeometry(QtCore.QRect(90, 60, 231, 25))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 15, 57, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 71, 31))
        self.label_2.setObjectName("label_2")
        self.loginPushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.loginPushButton.setGeometry(QtCore.QRect(40, 110, 80, 26))
        self.loginPushButton.setObjectName("loginPushButton")
        self.resultLabel = QtWidgets.QLabel(self.dockWidgetContents)
        self.resultLabel.setGeometry(QtCore.QRect(50, 160, 271, 41))
        self.resultLabel.setText("")
        self.resultLabel.setObjectName("resultLabel")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Dockable Sign In Form"))
        self.label.setText(_translate("MainWindow", "Email:"))
        self.label_2.setText(_translate("MainWindow", "Password: "))
        self.loginPushButton.setText(_translate("MainWindow", "Sign in"))
