from module.DataMiner import DataMiner

import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PDFDataMiner(DataMiner):

    def analyzeData(self):
        pageGenerator = self.parseData()
        pageList = [pageList for pageList in pageGenerator]
        for i in pageList:
            print(i)

    def parseData(self):
        with open(self.getpath, 'rb') as fh:
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

    def sendReport(self):
        pass
