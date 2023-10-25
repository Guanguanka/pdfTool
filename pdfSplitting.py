from PyPDF2 import  PdfWriter, PdfReader
import os

class pdfSplitting(object):
    def __init__(self,filepath,folderPath):
        self.filepath = filepath
        self.folderPath = folderPath

    def splitting(self):
        file_reader = PdfReader(self.filepath, 'rb')
        if not os.path.exists(self.folderPath):
            os.makedirs(self.folderPath)

        for page in range(len(file_reader.pages)):
            file_writer = PdfWriter()
            file_writer.add_page(file_reader.pages[page])
            with open(self.folderPath + "/{}.pdf".format(page), 'wb') as out:
                file_writer.write(out)


