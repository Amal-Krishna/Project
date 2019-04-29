#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:11:00 2019

@author: amalk
"""

import nltk
import re

IN = re.compile(r'.*\bin\b(?!\b.+ing)')

for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,corpus='ieer', pattern = IN):
        print(nltk.sem.relextract.rtuple(rel))
        
        

for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('PER', 'LOC', doc,corpus='ieer', pattern = IN):
        print(nltk.sem.relextract.rtuple(rel))        
        
        
PARENT = re.compile(r'.*\bfriend\b')

for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('PER', 'PER', doc,corpus='ieer', pattern = PARENT):
        print(nltk.sem.relextract.rtuple(rel))


WORKS = re.compile(r'.*\bworked\b')



WORKS = re.compile(r'.*\bfor\b')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('PER', 'ORG', doc,corpus='ieer', pattern = WORKS):
        print(nltk.sem.relextract.rtuple(rel))



nltk.corpus.gutenberg.fileids()


from nltk.corpus import gutenberg

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')

macbeth_sentences

for s in macbeth_sentences:
    print(s)
    



IN = re.compile(r'.*\bin\b(?!\b.+ing)')

#tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in macbeth_sentences]
#tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]




import nltk
import re
from nltk.sem import extract_rels,rtuple

with open('shakespeare-macbeth.txt', 'r') as f:
    sample = f.read()
    
sample = sample.replace('\n', ' ').replace('\r', '')

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

OF = re.compile(r'.*\bof\b.*')

for i, sent in enumerate(tagged_sentences):
    sent = nltk.ne_chunk(sent)
    rels = extract_rels('PER', 'ORG', sent, pattern=OF)
    for rel in rels:
        print('{0:<5}{1}'.format(i, rtuple(rel)))














