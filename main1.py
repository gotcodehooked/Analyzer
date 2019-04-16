import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        openFile = QAction(QIcon(), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
