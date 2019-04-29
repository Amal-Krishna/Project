# -*- coding: utf-8 -*-

from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm
nlp = spacy.load('en_core_web_md')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        rawtext = rawtext.replace('\n',' ').replace('\r',' ')
        doc = nlp(rawtext)
        d = []
        for ent in doc.ents:
            d.append((ent.label_,ent.text))
            df = pd.DataFrame(d,columns=('named entity','output'))
            ORG_named_entity = df.loc[df['named entity'] == 'ORG']['output']
            PERSON_named_entity = df.loc[df['named entity'] == 'PERSON']['output']
            GPE_named_entity = df.loc[df['named entity'] == 'GPE']['output']
            MONEY_named_entity = df.loc[df['named entity'] == 'MONEY']['output']
            FAC_named_entity = df.loc[df['named entity'] == 'FAC']['output']
            PRODUCT_named_entity = df.loc[df['named entity'] == 'PRODUCT']['output']
            LOC_named_entity = df.loc[df['named entity'] == 'LOC']['output']
            EVENT_named_entity = df.loc[df['named entity'] == 'EVENT']['output']
            WORK_OF_ART_named_entity = df.loc[df['named entity'] == 'WORK_OF_ART']['output']
            LANGUAGE_named_entity = df.loc[df['named entity'] == 'LANGUAGE']['output']
            PERCENT_named_entity = df.loc[df['named entity'] == 'PERCENT']['output']
            TIME_named_entity = df.loc[df['named entity'] == 'TIME']['output']
            DATE_named_entity = df.loc[df['named entity'] == 'DATE']['output']
            QUANTITY_named_entity = df.loc[df['named entity'] == 'QUANTITY']['output']
            CARDINAL_named_entity = df.loc[df['named entity'] == 'CARDINAL']['output']
        if choice == 'organization':
            results = ORG_named_entity
            num_of_results = len(results)
        elif choice == 'person':
            results = PERSON_named_entity
            num_of_results = len(results)
        elif choice == 'geopolitical':
            results = GPE_named_entity
            num_of_results = len(results)
        elif choice == 'money':
            results = MONEY_named_entity
            num_of_results = len(results)
        elif choice == 'facility':
            results = FAC_named_entity
            num_of_results = len(results)
        elif choice == 'product':
            results = PRODUCT_named_entity
            num_of_results = len(results)
        elif choice == 'location':
            results = LOC_named_entity
            num_of_results = len(results)
        elif choice == 'event':
            results = EVENT_named_entity
            num_of_results = len(results)
        elif choice == 'work_of_art':
            results = WORK_OF_ART_named_entity
            num_of_results = len(results)
        elif choice == 'language':
            results = LANGUAGE_named_entity
            num_of_results = len(results)
        elif choice == 'time':
            results = TIME_named_entity
            num_of_results = len(results)
        elif choice == 'date':
            results = DATE_named_entity
            num_of_results = len(results)
        elif choice == 'percent':
            results = PERCENT_named_entity
            num_of_results = len(results)
        elif choice == 'quantity':
            results = QUANTITY_named_entity
            num_of_results = len(results)
        elif choice == 'cardinal':
            results = CARDINAL_named_entity
            num_of_results = len(results)
        results = set(results)
        
    return render_template("index.html",results=results,num_of_results = num_of_results)

if __name__ == '__main__':
    app.run(debug=True)