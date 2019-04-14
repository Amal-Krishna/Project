#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:43:16 2019

@author: amalk
"""


import random
import nltk

text = """ Global warming, the phenomenon of increasing average air temperatures near the surface of Earth over the past one to two centuries. Climate scientists have since the mid-20th century gathered detailed observations of various weather phenomena (such as temperatures, precipitation, and storms) and of related influences on climate (such as ocean currents and the atmosphere’s chemical composition). These data indicate that Earth’s climate has changed over almost every conceivable timescale since the beginning of geologic time and that the influence of human activities since at least the beginning of the Industrial Revolution has been deeply woven into the very fabric of climate change.Many climate scientists agree that significant societal, economic, and ecological damage would result if global average temperatures rose by more than 2 °C (3.6 °F) in such a short time. Such damage would include increased extinction of many plant and animal species, shifts in patterns of agriculture, and rising sea levels. By 2015 all but a few national governments had begun the process of instituting carbon reduction plans as part of the Paris Agreement, a treaty designed to help countries keep global warming to 1.5 °C (2.7 °F) above preindustrial levels in order to avoid the worst of the predicted effects. Authors of a special report published by the IPCC in 2018 noted that should carbon emissions continue at their present rate, the increase in average near-surface air temperatures would reach 1.5 °C sometime between 2030 and 2052. Past IPCC assessments reported that the global average sea level rose by some 19–21 cm (7.5–8.3 inches) between 1901 and 2010 and that sea levels rose faster in the second half of the 20th century than in the first half. It also predicted, again depending on a wide range of scenarios, that the global average sea level would rise 26–77 cm (10.2–30.3 inches) relative to the 1986–2005 average by 2100 for global warming of 1.5 °C, an average of 10 cm (3.9 inches) less than what would be expected if warming rose to 2 °C (3.6 °F) above preindustrial levels."""

n = 3        # increase the value ofn to get better prediction results

ngrams ={}

words = nltk.word_tokenize(text)

for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])
    
    
currentgram = ' '.join(words[0:n])
result = currentgram
for i in range(30):
    if currentgram not in ngrams.keys():
        break
    possibilities = ngrams[currentgram]
    nextitem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextitem
    rwords = nltk.word_tokenize(result)
    currentgram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
    
print(result)
    

    
    
