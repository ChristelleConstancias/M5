# Heart Risk — TP Module 5

Squelette de dépôt pour le brief `brief_m5.md`. Point de départ fourni : le
modèle entraîné (`heart_risk_model.pkl`), le notebook d'entraînement
(`notebooks/entrainement_modele.ipynb`), les jeux de données
(`data/raw`, `data/reference`) et un environnement MLflow pré-configuré
(`docker-compose.yml`, service `mlflow`).

## Démarrer

```bash
pip install -r requirements.txt
docker compose up mlflow   # tracking + registry, déjà configuré
```

MLflow UI : http://localhost:5000

## À compléter

- `src/` : préprocessing, prédiction, API FastAPI (Jour 1).
- `Dockerfile`, `docker-compose.yml` (service `api`) (Jour 1).
- `.github/workflows/ci-cd.yml` (Jour 2).
- `scripts/register_model.py` (Jour 2).
- `monitoring/dashboard.py`, `scripts/evaluate_model.py` (Jour 3).
- `docs/` : architecture, métriques de monitoring, revue périodique des indicateurs.

Voir `brief_m5.md` pour le détail des livrables et critères de performance.
