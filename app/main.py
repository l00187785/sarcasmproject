mport os
from flask import Flask, request, render_template
import joblib
from predictor import predict_sarcasm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
MODEL_DIR = os.path.join(BASE_DIR, 'model')

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# loads a pre-trained machine learning model and a text vectorizer using joblib

vectorizer = joblib.load(os.path.join(MODEL_DIR, 'vectorizer.pkl'))
model = joblib.load(os.path.join(MODEL_DIR, 'sarcasm_model.pkl'))

@app.route('/', methods=['GET', 'POST'])
def home():
prediction = ""
if request.method == 'POST':
text = request.form['text']
prediction = predict_sarcasm(text, model, vectorizer)
return render_template('index.html', prediction=prediction)

# sets up the web server to run locally
if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0')

# When text is submitted, the predict_sarcasm function (from predictor.py) uses these loaded components
# to determine if the input is sarcastic. The result is then displayed on the web page.
