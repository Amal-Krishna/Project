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

@app.route('/visual',methods = ['POST', 'GET'])
def visual():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        rawtext = rawtext.replace('\n',' ').replace('\r',' ')
        doc = nlp(rawtext)
        displacy.serve(doc, style='ent',port = 8080)

if __name__ == '__main__':
    app.run(debug = True)