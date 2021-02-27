# This script reads in a pdf file and then either pulls the
# text directly from the pdf or applies OCR to it in order 
# to return the text that the document contains. This is useful
# when trying to do searches for specific strings or putting a document
# into word or other scenarios
#
# in addition to the normal pip3 installations of
#   wand
#   pdfplumber 
#   pytesseract
# 
# this requires the following libraries be installed 
#   https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows
#   https://github.com/UB-Mannheim/tesseract/wiki


from PIL import Image 
import pytesseract 
import sys 
import os
import pdfplumber

pdf_file = "source.pdf"
txt_file = "target.txt"
tempLoc = "tempPages/"
pageName = "page"
doc = ''

pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

with pdfplumber.open(pdf_file) as pdf:
    with open (txt_file, "w", encoding="utf-8") as outFile :
        for page in pdf.pages :
            # best way to get text is if the doc has the text component
            # already encoded (this only occurs if it was not scanned)
            doc = page.extract_text()
            # if we can't get the text the easy way, try the best we
            # can using OCR extraction of the text 
            if (not doc) :
                im = page.to_image(resolution=512)
                filename = tempLoc+pageName+".png"
                im.save(filename, format="PNG")
                doc = str(((pytesseract.image_to_string(Image.open(filename)))))
            outFile.write (doc) 


