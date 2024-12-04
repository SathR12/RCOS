# Works on MAC Only for now
# Coding on MACBOOK AIR and transferring over to work on windows 

import cv2 as cv
import numpy as np
import pytesseract
import sys

sys.path.append("/Users/cassini/Desktop/PyVision-main/src/tessexc")
sys.path.append("/Users/cassini/Desktop/PyVision-main/src/OCR")

import text_extraction

#Set pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'/Usr/local/bin/tesseract'

#initialize camera 
camera = cv.VideoCapture(0)

def extractText(mask):
    if 5 >= len(text_extraction.extractText(mask)) >= 2:
        return True
    
    return False 

def isOctagon(contour):
    edges = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    
    if 9 >= len(edges) >= 8:
        return True
    
    return False
