#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:57:22 2019

@author: amalk
"""


import numpy as np
import nltk
import pickle
import re
from nltk.corpus import stopwords
from sklearn.datasets import load_files
"""nltk.download('stopwords')"""


reviews = load_files('txt_sentoken/')

X,Y = reviews.data,reviews.target

"""with open('X.pickle','wb') as f:
    pickle.dump(X,f)
    
with open('Y.pickle','wb') as f:
    pickle.dump(Y,f)

with open('X.pickle','rb') as f:
    X = pickle.load(f)
    
with open('Y.pickle','rb') as f:
    Y = pickle.load(f)"""


corpus = []

for i in range(0,len(X)):
    review = re.sub(r'\W',' ',str(X[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+',' ',review)
    review = re.sub(r'\s+',' ',review)
    corpus.append(review)


#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer(max_features=2000,min_df=5,max_df=0.5,stop_words=stopwords.words('english'))
#X = vectorizer.fit_transform(corpus).toarray()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=2000,min_df=5,max_df=0.5,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(X).toarray()


from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test = train_test_split(X,Y,test_size=0.2,random_state =0 )


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)

sent_pred = classifier.predict(text_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test,sent_pred)


#sum_of_tp_tn = cm[0][0]+cm[1][1]

#accuracy =  sum_of_tp_tn/len(sent_test)*100

#print(accuracy)

with open('classifier.pickle','wb') as f:
    pickle.dump(classifier,f)


with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)


with open('classifier.pickle','rb') as f:
    clf = pickle.load(f)


with open('tfidfmodel.pickle','rb') as f:
    tfidf = pickle.load(f)



sample = ["You are a very nice person,have a good life"]
sample = tfidf.transform(sample).toarray()
print(clf.predict(sample))


sample1 = ["that is a bad movie"]
sample1 = tfidf.transform(sample1).toarray()
print(clf.predict(sample1))













