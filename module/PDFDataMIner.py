from module.DataMiner import DataMiner
from fitz import *
import json


class PDFDataMiner(DataMiner):

    def __init__(self, path):
        super().__init__(path)

    def analyzeData(self):
        pass

    def parseData(self):
        doc = fitz.open(self.getpath)

        if doc.isPDF:

            pageList = [page for page in doc]
            data = [page.getText('json') for page in pageList]

            doc.close()
            return data
        else:
            doc.close()


    def convertToJSON(self):

        pageList = self.parseData()

        convertResult = [json.loads(page) for page in pageList]

        print(convertResult[20]['blocks'][1]['lines'])
        # result = json.loads(pageList)
        lst = []

        # for i in range(10):
        # lst = result['blocks'][5]['lines'][0]['spans'][1]['text']



    def sendReport(self):
        pass
