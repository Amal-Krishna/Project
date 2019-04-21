#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:25:13 2019

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


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=2000,min_df=5,max_df=0.5,stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
X = transformer.fit_transform(X).toarray()


from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test = train_test_split(X,Y,test_size=0.2,random_state =0 )


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)

sent_pred = classifier.predict(text_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test,sent_pred)


sum_of_tp_tn = cm[0][0]+cm[1][1]

accuracy =  sum_of_tp_tn/len(sent_test)*100

print(accuracy)




































