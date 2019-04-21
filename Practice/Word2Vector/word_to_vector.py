#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:39:15 2019

@author: amalk
"""

import nltk
import re
import urllib
from nltk.corpus import stopwords
import bs4 as bs
from gensim.models import Word2Vec 

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Avengers:_Infinity_War').read()

soup = bs.BeautifulSoup(source,'lxml')

text = ""

for paragraph in soup.find_all('p'):
    text += paragraph.text
    
    

text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
#text = re.sub(r'\W',' ',text)
text = re.sub(r'[@#$%^&*\(\)\\<\>\?\'\";:\[\]\-\/]',' ',text)
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]


model = Word2Vec(sentences,min_count=1)

words = model.wv.vocab

vector = model.wv['avengers']

similar = model.wv.most_similar('gauntlet')










