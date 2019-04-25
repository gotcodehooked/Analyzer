import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog, QAction, QDialog
from PyQt5.uic.properties import QtCore, QtGui

from main_gui import Ui_MainWindow
from PyQt5 import QtCore, uic
from PyQt5.QtCore import QCoreApplication, QObject, Qt, pyqtSignal

from module.PDFDataMIner import PDFDataMiner
from PyQt5 import QtWidgets


# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.openFileNameDialog)
        self.buttonBox.accepted.connect(self.startAnayzer)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        object = PDFDataMiner
        print(id(object))
        options |= QFileDialog.DontUseNativeDialog
        filename = QFileDialog.getOpenFileName(options=options)[0]
        object.getpath = filename
        # object.extract_text(object())


    def startAnayzer(self):
        print("start Analyze")
        PDFDataMiner.extract_text(PDFDataMiner())

    def keyPressEvent(self, e):
        if self.lineEditOpenFile.text() != '':
            if e.key() == Qt.Key_Return:
                 if self.lineEditOpenFile.text().endswith(".pdf"):
                     PDFDataMiner.getpath = self.lineEditOpenFile.text()
                     print(PDFDataMiner.getpath)
                # filename = pdfData.getpath = pdfData.openFile(self)
                #
                # self.lineEditOpenFile.setText(pdfData.getpath)




            else:
                errorDialog = QtWidgets.QErrorMessage()
                errorDialog.showMessage('Oh no!')

        else:
            isEmptyLineMessage = QtWidgets.QMessageBox()
            isEmptyLineMessage.show()
            print("sfsf")

    def returnObjectPDF(self):
        return PDFDataMiner

    def returnObjectPDFo(self):
        return PDFDataMiner()

    def file_open(self):
        dialog = QFileDialog.getOpenFileName()[0]
        PDFDataMiner.getpath = dialog

    def progressBar(self):
        self.statusProgressBar.setValue(self.returnObjectPDFo().getcount)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
