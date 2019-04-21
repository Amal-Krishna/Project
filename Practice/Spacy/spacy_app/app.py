from flask import Flask,render_template,url_for,request
import spacy
from spacy import displacy
import re
import en_core_web_sm

nlp = spacy.load('en_core_web_md')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        rawtext =rawtext.replace('\n',' ').replace('\r',' ')
        doc = nlp(rawtext)
        results = {}
        for ent in doc.ents:
            results.update({ent.text : ent.label_})
    
    return render_template("index.html",results=results)

if __name__ == '__main__':
    app.run(debug=True)
