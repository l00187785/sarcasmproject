def predict_sarcasm(text, model, vectorizer):
    X = vectorizer.transform([text])
    pred = model.predict(X)
    return "That's so sarcastic of you!" if pred[0] == 1 else "Sounds genuine."

