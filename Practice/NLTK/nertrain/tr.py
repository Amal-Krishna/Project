#training a nltk ner

data = [(['Linux', 'is', 'the', 'best', 'OS'], ['OS','IR','IR','IR','IR']),
(['Ubuntu', 'is', 'my', 'favourite', 'OS'], ['OS','IR','IR','IR','IR'])]
corpus = []
for (doc, tags) in data:
    doc_tag = []
    for word, tag in zip(doc,tags):
        doc_tag.append((word, tag))
    corpus.append(doc_tag)
print(corpus)


def doc2features(doc, i):
    word = doc[i][0]
    
    # Features from current word
    features={
        'word.word': word,
    }
    if i > 0:
        prevword = doc[i-1][0]
        features['word.prevword'] = prevword
    else:
        features['BOS'] = True # Special "Beginning of Sequence" tag
        
    # Features from next word
    if i < len(doc)-1:
        nextword = doc[i+1][0]
        features['word.nextword'] = nextword
    else:
          features['EOS'] = True # Special "End of Sequence" tag
    return features
 
def extract_features(doc):
    return [doc2features(doc, i) for i in range(len(doc))]
 
X = [extract_features(doc) for doc in corpus]
print(X)



def get_labels(doc):
    return [tag for (token,tag) in doc]
y = [get_labels(doc) for doc in corpus]
print(y)

import sklearn_crfsuite

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=20,
    all_possible_transitions=False,
)

crf.fit(X, y);



test = [['CentOS', 'is', 'my', 'favourite', 'OS']]

X_test = extract_features(test)
print(crf.predict_single(X_test))

test1 = [['kubuntu','is','my','favorite','os']]

X_test1 = extract_features(test1)
print(crf.predict_single(X_test1))








