import cv2 as cv
import numpy as np
import pytesseract
import random
import sys

sys.path.append("/Users/cassini/Desktop/PyVision-main/src/tessexc")
sys.path.append("/Users/cassini/Desktop/PyVision-main/src/OCR")

import text_extraction

#Set pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'/Usr/local/bin/tesseract'

images = [r"/Users/cassini/Downloads/stop1.png", r"/Users/cassini/Downloads/stop3.jpeg", r"/Users/cassini/Downloads/stop2.jpeg",
          r"/Users/cassini/Downloads/stop5.jpeg", r"/Users/cassini/Downloads/stop7.jpeg", r"/Users/cassini/Downloads/stop6.webp"]

#initialize camera 
def extractText(mask):
    if 5 >= len(text_extraction.extractText(mask)) >= 2:
        return True
    
    return False 
