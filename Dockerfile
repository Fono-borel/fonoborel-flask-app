# Image officielle Python comme base
FROM python:3.9

# Répertoire de travail
WORKDIR /app

# Copie des fichiers
COPY app.py /app/
COPY requirements.txt /app/

# Installation des dépendances
RUN pip install -r requirements.txt

# Commande de lancement
CMD ["python", "app.py"]
