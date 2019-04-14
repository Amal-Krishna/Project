import nltk

sentence = ''' It was happening again.
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
“Why are these people fighting, Ma?”'''

for sent in nltk.sent_tokenize(sentence):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if hasattr(chunk, 'label'):
         print(chunk.label(), ' '.join(c[0] for c in chunk))
         #chunk.draw()