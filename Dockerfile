# Image de base
FROM python:3.14-slim

# Répertoire de travail
WORKDIR /app

# Copie des dépendances
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Port exposé
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]