import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.makedirs('app/model', exist_ok= True)

data = pd.read_json('data/sarcasm.json', lines=True)
X = data['headline']
y = data['is_sarcastic']
# converts words into numbers using TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vect = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_vect, y)
# This saves the trained word-understanding tool so it can be used later without training it again
joblib.dump(vectorizer, 'app/model/vectorizer.pkl')
#This saves the fully trained the sarcasm detection model so the website can use it to make predictions.
joblib.dump(model, 'app/model/sarcasm_model.pkl')
