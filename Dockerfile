# À compléter au Jour 3.
# Squelette minimal : à ajuster (port, commande de démarrage, copie du modèle).

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# TODO : exposer le bon port et lancer uvicorn sur src.api:app
EXPOSE 8000
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
