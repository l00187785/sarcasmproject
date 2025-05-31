def test_model_prediction():
    import joblib
    model = joblib.load('model/sarcasm_model.pkl')
    vectorizer = joblib.load('model/vectorizer.pkl')
    test_text = ["Oh wonderful, more traffic"]
    X = vectorizer.transform(test_text)
    pred = model.predict(X)
    assert pred[0] in [0, 1]
