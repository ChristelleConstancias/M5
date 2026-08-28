"""À faire (Jour 2) : enregistrer heart_risk_model.pkl dans le MLflow
Model Registry (voir docker-compose.yml, service `mlflow`, déjà
pré-configuré) avec ses métriques et le passer en stage Production.
"""

import mlflow

MLFLOW_TRACKING_URI = "http://localhost:5000"


def main():
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    # TODO : mlflow.start_run(), log des métriques, mlflow.sklearn.log_model(),
    # puis promotion en stage "Production" via le Model Registry.
    raise NotImplementedError


if __name__ == "__main__":
    main()
