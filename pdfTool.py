from pdfSplitting import pdfSplitting
from pdfToPic import pdfToPic
import os
import sys

def main(filepath,folderPath):
    print("Loading pdf file...")
    print("Spliting pdf file...")

    try:
        pdf = pdfSplitting(filepath,folderPath)
        pdf.splitting();
    except:
        print("PDF splitting exception...")

    try:
        pdfOpreation = pdfToPic(filepath,folderPath)
        pdfOpreation.pdfToPic()
    except:
        print("PDF conversion exception...")

    print("Successfully parsed PDF tracking number!!")

if __name__ == '__main__':
    print("Please enter the PDF path or drag the file in, and then press enter to continue:")
    filepath = str(sys.stdin.readline().strip())
    folderPath= os.path.dirname(filepath) + "/pdfFolder";
    main(filepath,folderPath);
