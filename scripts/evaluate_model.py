"""À faire (Jour 3) : job d'évaluation automatisée, intégré au CI/CD.

Rejoue `data/reference/diabetes_reference.csv` (cas nominal) sur le modèle
candidat, calcule les métriques, et compare à celles du modèle actuellement
en Production dans MLflow. Doit détecter la dégradation simulée avec
`data/reference/diabetes_reference_drifted.csv` et bloquer la promotion
(quality gate) si le rappel chute au-delà du seuil défini.
"""


def main():
    # TODO : charger le modèle en Production depuis MLflow Registry
    # TODO : charger le jeu de référence, calculer les métriques
    # TODO : comparer au modèle actuellement en Production
    # TODO : exit code != 0 si dégradation au-delà du seuil (pour bloquer le CI/CD)
    raise NotImplementedError


if __name__ == "__main__":
    main()
