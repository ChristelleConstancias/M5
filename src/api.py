"""API FastAPI exposant le modèle de risque de crise cardiaque.

À faire (Jour 1) :
    - POST /predict  : reçoit un profil patient, retourne la prédiction.
    - GET  /health    : statut de l'API (pour le healthcheck Docker/CI).
    - GET  /model/info : version et métriques du modèle chargé.
"""

from fastapi import FastAPI

app = FastAPI(title="Heart Risk API")


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
