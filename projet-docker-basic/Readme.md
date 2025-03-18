# Basic Docker Project

## Description
Ce projet met en place un serveur HTTP minimaliste en Python, exécuté dans un conteneur Docker. Il utilise uniquement les bibliothèques standards de Python et ne repose sur aucun framework.

## Structure du projet
```
basic-docker-project/
├── app/
│   ├── server.py          # Serveur HTTP en Python
├── Dockerfile             # Instructions pour créer l'image Docker
├── docker-compose.yml     # Configuration pour Docker Compose
└── README.md              # Documentation du projet
```

## Prérequis
- **Docker** installé sur votre machine.
- **(Optionnel)** Docker Compose pour une exécution simplifiée.

## Instructions

### Exécution avec Docker
1. **Construire l’image Docker** :
   ```sh
   docker build -t basic-http-server .
   ```
2. **Exécuter le conteneur** :
   ```sh
   docker run -p 8000:8000 basic-http-server
   ```
3. **Tester l’application** :
   Ouvrir un navigateur et aller sur [http://localhost:8000](http://localhost:8000).

### Exécution avec Docker Compose
1. **Lancer l’application avec une seule commande** :
   ```sh
   docker-compose up --build
   ```
2. **Tester l’application** sur [http://localhost:8000](http://localhost:8000).

### Exécution sans Docker (Mode classique)
1. **Installer Python (>=3.9)**.
2. **Lancer le serveur** :
   ```sh
   python app/server.py
   ```
3. **Accéder à l’application** sur [http://localhost:8000](http://localhost:8000).

## Vérification du serveur
Vous pouvez tester le serveur avec `curl` :
```sh
curl http://localhost:8000
```
Cela doit renvoyer :
```html
<html><body><h1>Hello, Docker!</h1></body></html>
```

## Arrêter l'application
- Si vous avez utilisé `docker run`, arrêtez-le avec **CTRL+C**.
- Si vous avez utilisé `docker-compose`, arrêtez-le avec :
  ```sh
  docker-compose down
  ```



