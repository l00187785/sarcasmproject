import os
import re
import numpy as np
import joblib

# Get the directory of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the vectorizer and model using relative paths
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model', 'vectorizer.pkl'))
model = joblib.load(os.path.join(BASE_DIR, 'model', 'sarcasm_model.pkl'))

def clean_text(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def predict_sarcasm(text, model, vectorizer):
    if not text.strip():  # Check for empty or whitespace-only input
        raise ValueError("Input text cannot be empty")
    X = vectorizer.transform([text])

    if not np.any(X.toarray()):
        return "Hmm, that's a new one! We're working on upgrading our sarcasm skills."

    pred = model.predict(X)
    return "That's so sarcastic of you!" if pred[0] == 1 else "Sounds genuine."
