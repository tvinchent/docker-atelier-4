# Application Python avec PostgreSQL et pgAdmin via Docker

Cette application est un exemple simple d'interaction entre une application Python et une base de données PostgreSQL, en utilisant Docker pour gérer les services PostgreSQL et pgAdmin. L'application exécute des requêtes SQL de base comme la création de tables, l'insertion et la récupération de données.

## Installation

### Étape 1 : Cloner le projet

Clonez ce dépôt sur votre machine locale.

```
git clone https://github.com/tvinchent/docker-atelier-4
cd docker-atelier-4
```

### Étape 2 : Lancer l'appli dans docker

Un fichier docker-compose.yml est fourni pour lancer les services PostgreSQL et pgAdmin.

```
docker compose up
```

### Étape 3 : Executer l'appli Python

```
python .\app.py
```
