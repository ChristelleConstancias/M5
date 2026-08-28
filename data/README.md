# Données — TP Module 5

- `raw/heart_train.csv` : dataset d'entraînement (700 profils patients), utilisé par la data scientist dans `notebooks/entrainement_modele.ipynb` pour produire `heart_risk_model.pkl`.
- `raw/training_metrics.json` : métriques du modèle sur son jeu de test interne (accuracy, recall, f1, auc), à titre de référence pour le Jour 2 (versionnement dans MLflow/DVC).
- `reference/heart_reference.csv` : jeu de référence labellisé (200 profils, même distribution que l'entraînement), à utiliser pour le job d'évaluation automatisée du Jour 3 (cas nominal — le quality gate doit laisser passer).
- `reference/heart_reference_drifted.csv` : même format, mais population décalée (patients plus âgés, tension et cholestérol plus élevés, davantage de cas positifs). À utiliser en Jour 3 pour simuler une dérive et vérifier que le job d'évaluation détecte la dégradation et bloque la promotion.

## Dictionnaire des colonnes

| Colonne | Description |
|---|---|
| age | Âge du patient |
| sex | Sexe (1 = homme, 0 = femme) |
| cp | Type de douleur thoracique (0-3) |
| trestbps | Tension artérielle au repos (mm Hg) |
| chol | Cholestérol sérique (mg/dl) |
| fbs | Glycémie à jeun > 120 mg/dl (1 = oui) |
| restecg | Résultat ECG au repos (0-2) |
| thalach | Fréquence cardiaque maximale atteinte |
| exang | Angine induite par l'effort (1 = oui) |
| oldpeak | Dépression du segment ST induite par l'effort |
| slope | Pente du segment ST à l'effort (0-2) |
| ca | Nombre de vaisseaux principaux colorés (0-3) |
| thal | Thalassémie (1 = normal, 2 = défaut fixe, 3 = défaut réversible) |
| target | 1 = risque de crise cardiaque présent, 0 = absent |
