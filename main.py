from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit, QGridLayout, QLabel
from module.ContentAnalisys import LSI, unicode
from DocxCreator import DocxCreator
from main_gui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.k = 0
        self.saveDirPath = ""
        #  Хранение объектов Qt
        self.hlItems = []
        self.labelItems = []
        self.editItems = []
        self.keywordsItems = []
        self.editTextNameArticle = []

        # Данные с полей
        self.articles = []
        self.nameArticles = []
        self.keywordsArticle = []

        self.lineEditOpenFile.returnPressed.connect(self.setSaveFileDirectory)
        self.toolButton.clicked.connect(self.setSaveFileDirectory)
        self.addArticle.clicked.connect(lambda: self.addArticles(self.spinArticleBox.text()))
        self.removeArticle.clicked.connect(lambda: self.delArticles(self.spinBox.text()))
        # self.cancelAnalyzeButton.clicked.connect(self.getArticlesInfo)
        self.startAnalyzeButton.clicked.connect(lambda: self.btnstate())

    def setSaveFileDirectory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.saveDirPath = QFileDialog.getSaveFileName(options=options)[0]
        self.lineEditOpenFile.setText(self.saveDirPath)

    def startAnalyzing(self):
        self.buildArticlesInfo()
        # self.keywordsArticle.
        self.getKeyWordList()
        lsi = LSI(["в", "и", "о", "для", "еще", "не"], self.articles)
        lsi.hyphenProcessing(self.articles[0])
        wdict = lsi.wdict

        document = DocxCreator()
        document.addDataInDocx(self.saveDirPath, self.articles, self.nameArticles, self.keywordsArticle, wdict)

    def btnstate(self):

        if self.startAnalyzeButton.isChecked():
            self.startAnalyzing()
            self.startAnalyzeButton.toggle()
        else:
            pass

    def getKeyWordList(self):
        keywordList = []
        for article in range(len(self.keywordsArticle)):
            for word in self.keywordsArticle[article].split(','):
                keywordList.append(LSI.processingIgnoreChars(self, word))

        return keywordList

    def addArticles(self, number):

        for i in range(int(number)):
            self.k += 1
            element = QGridLayout()
            element.setSpacing(10)

            label = QLabel("Статья: " + str(len(self.labelItems) + 1))

            editText = QTextEdit()
            editTextNameArticle = QTextEdit()
            editTextKeyWords = QTextEdit()

            editTextKeyWords.setFixedHeight(60)
            editTextNameArticle.setFixedHeight(50)

            editTextNameArticle.setPlaceholderText("Название статьи")
            editTextKeyWords.setPlaceholderText("Ключевые слова")
            editText.setPlaceholderText("Введите статью")

            element.addWidget(label, 0, 1)
            element.addWidget(editTextNameArticle, 1, 1)
            element.addWidget(editText, 2, 1)
            element.addWidget(editTextKeyWords, 3, 1)

            self.keywordsItems.append(editTextKeyWords)
            self.hlItems.append(element)
            self.labelItems.append(label)
            self.editTextNameArticle.append(editTextNameArticle)
            self.editItems.append(editText)

            self.verticalLayout_2.addLayout(element)

            self.numberArticlesLabel.setText(str(len(self.hlItems)))

    def delArticles(self, count):
        ct = int(count)
        if ct < len(self.hlItems) or ct == len(self.hlItems):
            for i in range(len(self.hlItems) - ct, len(self.hlItems)):
                self.hlItems[i].setParent(None)
                self.labelItems[i].setParent(None)
                self.editItems[i].setParent(None)
                self.editTextNameArticle[i].setParent(None)
                self.keywordsItems[i].setParent(None)

            for i in range(ct):
                del self.hlItems[-1]
                del self.labelItems[-1]
                del self.editItems[-1]
                del self.editTextNameArticle[-1]
                del self.keywordsItems[-1]
        else:
            pass

        self.numberArticlesLabel.setText(str(len(self.hlItems)))

    def buildArticlesInfo(self):
        for i in range(len(self.hlItems)):
            self.nameArticles.append(self.editTextNameArticle[i].toPlainText())
            self.articles.append(self.editItems[i].toPlainText())
            self.keywordsArticle.append(self.keywordsItems[i].toPlainText())


def main():
    import sys
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
