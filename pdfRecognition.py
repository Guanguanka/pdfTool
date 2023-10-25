import cv2
import numpy as np
from pyzbar.pyzbar import decode

class pdfRecognition():
    def __init__(self,filePath,folderPath):
        self.filePath = filePath
        self.folderPath = folderPath

    def BarodeIdentification(self):
        try:
            img = cv2.imread(self.filePath)
            barcodes = decode(img)
            return barcodes[0].data.decode()[-12:]
        except:
            print("Barcode parsing exception...")

