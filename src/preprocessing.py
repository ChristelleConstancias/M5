"""Prétraitement des profils patients avant prédiction.

À faire (Jour 1) : reprendre la logique de préparation des données du
notebook `notebooks/entrainement_modele.ipynb` et l'exposer ici sous une
forme testable, réutilisée à la fois par l'API et par le script
d'évaluation (scripts/evaluate_model.py).
"""

FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal",
]


def preprocess(payload: dict) -> list:
    """Transforme un profil patient (dict) en vecteur de features ordonné.

    TODO : valider les types/plages de valeurs, gérer les champs manquants.
    """
    raise NotImplementedError
