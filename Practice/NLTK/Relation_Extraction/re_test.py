import nltk
import re 
from nltk.chunk import ne_chunk_sents
from nltk.sem import relextract


def findrelations(text):
    roles = """
    (.*(                   
    computer scientist|
    led |
    adjunct professor).*)|
    co-founder|
    chairman|
    parents|
    ,\sof\sthe?\s*  # "X, of (the) Y"
    """
    ROLES = re.compile(roles, re.VERBOSE)

    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)


    for doc in chunked_sentences:
        print(doc)
        for rel in relextract.extract_rels('PER', 'ORG', doc, corpus='ace', pattern=ROLES):
            #it is a tree, so you need to work on it to output what you want
            print(relextract.show_raw_rtuple(rel)) 

findrelations('''Andrew Yan-Tak Ng is a Chinese American computer scientist.
He is the former chief scientist at Baidu, where he led the company's
Artificial Intelligence Group. He is an adjunct professor (formerly 
associate professor) at Stanford University. Ng is also the co-founder
and chairman at Coursera, an online education platform. Andrew was born
in the UK in 1976. His parents were both from Hong Kong''') 
