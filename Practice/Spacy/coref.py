#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:01:18 2019

@author: amalk
"""

import spacy

nlp = spacy.load('en')

import neuralcoref

neuralcoref.add_to_pipe(nlp)

doc = nlp(u'My sister has a dog. She loves him.')

doc._.has_coref


doc._.coref_clusters

doc._.coref_scores


doc._.coref_clusters


doc._.coref_clusters[1].mentions


text = """ Ishaan's scream drowned out the
stadium din on the TV. I had shifted up to a sofa from the floor.
`Huh?' I said. We were in Ishaan's house — Ishaan, Omi and I. Ishaan's mom
had brought in tea and khakra for us. 'It is more comfortable to snack on the
sofa. That is why I moved.'
`Tendulkar's gone. Fuck, now at this stage. Omi, don't you dare move now.
Nobody moves for the next five overs.'
I looked at the TV. We were chasing 283 to win. India's score a ball ago was
256-2 after forty-five overs. Twenty-seven runs in five overs, with eight wickets to
spare and Tendulkar on the crease. A cakewalk. The odds were still in India's
favour, but Tendulkar was out. And that explained the frowns on Ishaan's
forehead.
'The khakra's crispy,' Omi said. Ishaan glared at Omi, chiding him for his
shallow sensory pleasure in a moment of national grief. Omi and I kept our tea
cups aside and looked suitably mournful."""



text = text.replace('\n', ' ').replace('\r', '')


doc = nlp(text)


doc._.has_coref


doc._.coref_clusters


























