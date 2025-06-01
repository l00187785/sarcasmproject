import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.makedirs('app/model', exist_ok= True)

data = pd.read_json('data/sarcasm.json', lines=True)
X = data['headline']
y = data['is_sarcastic']

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vect = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_vect, y)

joblib.dump(vectorizer, 'app/model/vectorizer.pkl')
joblib.dump(model, 'app/model/sarcasm_model.pkl')
