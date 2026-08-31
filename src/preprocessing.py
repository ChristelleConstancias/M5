"""Prétraitement des profils patients avant prédiction.

À faire (Jour 1) : reprendre la logique de préparation des données du
notebook `notebooks/entrainement_modele.ipynb` et l'exposer ici sous une
forme testable, réutilisée à la fois par l'API et par les scripts de
monitoring/évaluation (scripts/monitor_metrics.py, scripts/evaluate_model.py).
"""

FEATURES = [
    "pregnancies", "glucose", "blood_pressure", "skin_thickness",
    "insulin", "bmi", "diabetes_pedigree", "age",
]


def preprocess(payload: dict) -> list:
    """Transforme un profil patient (dict) en vecteur de features ordonné.

    TODO : valider les types/plages de valeurs, gérer les champs manquants.
    """
    raise NotImplementedError
