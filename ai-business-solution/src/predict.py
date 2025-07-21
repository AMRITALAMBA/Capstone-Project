import joblib
import pandas as pd

def predict(df, model_path="models/model_v1.pkl"):
    model = joblib.load(model_path)
    return model.predict(df)
