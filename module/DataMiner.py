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




    @abstractmethod
    def sendReport(self):
        print("Have realise")

    @abstractmethod
    def parseData(self, path):
        pass

    @abstractmethod
    def analyzeData(self):
        pass
