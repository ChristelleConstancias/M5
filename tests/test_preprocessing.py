"""Tests unitaires du prétraitement — à compléter au Jour 1."""

from src.preprocessing import preprocess


def test_preprocess_returns_ordered_features():
    payload = {
        "age": 54, "sex": 1, "cp": 0, "trestbps": 130, "chol": 246,
        "fbs": 0, "restecg": 0, "thalach": 150, "exang": 0,
        "oldpeak": 1.0, "slope": 1, "ca": 0, "thal": 2,
    }
    # TODO : une fois preprocess() implémentée, vérifier la sortie attendue
    # features = preprocess(payload)
    # assert features == [54, 1, 0, 130, 246, 0, 0, 150, 0, 1.0, 1, 0, 2]
