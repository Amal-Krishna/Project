#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:00:18 2019

@author: amalk
"""

from nltk.corpus import wordnet

synonyms = []
antonyms = []


for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
        
print(set(synonyms))
print(set(antonyms))