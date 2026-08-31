"""Chargement du modèle et prédiction.

À faire (Jour 1) : charger `diabetes_risk_model.pkl`, puis l'enregistrer et
le charger depuis le MLflow Model Registry (stage Production) une fois le
tracking mis en place. Exposer une fonction de prédiction réutilisable par
l'API et les scripts de monitoring/évaluation.
"""


def load_model(path: str = "diabetes_risk_model.pkl"):
    """TODO : charger le modèle (joblib) et retourner l'objet modèle."""
    raise NotImplementedError


def predict(model, features: list) -> dict:
    """TODO : retourner la prédiction (classe + probabilité)."""
    raise NotImplementedError
