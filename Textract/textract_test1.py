# -*- coding: utf-8 -*-

import textract

text = textract.process('/home/amalk/Desktop/Project/Textract/three_mistakes_of_my_life.pdf', method='pdfminer')

print(text) 



