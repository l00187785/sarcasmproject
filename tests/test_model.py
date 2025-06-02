import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.predictor import predict_sarcasm, model, vectorizer

def test_model_prediction():
    result = predict_sarcasm("Oh wonderful, more traffic", model, vectorizer)
    assert result in ["That's so sarcastic of you!", "Sounds genuine."]

def test_model_empty_input():
    with pytest.raises(ValueError):
        predict_sarcasm("", model, vectorizer)
