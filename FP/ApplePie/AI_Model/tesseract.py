# This Python file uses the following encoding: utf-8
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os
import config

class OCR() :

    def __init__ (self, file_name) :
        # pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
        
        # 운영체제에 따라 다르게 설정
        # pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
        # self.path = IMAGE_PATH
        self.path = config.IMAGE_PATH
        self.file_name = file_name

    def ImgToText(self) :
        image = cv2.imread(self.path + self.file_name)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        text = pytesseract.image_to_string(rgb_image, lang='kor')

        return text