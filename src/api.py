"""API FastAPI exposant le modèle de risque de diabète.

À faire (Jour 1) :
    - POST /predict  : reçoit un profil patient, retourne la prédiction.
    - GET  /health    : statut de l'API (pour le healthcheck Docker/CI).
    - GET  /model/info : version, stage et métriques du modèle chargé
      depuis le MLflow Model Registry.
"""

from fastapi import FastAPI

app = FastAPI(title="Diabetes Risk API")


@app.get("/health")
def health():
    # TODO
    raise NotImplementedError


@app.get("/model/info")
def model_info():
    # TODO
    raise NotImplementedError


@app.post("/predict")
def predict_endpoint():
    # TODO : valider l'entrée avec un schéma Pydantic, appeler src.predict
    raise NotImplementedError
