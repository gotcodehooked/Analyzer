# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditOpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOpenFile.setGeometry(QtCore.QRect(20, 40, 370, 25))
        self.lineEditOpenFile.setObjectName("lineEditOpenFile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 130, 15))
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(400, 40, 30, 25))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName("toolButton")
        self.statusProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.statusProgressBar.setGeometry(QtCore.QRect(20, 460, 410, 25))
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusProgressBar.setTextVisible(True)
        self.statusProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.statusProgressBar.setInvertedAppearance(False)
        self.statusProgressBar.setFormat("")
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.startAnalyzeButton = QtWidgets.QPushButton(self.centralwidget)
        self.startAnalyzeButton.setGeometry(QtCore.QRect(350, 500, 80, 25))
        self.startAnalyzeButton.setObjectName("startAnalyzeButton")
        self.cancelAnalyzeButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelAnalyzeButton.setGeometry(QtCore.QRect(260, 500, 80, 25))
        self.cancelAnalyzeButton.setObjectName("cancelAnalyzeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Папка назначения"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.startAnalyzeButton.setText(_translate("MainWindow", "Анализ"))
        self.cancelAnalyzeButton.setText(_translate("MainWindow", "Отмена"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))


