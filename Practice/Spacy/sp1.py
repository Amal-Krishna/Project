import spacy

from spacy import displacy


nlp = spacy.load('en') 

doc = nlp(u"This is a sentence.")

print([(w.text, w.pos_) for w in doc])


doc = nlp(u'Give it back! He pleaded.')
len(doc)


doc = nlp(u'Give it back')
[t.text for t in doc] 

doc = nlp(u'Give it back! He pleaded.')
doc[0].text
doc[-1].text
span = doc[1:3]
span.text 


nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
    
displacy.serve(doc, style='dep')





import spacy
from spacy import displacy

text = """But Google is starting from behind. The company made a late push
into hardware, and Apple’s Siri, available on iPhones, and Amazon’s Alexa
software, which runs on its Echo and Dot devices, have clear leads in
consumer adoption."""

nlp = spacy.load('custom_ner_model')     ####cause error as is a custom model
doc = nlp(text)
displacy.serve(doc, style='ent')



nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

text = """But Google is starting from behind. The company made a late push
into hardware, and Apple’s Siri, available on iPhones, and Amazon’s Alexa
software, which runs on its Echo and Dot devices, have clear leads in
consumer adoption."""
nlp = spacy.load('custom_ner_model')  ####works with custom trained models only
doc = nlp(text)
displacy.serve(doc, style='ent')



nlp = spacy.load('en_core_web_sm')
doc = nlp(u"""But Google is starting from behind. The company made a late push
into hardware, and Apple’s Siri, available on iPhones, and Amazon’s Alexa
software, which runs on its Echo and Dot devices, have clear leads in
consumer adoption.""")
for ent in doc.ents:
    print(ent.text, ent.label_)

displacy.serve(doc, style='ent')




nlp = spacy.load('en_core_web_sm')
doc = nlp(u""" It was happening again.
His head was dwindling, and through the rain-blotted
wind-shield, the sight of the folk-flocked Doraisami.
Subway started to look like a smudged wet photograph.
The nausea is resurfacing.
He fished into his shirt pocket, hoping to feel the
sharp edge of his last tablet strip.
No?
See? I knew it. I asked her not to change the shirt. Now
how the hell am I going to drive all the way to the Airport with this throbbing head of mine? I can't even afford to
stop anywhere. I'm already late for the drop.
I wonder what's been taking Shailaja so long to prepare
tiffin these days...tastes the same to me...
The phone that hid behind the little Lord Ganesha
idol on the dashboard buzzed. It was the lady who had
been waiting to be dropped to the airport since the past
20 minutes.She pounced into the car, and the least she could do
to indicate her fury was to slam the door hard. I hope that
gave him a headache! she mumbled.
Finally, I'm on my way. Maybe not for the best, but I
have to move on.
What's this driver honking away for?
Through the little that fit her view from behind the
baldie's head, she could make out that a wretchedlooking
woman had carelessly walked herself right across
the speeding car.
She had seen that wretched-looking woman before.
Right there. Selling cheap picture books before the
multiplex.But she didn't have books in her hands this time.
Instead she had a baby in one and an empty disfigured
plate in another. And by the time Karthika pulled out
some change from her wallet, the driver had driven past
her.
"Forget about it, madam! Who cares? We all have to
move on..."
--Even at 70 years of age, Shantiamma worked as hard
as she did 40 years ago. Weekdays were spent cleaning
the washrooms and mopping the floors at the domestic
terminal of the Chennai Airport, a job she’d been
performing since she was 23; and at weekends, she
managed to find odd jobs like sweeping the front yard of
the Consulate, or the subway sidewalks.
Today, she stopped mopping, when she saw the little
kid dancing around in her squeaky shoes on the
bathroom floor. The toddler reminded her of her little
Mutthu. And so deep was she in her own reel of
memories that she didn’t realise when the little toddler
got frightened by her continuous stare, and rushed
outside the washroom, calling after her mother.“Which story shall we read, dear? Or would you rather
sleep now?” Fedora asked, as she twisted the A/C knob to
reduce the chill.
“Nooo. You read me something. Without looking into
the book.”
Fedora smiled. “How can I read you something
without looking into the book? You mean, I should
‘narrate’ you a story.”
“Yeah. ‘Narrate.’”
“Alright, dear. Shall I tell you the story about the little
mermaid who-”
Why are these people howling at each other?
“Why are these people fighting, Ma?” """)
mystring = mystring.replace('\n', ' ').replace('\r', '')
entity = {}
for ent in doc.ents:
    entity.update({ent.text :  ent.label_})   

for c in entity:
    print("{item}: {label}".format(item=c, label=entity[c]))

displacy.serve(doc, style='ent')



import nltk

text = """It was happening again.
His head was dwindling, and through the rain-blotted
wind-shield, the sight of the folk-flocked Doraisami.
Subway started to look like a smudged wet photograph.
The nausea is resurfacing.
He fished into his shirt pocket, hoping to feel the
sharp edge of his last tablet strip.
No?
See? I knew it. I asked her not to change the shirt. Now
how the hell am I going to drive all the way to the Airport with this throbbing head of mine? I can't even afford to
stop anywhere. I'm already late for the drop.
I wonder what's been taking Shailaja so long to prepare
tiffin these days...tastes the same to me...
The phone that hid behind the little Lord Ganesha
idol on the dashboard buzzed. It was the lady who had
been waiting to be dropped to the airport since the past
20 minutes.She pounced into the car, and the least she could do
to indicate her fury was to slam the door hard. I hope that
gave him a headache! she mumbled.
Finally, I'm on my way. Maybe not for the best, but I
have to move on.
What's this driver honking away for?
Through the little that fit her view from behind the
baldie's head, she could make out that a wretchedlooking
woman had carelessly walked herself right across
the speeding car.
She had seen that wretched-looking woman before.
Right there. Selling cheap picture books before the
multiplex.But she didn't have books in her hands this time.
Instead she had a baby in one and an empty disfigured
plate in another. And by the time Karthika pulled out
some change from her wallet, the driver had driven past
her.
"Forget about it, madam! Who cares? We all have to
move on..."
--Even at 70 years of age, Shantiamma worked as hard
as she did 40 years ago. Weekdays were spent cleaning
the washrooms and mopping the floors at the domestic
terminal of the Chennai Airport, a job she’d been
performing since she was 23; and at weekends, she
managed to find odd jobs like sweeping the front yard of
the Consulate, or the subway sidewalks.
Today, she stopped mopping, when she saw the little
kid dancing around in her squeaky shoes on the
bathroom floor. The toddler reminded her of her little
Mutthu. And so deep was she in her own reel of
memories that she didn’t realise when the little toddler
got frightened by her continuous stare, and rushed
outside the washroom, calling after her mother.“Which story shall we read, dear? Or would you rather
sleep now?” Fedora asked, as she twisted the A/C knob to
reduce the chill.
“Nooo. You read me something. Without looking into
the book.”
Fedora smiled. “How can I read you something
without looking into the book? You mean, I should
‘narrate’ you a story.”
“Yeah. ‘Narrate.’”
“Alright, dear. Shall I tell you the story about the little
mermaid who-”
Why are these people howling at each other?
“Why are these people fighting, Ma?” """
text = text.replace('\n', ' ').replace('\r', '')
sentence = nltk.sent_tokenize(text)
entity = {}
for doc in nlp.pipe(sentence):
    for ent in doc.ents:
        entity.update({ent.text :  ent.label_})  


for c in entity:
    print("{item}: {label}".format(item=c, label=entity[c]))






import spacy

from spacy import displacy

nlp = spacy.load('en') 

text = """It was happening again.
His head was dwindling, and through the rain-blotted
wind-shield, the sight of the folk-flocked Doraisami.
Subway started to look like a smudged wet photograph.
The nausea is resurfacing.
He fished into his shirt pocket, hoping to feel the
sharp edge of his last tablet strip.
No?
See? I knew it. I asked her not to change the shirt. Now
how the hell am I going to drive all the way to the Airport with this throbbing head of mine? I can't even afford to
stop anywhere. I'm already late for the drop.
I wonder what's been taking Shailaja so long to prepare
tiffin these days...tastes the same to me...
The phone that hid behind the little Lord Ganesha
idol on the dashboard buzzed. It was the lady who had
been waiting to be dropped to the airport since the past
20 minutes.She pounced into the car, and the least she could do
to indicate her fury was to slam the door hard. I hope that
gave him a headache! she mumbled.
Finally, I'm on my way. Maybe not for the best, but I
have to move on.
What's this driver honking away for?
Through the little that fit her view from behind the
baldie's head, she could make out that a wretchedlooking
woman had carelessly walked herself right across
the speeding car.
She had seen that wretched-looking woman before.
Right there. Selling cheap picture books before the
multiplex.But she didn't have books in her hands this time.
Instead she had a baby in one and an empty disfigured
plate in another. And by the time Karthika pulled out
some change from her wallet, the driver had driven past
her.
"Forget about it, madam! Who cares? We all have to
move on..."
--Even at 70 years of age, Shantiamma worked as hard
as she did 40 years ago. Weekdays were spent cleaning
the washrooms and mopping the floors at the domestic
terminal of the Chennai Airport, a job she’d been
performing since she was 23; and at weekends, she
managed to find odd jobs like sweeping the front yard of
the Consulate, or the subway sidewalks.
Today, she stopped mopping, when she saw the little
kid dancing around in her squeaky shoes on the
bathroom floor. The toddler reminded her of her little
Mutthu. And so deep was she in her own reel of
memories that she didn’t realise when the little toddler
got frightened by her continuous stare, and rushed
outside the washroom, calling after her mother.“Which story shall we read, dear? Or would you rather
sleep now?” Fedora asked, as she twisted the A/C knob to
reduce the chill.
“Nooo. You read me something. Without looking into
the book.”
Fedora smiled. “How can I read you something
without looking into the book? You mean, I should
‘narrate’ you a story.”
“Yeah. ‘Narrate.’”
“Alright, dear. Shall I tell you the story about the little
mermaid who-”
Why are these people howling at each other?
“Why are these people fighting, Ma?” """

text = text.replace('\n', ' ').replace('\r', '')

doc = nlp(text)

entity = {}
for ent in doc.ents:
    entity.update({ent.text :  ent.label_})   

for c in entity:
    print("{item}: {label}".format(item=c, label=entity[c]))


displacy.serve(doc, style='ent')







#####Training


TRAIN_DATA = [
     ("Uber blew through $1 million a week", {'entities': [(0, 4, 'ORG')]}),
     ("Google rebrands its business apps", {'entities': [(0, 6, "ORG")]})]

nlp = spacy.blank('en')
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], sgd=optimizer)
nlp.to_disk('/model')



















