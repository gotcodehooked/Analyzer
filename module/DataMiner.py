from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QFileDialog


class DataMiner(ABC):
    _path = ""



    @property
    def getpath(self):
        return self._path

    @getpath.setter
    def getpath(self, value):
        self._path = value


    def returnPath(self, path):
        return path

    def extractData(self, path):
        file = open(path, 'r')
        with file:
            print("Data load")
            data = file.read()

        return data

    def openFile(self):
        dialog = QFileDialog()
        if dialog.exec_() == QFileDialog.Accepted:
            print("True")
            path = dialog.selectedFiles()[0]
            return path



    def sendReport(self):
        print("Have realise")

    # def closeFile(self):
    #     closeFile(self)
    #     print("Have realsie")

    def mine(self):
        print("saf")
        self.openFile()
        # self.extractData()
        # self.parseData()
        # self.analyzeData()
        # self.sendReport()
        # self.closeFile()

    @abstractmethod
    def parseData(self):
        pass

    @abstractmethod
    def analyzeData(self):
        pass
