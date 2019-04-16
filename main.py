import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileDialog, QAction
from main_gui import Ui_MainWindow
from PyQt5.QtCore import QCoreApplication
from module.openfiles import OpenParseFile as opf
import module.openfiles as openParse


# Создаём ещё один класс, наследуясь от класса со слотами
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.file_open)


    def file_open(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.name
            self.lineEditOpenFile.setText(str(data))


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
