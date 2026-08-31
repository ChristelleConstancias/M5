# Données — TP Module 5

- `raw/diabetes_train.csv` : dataset d'entraînement (700 profils patients), utilisé par la data scientist dans `notebooks/entrainement_modele.ipynb` pour produire `diabetes_risk_model.pkl`.
- `raw/training_metrics.json` : métriques du modèle sur son jeu de test interne (accuracy, recall, f1, auc), à titre de référence pour le tracking MLflow (Jour 1).
- `reference/diabetes_reference.csv` : jeu de référence labellisé (200 profils, même distribution que l'entraînement), à utiliser pour le monitoring et le job d'évaluation automatisée (cas nominal — les métriques doivent rester stables, le quality gate doit laisser passer).
- `reference/diabetes_reference_drifted.csv` : même format, mais population décalée (patients plus âgés, glycémie/tension/IMC plus élevés, davantage de cas positifs). À utiliser pour simuler une dérive de données et vérifier que le monitoring la détecte, et que le CI/CD bloque la promotion.

## Dictionnaire des colonnes

| Colonne | Description |
|---|---|
| pregnancies | Nombre de grossesses |
| glucose | Glycémie plasmatique (test de tolérance au glucose) |
| blood_pressure | Tension artérielle diastolique (mm Hg) |
| skin_thickness | Épaisseur du pli cutané tricipital (mm) |
| insulin | Insuline sérique à 2h (mu U/ml) |
| bmi | Indice de masse corporelle |
| diabetes_pedigree | Fonction pedigree du diabète (facteur héréditaire) |
| age | Âge du patient |
| outcome | 1 = risque de diabète présent, 0 = absent |
