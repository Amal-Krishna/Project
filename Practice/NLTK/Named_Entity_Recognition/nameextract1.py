import nltk

doc = '''Andrew Yan-Tak Ng is a Chinese American computer scientist.
He is the former chief scientist at Baidu, where he led the company's
Artificial Intelligence Group. He is an adjunct professor (formerly 
associate professor) at Stanford University. Ng is also the co-founder
and chairman at Coursera, an online education platform. Andrew was born
in the UK in 1976. His parents were both from Hong Kong.'''

tokenized_doc = nltk.word_tokenize(doc)

tagged_sentences = nltk.pos_tag(tokenized_doc)

ne_chunked_sents = nltk.ne_chunk(tagged_sentences)

named_entities = []

for tagged_tree in ne_chunked_sents:
    if hasattr(tagged_tree, 'label'):
        print(tagged_tree.leaves())
        entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
        entity_type = tagged_tree.label()
        named_entities.append((entity_name, entity_type))
        tagged_tree.draw()

print(named_entities)


# ne_chunked_sents.draw()



sentence = '''Andrew Yan-Tak Ng is a Chinese American computer scientist.
He is the former chief scientist at Baidu, where he led the company's
Artificial Intelligence Group. He is an adjunct professor (formerly 
associate professor) at Stanford University. Ng is also the co-founder
and chairman at Coursera, an online education platform. Andrew was born
in the UK in 1976. His parents were both from Hong Kong.'''

for sent in nltk.sent_tokenize(sentence):
   for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
      if hasattr(chunk, 'label'):
         print(chunk.label(), ' '.join(c[0] for c in chunk))
         #chunk.draw()