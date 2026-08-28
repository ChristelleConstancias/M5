"""Chargement du modèle et prédiction.

À faire (Jour 1) : charger `heart_risk_model.pkl` (ou, à partir du Jour 2,
la version enregistrée dans le MLflow Model Registry) et exposer une
fonction de prédiction réutilisable par l'API et le script d'évaluation.
"""


def load_model(path: str = "heart_risk_model.pkl"):
    """TODO : charger le modèle (joblib) et retourner l'objet modèle."""
    raise NotImplementedError


def predict(model, features: list) -> dict:
    """TODO : retourner la prédiction (classe + probabilité)."""
    raise NotImplementedError
