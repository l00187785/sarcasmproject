import re
import numpy as np

def clean_text(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

def predict_sarcasm(text, model, vectorizer):
    text = clean_text(text)
    X = vectorizer.transform([text])
    
    # Check if input has any known words (non-zero features)
    if not np.any(X.toarray()):
        return "Hmm, that's a new one! We're working on upgrading our sarcasm skills."

    pred = model.predict(X)
    return "That's so sarcastic of you!" if pred[0] == 1 else "Sounds genuine."

