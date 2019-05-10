from module.DataMiner import DataMiner

import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PDFDataMiner(DataMiner):

    @classmethod
    def analyzeData(cls):
        fileName = cls.getpath
        pageGenerator = cls.parseData(fileName)

        pageList = [pageList for pageList in pageGenerator]

        return pageList[0]

    @classmethod
    def parseData(cls, pdf_path):
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
