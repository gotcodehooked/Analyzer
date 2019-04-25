# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditOpenFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditOpenFile.setGeometry(QtCore.QRect(20, 40, 380, 25))
        self.lineEditOpenFile.setObjectName("lineEditOpenFile")
        self.lineEditOpenFile.setMaxLength(100)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 130, 15))
        self.label.setObjectName("label")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(100, 100, 200, 400)
        self.labelResult.setObjectName("Result")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(410, 40, 30, 25))
        self.toolButton.setCheckable(False)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setToolTip('Выберите файл')
        self.statusProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.statusProgressBar.setGeometry(QtCore.QRect(20, 460, 410, 25))
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.statusProgressBar.setTextVisible(True)
        self.statusProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.statusProgressBar.setInvertedAppearance(False)
        self.statusProgressBar.setFormat("")
        self.statusProgressBar.setObjectName("statusProgressBar")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(260, 510, 169, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        openFile = QtWidgets.QAction(QIcon(), 'Open', MainWindow)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.file_open)
        filemenu = self.menubar.addMenu("Файл")
        filemenu.addAction(openFile)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Папка назначения"))
        self.labelResult.setText(_translate("MainWindow", "Result"))
        self.toolButton.setText(_translate("MainWindow", "..."))

    # def file_open(self):
    #     fname = QFileDialog.getOpenFileName()[0]
    #
    #     f = open(fname, 'r')
    #
    #     with f:
    #         data = f.name
    #         self.lineEditOpenFile.setText(str(data))
