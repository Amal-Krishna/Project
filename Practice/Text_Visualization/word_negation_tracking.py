#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:24:41 2019

@author: amalk
"""

import nltk

from nltk.corpus import wordnet

sentence = """I did not cry or yell or lie down on the pine floorboards and kick my feet.At no time did I feel threatened or in danger of violence. At no time did I feel inclined to regard any of my colleagues as lazy or inept—or feel they were insinuating similar judgments about me.There are no apples in the basket. He is not interested in the project. There was no car on the road.Cats do not like swimming.No man is totally perfect. My guests are not arriving now. Jennie has no money."""


words = nltk.word_tokenize(sentence)

new_word = []

temp_word = ""

for word in words:
    antonyms = []
    if word == "not":
        temp_word = "not_"
    elif temp_word == "not_":
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
        if len(antonyms) >= 1:
            word = antonyms[0]
        else:
            word = temp_word + word
        temp_word = ""
    if word != "not":
        new_word.append(word)
        
sentence = ' '.join(new_word)

print(sentence)