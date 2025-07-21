from fastapi import FastAPI
from src.predict import predict
import pandas as pd

app = FastAPI()

@app.get("/predict_country/")
def predict_country(country: str = "India"):
    df = pd.DataFrame([[1, 2, 3]], columns=["feature1", "feature2", "feature3"])
    prediction = predict(df)
    return {"country": country, "prediction": prediction.tolist()}
