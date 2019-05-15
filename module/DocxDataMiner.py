from module.DataMiner import DataMiner
import docx


class DocxDataMiner(DataMiner):


    def parseData(self):

        if str(self.getpath).endswith(".docx"):
            document = docx.Document(self.getpath)

            for i in range(len(document.paragraphs)):
                if document.paragraphs[i].text in "Ключевые":
                    print(document.paragraphs[i - 1].text)
        else:
            print("Error")

    def analyzeData(self):
        pass

    def sendReport(self):
        pass
