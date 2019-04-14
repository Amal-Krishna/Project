#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 17:30:48 2019

@author: amalk
"""

import nltk
import numpy as np
import heapq
import re


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
cups aside and looked suitably mournful.
The crowd clapped as Tendulkar made his exit. Jadeja came to the crease and
added six more runs. End of forty-six overs, India 262/3. Twenty-one more runs
to win in four overs, with seven wickets in hand.
Over 46
'He made 122. The guy did his job. Just a few final closing shots left. Why are
you getting so worked up?' I asked during a commercial break. I reached for my
tea cup, but Ishaan signalled me to leave it alone. We were not going to indulge
until the fate of the match was decided. Ishaan was pissed with us anyway. The
match was in Vadodra, just two hours away from Ahmedabad. But we could not
go - one, because we didn't have money, and two, because I had my
correspondence exams in two days. Of course, I had wasted the whole day
watching the match on TV instead, so reason number two did not really hold
much weight.
'It is 5.25 runs required per over,' I said, not able to resist doing a
mathematical calculation. That is one reason I like cricket, there is so much
maths in it.
'You don't know this team. Tendulkar goes, they panic. It isn't about the
average. It is like the queen bee is dead, and the hive loses order,' Ishaan said.
Omi nodded, as he normally does to whatever Ishaan has to say about cricket.
'Anyway, I hope you realise, we didn't meet today to see this match. We have to
decide what Mr Ishaan is doing about his future, right?' I said.
Ishaan had always avoided this topic ever since he ran away from NDA a year
ago. His dad had already sarcastically commented, 'Cut a cake today to celebrate
one year of your uselessness.'
However, today I had a plan. I needed to sit them down to talk about our lives.
Of course, against cricket, life is second priority.
'Later,' Ishaan said, staring avidly at a pimple cream commercial.
'Later when Ishaan? I have an idea that works for all of us. We don't have a lot
of choice, do we?'
'All of us? Me, too?' Omi quizzed, already excited. Idiots like him love to be part
of something, anything. However, this time we needed Omi.
'Yes, you play a critical role Omi. But later when Ish? When?'
'Oh, stop it! Look, the match is starting. Ok, over dinner. Let's go to Gopi,' Ish
said.
'Gopi? Who's paying?' I was interrupted as the match began.
Beep, beep, beep. The horn of a car broke our conversation. A car zoomed
outside the pol.
'What the hell! I am going to teach this bastard a lesson,' Ish said, looking out
the window.
'What's up?'
'Bloody son of a rich dad. Comes and circles around our house everyday'
'Why?' I said.
'For Vidya. He used to be in coaching classes with her. She complained about
him there too,' Ish said.
Beep, beep, beep, the car came near the house again.
'Damn, I don't want to miss this match,' Ish said as he saw India hit a four. Ish
picked up his bat. We ran out the house. The silver Esteem circled the pol and
came back for another round of serenading. Ish stood in front of the car and
asked the boy to stop. The Esteem halted in front of Ish. Ish went to the driver,
an adolescent.
'Excuse me, your headlight is hanging out.'
'Really?' the boy said and shut off the ignition. He stepped outside and came to
the front.
Ish grabbed the boy's head from behind and smashed his face into the bonnet.
He proceeded to strike the headlight with his bat. The glass broke and the bulb
hung out.
'What's your problem,' the boy said, blood spurting out of his nose.
'You tell me what's up? You like pressing horns?' Ish said.
Ish grabbed his collar and gave six non-stop slaps across his face. Omi picked
up the bat and smashed the windscreen. The glass broke into a million pieces.
People on the street gathered around as there is nothing quite as entertaining as
a street fight.
The boy shivered in pain and fear. What would he tell his daddy about his
broken car and face?
Ish's dad heard the commotion and came out of the house. Ish held the boy in
an elbow lock. The boy was struggling to breathe.
'Leave him,' Ish's dad said.
Ish gripped him tighter.
'I said leave him,' Ish's dad shouted, 'what's going on here?'
'He has been troubling Vidya since last week,' Ish said. He kicked the boy's face
with his knee and released him. The boy kneeled on the floor and sucked in air.
The last kick from Ish had smeared the blood from his nose across his face.
'And what do you think you are doing?' Ish's dad asked him.
'Teaching him a lesson,' Ish said and unhooked his bat stuck in the
windscreen.
 """
 
 
#pre-processing
 
dataset = nltk.sent_tokenize(text)

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W',' ',dataset[i])
    dataset[i] = re.sub(r'\s+',' ',dataset[i])
     
    
#creating histogram

word2count = {}

for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
 
    
# creating most frequent words list
            
freq_words = heapq.nlargest(325,word2count,key=word2count.get)

# IDF matrix

word_idfs = {}

for word in freq_words:
    doc_count = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            doc_count += 1
    word_idfs[word] = np.log((len(dataset)/doc_count)+1)


# tf matrix
    
tf_matrix = {}

for word in freq_words:
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if word == w:
                frequency += 1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
        tf_matrix[word] = doc_tf


# TF-IDF Calculation
        
tfidf_matrix =[]

for word in tf_matrix.keys():
    tfidf = []
    for value in tf_matrix[word]:
        score =  value * word_idfs[word]
        tfidf.append(score)
    tfidf_matrix.append(tfidf)    

X = np.asarray(tfidf_matrix)

X = np.transpose(X)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 