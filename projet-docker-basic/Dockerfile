# Utilisation de l'image Python légère
FROM python:3.9.12-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier serveur dans le conteneur
COPY app/server.py .

# Exposer le port 8000 pour accéder au serveur
EXPOSE 8000

# Démarrer le serveur HTTP
CMD ["python", "server.py"]
