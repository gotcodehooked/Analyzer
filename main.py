from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog, QAction, QDialog
from PyQt5.uic.properties import QtCore, QtGui

from main_gui import Ui_MainWindow

from PyQt5.QtCore import QCoreApplication, QObject, Qt, pyqtSignal

from module.PDFDataMIner import PDFDataMiner
from PyQt5 import QtWidgets


# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.openFileNameDialog)
        self.startAnalyzeButton.clicked.connect(self.startAnalyzing)
        # self.cancelAnalyzeButton.clicked.connect(PDFDataMiner.openFileNameDialog)


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        object = PDFDataMiner
        options |= QFileDialog.DontUseNativeDialog
        filename = QFileDialog.getOpenFileName(options=options)[0]
        object.getpath = filename
        self.lineEditOpenFile.setText(filename)


    def startAnalyzing(self):
        print("start Analyze")
        PDFDataMiner.analyzeData()



def main():
    import sys
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
