import os
from flask import Flask, request, render_template
import joblib
from predictor import predict_sarcasm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
MODEL_DIR = os.path.join(BASE_DIR, 'model')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

vectorizer = joblib.load(os.path.join(MODEL_DIR, 'vectorizer.pkl'))
model = joblib.load(os.path.join(MODEL_DIR, 'sarcasm_model.pkl'))

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        text = request.form['text']
        if not text.strip():  # Check for empty or whitespace-only input
            return "Error: Input text cannot be empty", 400  # Return HTTP 400 status code
        prediction = predict_sarcasm(text, model, vectorizer)
    return render_template('index.html', prediction=prediction)
