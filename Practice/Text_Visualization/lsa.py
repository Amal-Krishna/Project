#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:55:15 2019

@author: amalk
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import re
import numpy as np
import nltk

dataset = ["""She stood two places ahead of me in the lunch line at the IIMA mess. I checked her out
from the corner of my eye, wondering what the big fuss about this South Indian girl was.
Her waist-length hair rippled as she tapped the steel plate with her fingers like a
famished refugee. I noticed three black threads on the back of her fair neck. Someone
had decided to accessorise in the most academically-oriented B-school in the country.
‘Ananya Swaminathan—best girl in the fresher batch,’ seniors had already
anointed her on the dorm board. We had only twenty girls in a batch of two hundred.
Good-looking ones were rare; girls don’t get selected to IIM for their looks. They get in
because they can solve mathematical problems faster than 99.9% of India’s population
and crack the CAT. Most IIM girls are above shallow things like make-up, fitting clothes,
contact lenses, removal of facial hair, body odour and feminine charm.""",
"""1900 BC, Mansarovar Lake
Shiva gazed at the orange sky. The clouds hovering above Mansarovar had just parted
to reveal the setting sun. The brilliant giver of life was calling it a day once again. Shiva
had seen a few sunrises in his twenty-one years. But the sunset! He tried never to miss
the sunset! On any other day, Shiva would have taken in the vista — the sun and the
immense lake against the magnificent backdrop of the Himalayas stretching as far back
as the eye could see. But not today.
He squatted and perched his lithe, muscular body on the narrow ledge extending over
the lake. The numerous batde-scars on his skin gleamed in the shimmering reflected
light of the waters. Shiva remembered well his carefree childhood days. He had
perfected the art of throwing pebbles that bounced off the surface of the lake. He still
held the record in his tribe for the highest number of bounces: seventeen.
On a normal day, Shiva would have smiled at the memory from a cheerful past that had
been overwhelmed by the angst of the present. But today, he turned back towards his
village without any hint of joy.
Bhadra was alert, guarding the main entrance. Shiva gestured with his eyes. Bhadra
turned back to find his two back-up soldiers dozing against the fence. He cursed and
kicked them hard.
Shiva turned back towards the lake.""",
"""May in Ayemenem is a hot, brooding month. The days are long and humid. The river shrinks
and black crows gorge on bright mangoes in still, dustgreen trees. Red bananas ripen. Jackfruits
burst. Dissolute bluebottles hum vacuously in the fruity air. Then they stun themselves against clear
windowpanes and die, fatly baffled in the sun.
The nights are clear, but suffused with sloth and sullen expectation.
But by early June the southwest monsoon breaks and there are three months of wind and
water with short spells of sharp, glittering sunshine that thrilled children snatch to play with. The
countryside turns an immodest green. Boundaries blur as tapioca fences take root and bloom. Brick
walls turn moss green. Pepper vines snake up electric poles. Wild creepers burst through laterite
banks and spill across flooded roads. Boats ply in the bazaars. And small fish appear in the puddles
that fill the PWD potholes on the highways.""",
"""But fate was against the Pakratis yet again. Thanks to the foreign presence, Shiva had
ordered the Gunas to remain alert. Thus they were forewarned and the Pakratis lost the
element of surprise. The presence of the Meluhans was also decisive, turning the tide of
the short, brutal battle in favour of the Gunas. The Pakratis had to retreat.
Bloodied and scarred, Shiva surveyed the damage at the end of the battle. Two Guna
soldiers had succumbed to their injuries. They would be honoured as clan heroes. But
even worse, the warning had come too late for at least ten Guna women and children.
Their mutilated bodies were found next to the lake. The losses were high.
Bastards They kill women and children when they can’t beat us!
A livid Shiva called the entire tribe to the centre of the village. His mind was made.
‘This land is fit for barbarians! We have fought pointless battles with no end in sight. You
know my uncle tried to make peace, even offering access to the lake shore to the
mountain tribes. But these scum mistook our desire for peace as weakness. We all
know what followed!’ """,
""" They were nearly born on a bus, Estha and Rahel. The car in which Baba, their father, was
taking Ammu, their mother, to hospital in Shillong to have them, broke down on the winding
tea-estate road in Assam. They abandoned the car and flagged down a crowded State Transport bus.
With the queer compassion of the very poor for the comparatively well off, or perhaps only because
they saw how hugely pregnant Ammu was, seated passengers made room for the couple, and for the
rest of the journey Estha and Rahel’s father had to hold their mother’s stomach (with them in it) to
prevent it from wobbling. That was before they were divorced and Ammu came back to live in
Kerala."""
           ]
dt = []
for line in dataset:
    data = nltk.sent_tokenize(line)
    for d in data:
        dt.append(d)
        
dt = [ line.lower() for line in dt ]


dt = [ re.sub(r"\W"," ",line) for line in dt]

dt = [ re.sub(r"\s+"," ",line) for line in dt]
    

""" dataset = [ line.lower() for line in dataset]

dataset = [ re.sub(r"\W"," ",line) for line in dataset]

dataset = [ re.sub(r"\s+"," ",line) for line in dataset] """

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

#print(X[0])

#np.shape(X)
                        ## X is tfidf matrix
#print(X[1])

lsa = TruncatedSVD(n_components=3,n_iter = 200)  #n_components - specify the no of concepts
lsa.fit(X)                                      # n_iter - larger no of iteration is required for greater efficiency

#type(lsa)


##row1,2,3 are the three concepts which forms 3 rows of V-Transpose matrix 

#row1 = lsa.components_[0]

#row2 = lsa.components_[1]

#row3 = lsa.components_[2]

concept_words = {}

terms = vectorizer.get_feature_names()

for i,comp in enumerate(lsa.components_):
    componentterms = zip(terms,comp)
    sortedterms = sorted(componentterms,key=lambda x:x[1],reverse = True)
    sortedterms = sortedterms[:200]
    concept_words["concept"+str(i)] = sortedterms
    #print("\nConcept",i,":")
    #for term in sortedterms:
        #print(term)
        
for key in concept_words.keys():
    sentence_scores = []
    for sentence in dataset:
        words = nltk.word_tokenize(sentence)
        score = 0
        for word in words:
            for word_with_score in concept_words[key]:
                if word == word_with_score[0]:
                    score += word_with_score[1]
        sentence_scores.append(score)
    print("\n"+key+":")
    for sentence_score in sentence_scores:
        print(sentence_score)
        
    
        


















