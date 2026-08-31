"""À faire (Jour 2) : recalcul périodique des métriques de performance et
détection de dérive des données.

Rejoue `data/reference/diabetes_reference.csv` (cas nominal) sur le modèle
en Production (MLflow Model Registry), logue les métriques dans un nouveau
run MLflow, puis compare les distributions des variables cliniques à celles
du jeu d'entraînement (`data/raw/diabetes_train.csv`).

Rejouer ensuite sur `data/reference/diabetes_reference_drifted.csv` doit
mettre en évidence une dérive nette (population plus âgée, glycémie/IMC/
tension plus élevés) — à documenter dans docs/metriques_monitoring.md.
"""


def compute_performance_metrics(reference_csv: str):
    """TODO : charger le modèle en Production, prédire sur reference_csv,
    calculer accuracy/recall/f1/auc, logger dans MLflow."""
    raise NotImplementedError


def detect_drift(reference_csv: str, train_csv: str = "data/raw/diabetes_train.csv"):
    """TODO : comparer les distributions des variables entre les deux jeux
    (ex. test de Kolmogorov-Smirnov par variable) et retourner les variables
    qui dérivent significativement."""
    raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError
