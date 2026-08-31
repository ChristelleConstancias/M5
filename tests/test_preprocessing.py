"""Tests unitaires du prétraitement — à compléter au Jour 1."""

from src.preprocessing import preprocess


def test_preprocess_returns_ordered_features():
    payload = {
        "pregnancies": 2, "glucose": 120, "blood_pressure": 72,
        "skin_thickness": 20, "insulin": 80, "bmi": 31.0,
        "diabetes_pedigree": 0.4, "age": 35,
    }
    # TODO : une fois preprocess() implémentée, vérifier la sortie attendue
    # features = preprocess(payload)
    # assert features == [2, 120, 72, 20, 80, 31.0, 0.4, 35]
