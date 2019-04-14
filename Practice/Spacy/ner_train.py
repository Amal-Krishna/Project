from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding


TRAIN_DATA = [
    ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
    ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),
    ("India vs South Africa", {"entities": [(0, 5, "LOC"), (9, 21, "LOC")]}), 
    ("4th ODI, Vadodra", {"entities": [(0, 1, "CARDINAL"), (9, 16, "LOC")]}), 
    ("17 March 2000", {"entities": [(0, 13, "DATE")]}),     
    ("Over 45", {"entities": [(5, 7, "CARDINAL")]}),
    ("Ishaan's scream drowned out the stadium din on the TV.", {"entities": [(0, 6, "NAME")]}), 
    ("We were in Ishaan's house — Ishaan, Omi and I.", {"entities": [(11, 17, "NAME"), (28, 34, "NAME"), (36, 39, "NAME")]}),   
    ("Ishaan's mom had brought in tea and khakra for us.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}), 
    ("Tendulkar's gone.", {"entities": [(0, 9, "NAME")]}), 
    ("Omi, don't you dare move now.", {"entities": [(0, 3, "NAME")]}),
    ("India's score a ball ago was 256-2 after forty-five overs.", {"entities": [(0, 5, "LOC"), (29, 32, "CARDINAL"), (33, 34, "CARDINAL")]}),
    ("Twenty-seven runs in five overs, with eight wickets to spare and Tendulkar on the crease.", {"entities": [(43, 52, "NAME")]}),
    ("The odds were still in India's favour, but Tendulkar was out.", {"entities": [(23, 28, "LOC"), (18, 24, "LOC")]}),
    ("Ishaan glared at Omi, chiding him for his shallow sensory pleasure in a moment of national grief.", {"entities": [(0, 7, "NAME"), (17, 20, "NAME")]}),
    ("Omi and I kept our tea cups aside and looked suitably mournful.", {"entities": [(0, 3, "NAME")]}),
    ("The crowd clapped as Tendulkar made his exit.", {"entities": [(21, 30, "NAME")]}),
    ("Jadeja came to the crease and added six more runs.", {"entities": [(0, 6, "NAME")]}),
    ("End of forty-six overs, India 262/3.", {"entities": [(24, 30, "LOC"), (31, 34, "CARDINAL"), (35, 36, "CARDINAL")]}),
    ("Over 46", {"entities": [(5, 7, "CARDINAL")]}),
    ("I reached for my tea cup, but Ishaan signalled me to leave it alone.", {"entities": [(30, 36, "NAME")]}),
    ("Ishaan was pissed with us anyway.", {"entities": [(0, 6, "NAME")]}),
    ("The match was in Vadodra, just two hours away from Ahmedabad.", {"entities": [(17, 24, "LOC"), (51, 60, "LOC")]}),
    ("'It is 5.25 runs required per over,' I said, not able to resist doing a mathematical calculation.", {"entities": [(7, 11, "CARDINAL")]}),
    ("'You don't know this team. Tendulkar goes, they panic.", {"entities": [(27, 36, "NAME")]}),
    ("It is like the queen bee is dead, and the hive loses order,' Ishaan said.", {"entities": [(61, 67, "NAME")]}),
    ("Omi nodded, as he normally does to whatever Ishaan has to say about cricket.", {"entities": [(0, 3, "NAME"), (44, 50, "NAME")]}),
    ("Ishaan had always avoided this topic ever since he ran away from NDA a year ago.", {"entities": [(0, 6, "NAME"), (65, 68, "FAC")]}),
    ("'Later,' Ishaan said, staring avidly at a pimple cream commercial.", {"entities": [(9, 15, "LOC"), (18, 24, "LOC")]}),
    ("'Later when Ishaan? I have an idea that works for all of us. We don't have a lot of choice, do we?'", {"entities": [(12, 18, "NAME")]}),
    ("'All of us? Me, too?' Omi quizzed, already excited.", {"entities": [(22, 25, "NAME")]}),
    ("However, this time we needed Omi.", {"entities": [(29, 32, "NAME")]}),
    ("Yes, you play a critical role Omi.", {"entities": [(30, 33, "NAME")]}),
    ("But later when Ish?", {"entities": [(15, 18, "NAME")]}),
    ("Let's go to Gopi.", {"entities": [(12, 16, "NAME")]}),
    ("For Vidya.", {"entities": [(4, 9, "NAME")]}),
    ("Beep, beep, beep, the car came near the house again.", {"entities": [(22, 25, "VEHICLE")]}),
    ("Ish said as he saw India hit a four.", {"entities": [(0, 3, "NAME"), (19, 24, "LOC")]}),
    ("Ish picked up his bat.", {"entities": [(0, 3, "NAME")]}),
    ("Ish stood in front of the car and asked the boy to stop.", {"entities": [(0, 3, "NAME")]}),
    ("The Esteem halted in front of Ish.", {"entities": [(4, 10, "VEHICLE"), (30, 33, "NAME")]}),
    ("Ish went to the driver,an adolescent.", {"entities": [(0, 3, "NAME")]}),
    ("Ish grabbed the boy's head from behind and smashed his face into the bonnet.", {"entities": [(0,3, "NAME")]}),
    ("Ish grabbed his collar and gave six non-stop slaps across his face.", {"entities": [(0, 3, "NAME")]}),
    ("Omi picked up the bat and smashed the windscreen.", {"entities": [(0, 3, "NAME")]}),
    ("'He has been troubling Vidya since last week,' Ish said.", {"entities": [(23, 28, "NAME"), (9, 21, "LOC")]}),
    ("India vs South Africa", {"entities": [(0, 5, "LOC"), (9, 21, "LOC")]}),
    ("India vs South Africa", {"entities": [(0, 5, "LOC"), (9, 21, "LOC")]}),
    ("The Esteem halted in front of Ish.", {"entities": [(4, 10, "VEHICLE"), (30, 33, "NAME")]}),

]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, output_dir=None, n_iter=100):
    if model is not None:
        nlp = spacy.load(model)
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  
        print("Created blank 'en' model")

    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print("Losses", losses)

    # test the trained model
    for text, _ in TRAIN_DATA:
        doc = nlp(text)
        print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
        print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        for text, _ in TRAIN_DATA:
            doc = nlp2(text)
            print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
            print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])


if __name__ == "__main__":
    plac.call(main)