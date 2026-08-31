# Diabetes Risk — TP Module 5

Squelette de dépôt pour le brief `brief_m5.md`. Point de départ fourni : le
modèle entraîné (`diabetes_risk_model.pkl`), le notebook d'entraînement
(`notebooks/entrainement_modele.ipynb`), les jeux de données
(`data/raw`, `data/reference`) et un environnement MLflow pré-configuré
(`docker-compose.yml`, service `mlflow`).

## Démarrer

```bash
pip install -r requirements.txt
docker compose up mlflow   # tracking + registry, déjà configuré
```

MLflow UI : http://localhost:5000

## À compléter, dans l'ordre du brief

- Jour 1 — `src/` (préprocessing, prédiction, API FastAPI) + `scripts/register_model.py` (tracking et versionnement MLflow).
- Jour 2 — `scripts/monitor_metrics.py` (recalcul des métriques, détection de dérive) + `monitoring/dashboard.py`.
- Jour 3 — `Dockerfile`, `docker-compose.yml` (service `api`), `.github/workflows/ci-cd.yml`, `scripts/evaluate_model.py` (quality gate).
- `docs/` : architecture, métriques de monitoring, revue périodique des indicateurs.

Voir `brief_m5.md` pour le détail des livrables et critères de performance.
