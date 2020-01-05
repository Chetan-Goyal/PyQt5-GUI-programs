# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawing_shapes.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 300, 371, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 23))
        self.menubar.setObjectName("menubar")
        self.menuShape = QtWidgets.QMenu(self.menubar)
        self.menuShape.setObjectName("menuShape")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCircle = QtWidgets.QAction(MainWindow)
        self.actionCircle.setObjectName("actionCircle")
        self.actionRectangle = QtWidgets.QAction(MainWindow)
        self.actionRectangle.setObjectName("actionRectangle")
        self.actionLine = QtWidgets.QAction(MainWindow)
        self.actionLine.setObjectName("actionLine")
        self.actionPage_Setup = QtWidgets.QAction(MainWindow)
        self.actionPage_Setup.setObjectName("actionPage_Setup")
        self.actionPassword = QtWidgets.QAction(MainWindow)
        self.actionPassword.setObjectName("actionPassword")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuShape.addAction(self.actionCircle)
        self.menuShape.addAction(self.actionRectangle)
        self.menuShape.addAction(self.actionLine)
        self.menuOptions.addAction(self.actionPage_Setup)
        self.menuOptions.addAction(self.actionPassword)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuShape.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuShape.setTitle(_translate("MainWindow", "Shape"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCircle.setText(_translate("MainWindow", "Circle"))
        self.actionCircle.setShortcut(_translate("MainWindow", "Shift+C"))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle"))
        self.actionRectangle.setShortcut(_translate("MainWindow", "Shift+R"))
        self.actionLine.setText(_translate("MainWindow", "Line"))
        self.actionLine.setShortcut(_translate("MainWindow", "Shift+L"))
        self.actionPage_Setup.setText(_translate("MainWindow", "Page Setup"))
        self.actionPage_Setup.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPassword.setText(_translate("MainWindow", "Password"))
        self.actionPassword.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
