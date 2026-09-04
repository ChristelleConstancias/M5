# tests/test_model_quality.py

from pathlib import Path
from pyexpat import model
import joblib
import pandas as pd

from sklearn.metrics import recall_score
from src.train_model import train_the_model


MODEL_PATH = Path("diabetes_risk_model.pkl")

# Fonction utilitaire pour charger ou entraîner le modèle si nécessaire
def load_or_train_model():
    """
    Charge le modèle s'il existe, sinon lance l'entraînement.
    """

    if MODEL_PATH.exists():
        artifact = joblib.load(MODEL_PATH)

        if isinstance(artifact, dict):
            return artifact["model"], artifact["features"]

        return artifact, None

    model, features = train_the_model()

    return model, features

# test de la qualité du modèle
def test_model_recall():
    model, features = load_or_train_model()

    df = pd.read_csv("data/reference/diabetes_reference_drift.csv")

    X = df.drop(columns=["outcome"])
    y = df["outcome"]

    if features is not None:
        X = X[features]

    y_pred = model.predict(X)

    recall = recall_score(y, y_pred)

    assert recall >= 0.60, (
        f"Recall insuffisant : {recall:.4f} < 0.60"
    )