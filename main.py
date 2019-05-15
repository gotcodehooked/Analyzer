from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from main_gui import Ui_MainWindow

from module import DataMiner
from module.DocxDataMiner import DocxDataMiner
from module.PDFDataMIner import PDFDataMiner


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.path = ""
        self.lineEditOpenFile.returnPressed.connect(self.openFileNameDialog)
        self.toolButton.pressed.connect(self.openFileNameDialog)
        self.startAnalyzeButton.clicked.connect(lambda: self.startAnalyzing(self.fileTypeDetection()))
        self.cancelAnalyzeButton.pressed.connect(self.cancelAnalysis)

    def fileTypeDetection(self):
        if self.path.endswith(".pdf"):
            print("PDF")
            return PDFDataMiner()
        elif self.path.endswith(".docx"):
            print("DOCX")
            return DocxDataMiner()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.path = QFileDialog.getOpenFileName(options=options)[0]
        self.lineEditOpenFile.setText(self.path)

    def startAnalyzing(self, dataMiner: DataMiner):
        print("start Analyze")
        dataMiner.getpath = self.path
        dataMiner.analyzeData()


    def getInstance(self):
        pass

    def cancelAnalysis(self):
        return self.startAnalyzeButton.disconnect()


def main():
    import sys
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
