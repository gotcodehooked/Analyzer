from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed, PDFDocument

from module.DataMiner import DataMiner
import docx

import io
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from main_gui import Ui_MainWindow


class PDFDataMiner(DataMiner):
    _count = 0

    @property
    def getcount(self):
        return self._count

    @getcount.setter
    def getcount(self, value):
        self._count = value

    def pdfAnalyze(self, path):

        document = docx.Document(path)
        print(len(document.paragraphs))






    def parseData(self):

        pass

    def analyzeData(self):
        return "analyzeData"

    def extract_text_by_page(self, pdf_path):
        with open(pdf_path, 'rb') as fh:
            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                resource_manager = PDFResourceManager()
                fake_file_handle = io.StringIO()
                converter = TextConverter(resource_manager, fake_file_handle)
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(page)

                text = fake_file_handle.getvalue()

                yield text

                # close open handles
                converter.close()
                fake_file_handle.close()

    def extract_text(self):
        fileName = self.getpath
        pageGenerator = self.extract_text_by_page(fileName)
        pageList = [pageList for pageList in pageGenerator]
        for i in pageList[0]:
            print(i)
