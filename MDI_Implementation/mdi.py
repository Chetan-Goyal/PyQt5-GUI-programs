# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdi.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 216)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 621, 171))
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow = QtWidgets.QWidget()
        self.subwindow.setObjectName("subwindow")
        self.label = QtWidgets.QLabel(self.subwindow)
        self.label.setGeometry(QtCore.QRect(100, 50, 57, 15))
        self.label.setObjectName("label")
        self.subwindow_2 = QtWidgets.QWidget()
        self.subwindow_2.setObjectName("subwindow_2")
        self.label_2 = QtWidgets.QLabel(self.subwindow_2)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 57, 15))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 23))
        self.menubar.setObjectName("menubar")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Sub_Window_View = QtWidgets.QAction(MainWindow)
        self.Sub_Window_View.setObjectName("Sub_Window_View")
        self.Tabbed_View = QtWidgets.QAction(MainWindow)
        self.Tabbed_View.setObjectName("Tabbed_View")
        self.Cascade_View = QtWidgets.QAction(MainWindow)
        self.Cascade_View.setObjectName("Cascade_View")
        self.Tile_View = QtWidgets.QAction(MainWindow)
        self.Tile_View.setObjectName("Tile_View")
        self.menuWindow.addAction(self.Sub_Window_View)
        self.menuWindow.addAction(self.Tabbed_View)
        self.menuWindow.addAction(self.Cascade_View)
        self.menuWindow.addAction(self.Tile_View)
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label.setText(_translate("MainWindow", "1"))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.Sub_Window_View.setText(_translate("MainWindow", "Sub Window View"))
        self.Tabbed_View.setText(_translate("MainWindow", "Tabbed View"))
        self.Cascade_View.setText(_translate("MainWindow", "Cascade View"))
        self.Tile_View.setText(_translate("MainWindow", "Tile View"))
