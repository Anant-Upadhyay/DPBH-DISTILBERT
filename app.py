import transformers
from transformers import pipeline, DistilBertForSequenceClassification, DistilBertTokenizerFast
from flask import Flask, render_template, request
model_path = "Notebook_output"
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer= DistilBertTokenizerFast.from_pretrained(model_path)
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
#print(nlp("2 people are viewing.")[0]['label'])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    outputText = None
    if request.method == 'POST':
        inputText = request.form['inputText']
        outputText = nlp(inputText)[0]['label']
    return render_template('index.html', outputText=outputText)

if __name__ == '__main__':
    app.run(debug=True)
