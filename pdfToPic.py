import os
from pdfRecognition import pdfRecognition
import fitz

class pdfToPic():
    def __init__(self,filepath,folderPath):
        self.filepath  = filepath
        self.folderPath = folderPath

    def pdfToPic(self):
        pdfDoc = fitz.open(self.filepath)
        for pg in range(pdfDoc.page_count):
            page = pdfDoc[pg]
            rotate = int(0)
            zoom_x = 1.33333333
            zoom_y = 1.33333333
            mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pix = page.get_pixmap(matrix=mat, alpha=False)

            if not os.path.exists(self.folderPath):
                os.makedirs(self.folderPath)

            fileName = self.folderPath + '/' + '%s.png' % pg

            pix.save(fileName)

            pdfNewName = pdfRecognition(fileName,self.folderPath).BarodeIdentification()

            os.rename(self.folderPath + '/' + '%s.pdf' % pg, self.folderPath + '/' + pdfNewName + ".pdf")

            os.remove(fileName)



