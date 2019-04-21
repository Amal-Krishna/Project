#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:10:53 2019

@author: amalk
"""

import re
import nltk
import heapq

text = """She stood two places ahead of me in the lunch line at the IIMA mess. I checked her out
from the corner of my eye, wondering what the big fuss about this South Indian girl was.
Her waist-length hair rippled as she tapped the steel plate with her fingers like a
famished refugee. I noticed three black threads on the back of her fair neck. Someone
had decided to accessorise in the most academically-oriented B-school in the country.
‘Ananya Swaminathan—best girl in the fresher batch,’ seniors had already
anointed her on the dorm board. We had only twenty girls in a batch of two hundred.
Good-looking ones were rare; girls don’t get selected to IIM for their looks. They get in
because they can solve mathematical problems faster than 99.9% of India’s population
and crack the CAT. Most IIM girls are above shallow things like make-up, fitting clothes,
contact lenses, removal of facial hair, body odour and feminine charm. Girls like
Ananya, if and when they arrive by freak chance, become instant pin-ups in our
testosterone-charged, estrogen-starved campus.
I imagined Ms Swaminathan had received more male attention in the last week
than she had in her entire life. Thus, I assumed she’d be obnoxious and decided to ignore
her.
The students inched forward on auto-pilot. The bored kitchen staff couldn’t care if
they were serving prisoners or future CEOs. They tossed one ladle of yellow stuff after
another into plates. Of course, Ms Best Girl needed the spotlight.
‘That’s not rasam. Whatever it is, it’s definitely not rasam. And what’s that, the
dark yellow stuff?’
‘Sambhar,’ the mess worker growled.
‘Eew, looks disgusting! How did you make it?’ she asked.
‘You want or not?’ the mess worker said, more interested in wrapping up lunch
than discussing recipes.
While our lady decided, the two boys between us banged their plates on the
counter. They took the food without editorials about it and left. I came up right behind
her. I stole a sideways glance—definitely above average. Actually, well above average.
In fact, outlier by IIMA standards. She had perfect features, with her eyes, nose, lips
and ears the right size and in right places. That is all it takes to make people beautiful—
normal body parts—yet why does nature mess it up so many times? Her tiny blue bindi
matched her sky-blue and white salwar kameez. She looked like Sridevi’s smarter
cousin, if there is such a possibility.
The mess worker dumped a yellow lump on my plate.
‘Excuse me, I’m before him,’ she said to the mess worker, pinning him down with
her large, confident eyes.
‘What you want?’ the mess worker said in a heavy South Indian accent. ‘You
calling rasam not rasam. You make face when you see my sambhar. I feed hundred
people. They no complain.’
‘And that is why you don’t improve. Maybe they should complain,’ she said.
The mess worker dropped the ladle in the sambhar vessel and threw up his hands.
‘You want complain? Go to mess manager and complain . . . see what student coming to
these days,’ the mess worker turned to me, seeking sympathy.
I almost nodded.
She looked at me. ‘Can you eat this stuff?’ she wanted to know. ‘Try it.’
I took a spoonful of sambhar. Warm and salty, not gourmet stuff, but edible in a no-
choice kind of way. I could eat it for lunch; I had stayed in a hostel for four years.
However, I saw her face, now prettier with a hint of pink. I compared her to the
fifty-year-old mess worker. He wore a lungi and had visible grey hair on his chest.
When in doubt, the pretty girl is always right.
‘It’s disgusting,’ I said.
‘See,’ she said with childlike glee.
The mess worker glared at me.
‘But I can develop a taste for it,’ I added in a lame attempt to soothe him.
The mess worker grunted and tossed a mound of rice on my plate.
‘Pick something you like,’ I said to her, avoiding eye contact. The whole campus
had stared at her in the past few days. I had to appear different.
‘Give me the rasgullas,’ she pointed to the dessert.
‘That is after you finish meal,’ the mess worker said.
‘Who are you? My mother? I am finished. Give me two rasgullas,’ she insisted.
‘Only one per student,’ he said as he placed a katori with one sweet on her plate.
‘Oh, come on, there are no limits on this disgusting sambhar but only one of what
is edible,’ she said. The line grew behind us. The boys in line didn’t mind. They had a
chance to legitimately stare at the best-looking girl of the batch.
‘Give mine to her,’ I said and regretted it immediately. She’ll never date you, it is
a rasgulla down the drain, I scolded myself.
‘I give to you,’ the mess worker said virtuously as he placed the dessert on my
plate.
I passed my katori to her. She took the two rasgullas and moved out of the line.
OK buddy, pretty girl goes her way, rasgulla-less loser goes another. Find a
corner to sit, I said to myself.
She turned to me. She didn’t ask me to sit with her, but she looked like she
wouldn’t mind if I did. She pointed to a table with a little finger where we sat down
opposite each other. The entire mess stared at us, wondering what I had done to merit
sitting with her. I have made a huge sacrifice—my dessert—I wanted to tell them.
‘I’m Krish,’ I said, doodling in the sambhar with my spoon.
‘I’m Ananya. Yuk, isn’t it?’ she said as I grimaced at the food’s taste.
‘I’m used to hostel food,’ I shrugged. ‘I’ve had worse.’
‘Hard to imagine worse,’ she said.
I coughed as I bit on a green chilli. She had a water jug next to her. She lifted the
jug, leaned forward and poured water for me. A collective sigh ran through the mess. We
had become everyone’s matinee show.
She finished her two desserts in four bites. ‘I’m still hungry. I didn’t even have
breakfast.’
‘Hunger or tasteless food, hostel life is about whatever is easier to deal with,’said.
‘You want to go out? I’m sure this city has decent restaurants,’ she said.
‘Now?’ We had a class in one hour. But Ms Best Girl had asked me out, even
though for her own stomach. And as everyone knows, female classmates always come
before class.
‘Don’t tell me you are dying to attend the lecture,’ she said and stood up, daring
me.
I spooned in some rice.
She stamped a foot. ‘Leave that disgusting stuff.’
Four hundred eyes followed us as I walked out of the mess with Ms Ananya
Swaminathan, rated the best girl by popular vote in IIMA.
I
‘Do you like chicken?’ The menu rested on her nose as she spoke. We had come to
Topaz, a basic, soulless but air-conditioned restaurant half a kilometre from campus.
Like all mid-range Indian restaurants, it played boring instrumental versions of old Hindi
songs and served little marinated onions on the table.
‘I thought Ahmedabad was vegetarian,’ I said.
‘Please, I’d die here then.’ She turned to the waiter and ordered half a tandoori
chicken with roomali rotis.
‘Do you have beer?’ she asked the waiter.
The waiter shook his head in horror and left.
‘We are in Gujarat, there is prohibition here,’ I said.
‘Why?’
‘Gandhiji’s birthplace,’ I said.
‘But Gandhiji won us freedom,’ she said, playing with the little onions. ‘What’s
the point of getting people free only to put restrictions on them?’
‘Point,’ I said. ‘So, you are an expert on rasam and sambhar. Are you South
Indian?’
‘Tamilian, please be precise. In fact, Tamil Brahmin, which is way different from
Tamilians. Never forget that.’ She leaned back as the waiter served our meal. She tore a
chicken leg with her teeth.
‘And how exactly are Tamil Brahmins different?’
‘Well, for one thing, no meat and no drinking,’ she said as she gestured a cross
with the chicken leg.
‘Absolutely,’ I said.
She laughed. ‘I didn’t say I am a practising Tam Brahm. But you should know that I
am born into the purest of pure upper caste communities ever created. What about you,
commoner?’
‘I am a Punjabi, though I never lived in Punjab. I grew up in Delhi. And I have no
idea about my caste, but we do eat chicken. And I can digest bad sambhar better than
Tamil Brahmins,’ I said.
‘You are funny,’ she said, tapping my hand. I liked the tap.
‘So where did you stay in hostel before?’ she said. ‘Please don’t say IIT, you are
doing pretty well so far.’
‘What’s wrong with IIT?’
‘Nothing, are you from there?’ She sipped water.
‘Yes, from IIT Delhi. Is that a problem?’
‘No,’ she smiled, ‘not yet.’
‘Excuse me?’ I said. Her smugness had reached irritating levels.
‘Nothing,’ she said.
We stayed quiet.
‘What’s the deal? Someone from IIT broke your heart?’
She laughed. ‘No, on the contrary. I seem to have broken some, for no fault of my
own.’
‘Care to explain?’
‘Don’t tell anyone, but in the past one week that I’ve been here, I’ve had ten
proposals. All from IITians.’
I mentally kicked myself. My guess was right; she was getting a lot of attention. I
only wished it wasn’t from my own people.
‘Proposals for what?’
‘The usual, to go out, be friends and stuff. Oh, and one guy from IIT Chennai
proposed marriage!’
‘Serious?’
‘Yes, he said this past week has been momentous for him. He joined IIMA, and
now he has found his wife in me. I may be wrong, but I think he had some jewellery on
him.’
I smacked my forehead. No, my collegemates can’t be doing this, whatever the
deprivation.
‘So, you understand my concern about you being from IIT,’ she said, picking up a
chicken breast next.
‘Oh, so it is a natural reaction. If I am from IIT, I have to propose to you within ten
minutes?’
‘I didn’t say that.’
‘You implied that.’
‘I’m sorry.’
‘It’s OK. I expected you to be like this. Let me guess—only child, rich parents?’
‘Wrong, wrong. I have a younger brother. And my father works in Bank of Baroda
in Chennai. Sorry, you expected me to be like what?’
‘Some girls cannot handle attention. Two days of popularity and every guy in
college should bow to you.’
‘That’s not true. Didn’t I come out with you?’ She neatly transferred the bare bones
of the chicken on to another plate.
‘Oh, that’s huge. Coming out with a commoner like me. How much is the bill? I’ll
pay my share and leave.’ I stood up.
‘Hey,’ she said.
‘What?’
‘I’m sorry. Please sit down.’
I had lost interest in the conversation anyway. If there is nothing as attractive as a
pretty girl, there’s nothing as repulsive as a cocky chick.
I sat back and focussed on the food and the irritating instrumental music for the
next ten minutes. I ignored the Brahmin who stereotyped my collegemates.
‘Are we OK now?’ she smiled hesitantly.
‘Why did you come out with me? To take your score to eleven?’
‘You really want to know?’
‘Yes.’
‘I need some friends here. And you seemed like a safe-zone guy. Like the kind of
guy who could just be friends with a girl, right?’
Absolutely not, I thought. Why would any guy want to be only friends with a girl?
It’s like agreeing to be near a chocolate cake and never eat it. It’s like sitting in a
racing car but not driving it. Only wimps do that.
‘I’m not so sure,’ I said.
‘You can handle it. I told you about the proposals because you can see how stupid
they are.’
‘They are not stupid. They are IITians. They just don’t know how to talk to women
yet,’ I said.
‘Whatever. But you do. And I’d like to be friends with you. Just friends, OK?’ She
extended her hand. I gave her a limp handshake.
‘Let’s share, sixty each,’ she said as the bill arrived.
That’s right, ‘just friends’ share bills. I didn’t want to be just friends with her. And
I didn’t want to be the eleventh martyr.
I paid my share and came back to campus. I had no interest in meeting my just
friend anytime again soon."""


text = re.sub(r'\s+',' ',text)
clean_text = text.lower()
clean_text = re.sub(r'\W',' ',clean_text)
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)

sentences = nltk.sent_tokenize(text)

stop_words = nltk.corpus.stopwords.words('english')

word2count ={}

for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())


sent2score = {}

for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2count.keys():
            if len(sentence.split(' ')) > 6:
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]
                else:
                    sent2score[sentence] = word2count[word]
                    
best_sentences = heapq.nlargest(50,sent2score,key=sent2score.get) 

for sentence in best_sentences:
    print(sentence)                 


        

























