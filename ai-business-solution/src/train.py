import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump
from model import train_model

df = pd.read_csv('data/raw_data.csv')
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = train_model(X_train, y_train)
dump(model, 'models/model_v1.pkl')
