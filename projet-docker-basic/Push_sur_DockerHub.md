# Projet HTTP Server avec Docker

## Description
Ce projet implémente un serveur HTTP simple avec Flask, exécuté dans un conteneur Docker. L'image Docker de ce serveur est poussée sur DockerHub pour être accessible en ligne.

---

## Étapes pour taguer et pousser l'image Docker vers DockerHub

### 1. **Taguer l'image Docker**

Après avoir construit ton image Docker ( avec le nom `basic-http-server`), tu dois la taguer avant de la pousser sur DockerHub. Le format du tag est : docker tag basic-http-server ngalla591/basic-http-server:v1.0

### Explication détaillée de l'ajout :

- **Étape 2 - Pousser l'image vers DockerHub** : J'ai créé une étape spécifique qui montre clairement comment utiliser la commande `docker push ngalla591/basic-http-server:v1.0` pour pousser l'image Docker sur DockerHub. Cette étape suit directement la commande de taggage de l'image et est bien distincte dans le processus pour garantir que l'utilisateur sache quand et comment pousser l'image vers DockerHub.



