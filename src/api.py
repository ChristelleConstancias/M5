from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel


# ==========================
# Chargement du modèle
# ==========================

MODEL_PATH = Path("diabetes_risk_model.pkl")

artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
features = artifact["features"]


# ==========================
# FastAPI
# ==========================

app = FastAPI(
    title="Diabetes Risk API",
    version="1.0"
)


# ==========================
# Input Schema
# ==========================

class Patient(BaseModel):
    pregnancies: int
    glucose: int
    blood_pressure: int
    skin_thickness: int
    insulin: int
    bmi: float
    diabetes_pedigree: float
    age: int



# ==========================
# Health Check
# ==========================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "model_loaded": True
    }


# ==========================
# Prediction
# ==========================

@app.post("/predict")
def predict(patient: Patient):

    X = pd.DataFrame([patient.dict()])

    prediction = int(model.predict(X)[0])

    probability = float(
        model.predict_proba(X)[0][1]
    )

    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }