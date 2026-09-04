from pathlib import Path

import joblib
import pandas as pd
import shap

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import values


# ==========================
# Chargement du modèle
# ==========================

MODEL_PATH = Path("diabetes_risk_model.pkl")

artifact = joblib.load(MODEL_PATH)

model = artifact["model"]
features = artifact["features"]
explainer = shap.TreeExplainer(model.named_steps["model"])


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


# ==========================
# Explanation
# ==========================
@app.post("/explain")
def explain(patient: Patient):

    df = pd.DataFrame([patient.model_dump()])

    prediction = int(model.predict(df)[0])

    proba = float(model.predict_proba(df)[0][1])

    shap_values = explainer.shap_values(df)

    # Pour un problème binaire
    values = shap_values[0, :, 1]

    explanations = []

    for feature, value in zip(df.columns, values):
        print(value)
        explanations.append(
            {
                "feature": feature,
                "impact": round(float(value), 4),
                "direction": (
                    "augmente le risque"
                    if value > 0
                    else "diminue le risque"
                )
            }
        )

    explanations = sorted(
        explanations,
        key=lambda x: abs(x["impact"]),
        reverse=True
    )

    return {
        "prediction": prediction,
        "risk_probability": round(proba, 3),
        "top_factors": explanations[:5]
    }
