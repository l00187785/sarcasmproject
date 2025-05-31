from flask import Flask, request, render_template
import joblib
from app.predictor import predict_sarcasm

app = Flask(__name__, template_folder='../templates')

model = joblib.load('model/sarcasm_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        text = request.form['text']
        prediction = predict_sarcasm(text, model, vectorizer)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

