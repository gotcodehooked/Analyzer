from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit, QHBoxLayout, QPushButton, QLabel, \
    QLineEdit
from main_gui import Ui_MainWindow
from PyQt5 import QtCore
from module import DataMiner
from module.DocxDataMiner import DocxDataMiner
from module.PDFDataMIner import PDFDataMiner


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.k = 0
        self.path = ""
        self.hlItems = []
        self.labelItems = []
        self.editItems = []
        self.articles = []
        self.cancelAnalyzeButton.clicked.connect(self.getArticles)
        self.saveDirPath = ""
        self.lineEditOpenFile.returnPressed.connect(self.setPathFromLineEdit)
        self.toolButton.clicked.connect(self.setFilePath)
        self.addArticle.clicked.connect(lambda: self.addArticles(self.spinArticleBox.text()))
        self.removeArticle.clicked.connect(lambda: self.delArticles(self.spinBox.text()))
        self.startAnalyzeButton.clicked.connect(lambda: self.btnstate(self.getInstance()))

    def getInstance(self):
        if self.path.endswith(".pdf"):
            print("pdf")
            return PDFDataMiner(self.path)
        elif self.path.endswith(".docx"):
            print("docx")
            return DocxDataMiner(self.path)

    def setPathFromLineEdit(self):
        if self.lineEditOpenFile.text().endswith(".pdf"):
            self.path = self.lineEditOpenFile.text()

        elif self.lineEditOpenFile.text().endswith(".docx"):
            self.path = self.lineEditOpenFile.text()

        else:
            self.setFilePath()

    def setFilePath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.path = QFileDialog.getOpenFileName(options=options)[0]
        self.lineEditOpenFile.setText(self.path)

    def setSaveFileDirectory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.saveDirPath = QFileDialog.getSaveFileName(options=options)[0]
        print(self.saveDirPath)

    def startAnalyzing(self, dataMiner: DataMiner):
        return dataMiner.convertToJSON()

    def cancelAnalysis(self):
        return self.startAnalyzeButton.pressed.disconnect()

    def btnstate(self, dataMiner: DataMiner):

        if self.startAnalyzeButton.isChecked():
            self.startAnalyzing(dataMiner)
            self.startAnalyzeButton.toggle()
        else:
            pass

    def addArticles(self, number):

        for i in range(int(number)):
            self.k += 1
            element = QHBoxLayout()
            label = QLabel(str(len(self.labelItems)+1))
            editText = QTextEdit()
            element.addWidget(label)
            element.addWidget(editText)
            self.hlItems.append(element)
            self.labelItems.append(label)
            self.editItems.append(editText)
            self.verticalLayout_2.addLayout(element)
            self.numberArticlesLabel.setText(str(len(self.hlItems)))

    def getArticles(self):
        print("dasdas")
        for i in range(len(self.hlItems)):
            self.articles.append(self.editItems[i].toPlainText())

        print(self.articles)

    def removeArticleList(self):
        pass


    def delArticles(self, count):
        ct = int(count)

        if ct < len(self.hlItems) or ct == len(self.hlItems):
            for i in range(len(self.hlItems) - ct, len(self.hlItems)):

                self.hlItems[i].setParent(None)
                self.labelItems[i].setParent(None)
                self.editItems[i].setParent(None)

            for i in range(ct):
                del self.hlItems[-1]
                del self.labelItems[-1]
                del self.editItems[-1]

        else:
            pass

        self.numberArticlesLabel.setText(str(len(self.hlItems)))


def main():
    import sys
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
