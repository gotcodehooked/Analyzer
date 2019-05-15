from abc import ABC, abstractmethod


class DataMiner(ABC):
    __path = ""

    @property
    def getpath(self):
        return self.__path

    @getpath.setter
    def getpath(self, value):
        self.__path = value

    @abstractmethod
    def sendReport(self):
        print("Have realise")

    @abstractmethod
    def parseData(self):
        pass

    @abstractmethod
    def analyzeData(self):
        pass
