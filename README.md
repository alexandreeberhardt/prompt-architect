# Image Prompt Architect

Ce projet met à disposition une interface utilisateur web permettant de transformer des descriptions d'images vagues ou incomplètes en **spécifications JSON structurées et détaillées**. L'objectif est de faciliter la création de prompts complexes pour les générateurs d'images par IA (Midjourney, DALL-E 3, Stable Diffusion).

L'application utilise l'API d'OpenAI (modèle **GPT-4o**) pour agir comme un "Architecte de Prompt", extrapolant de manière cohérente les détails manquants (éclairage, angle de caméra, style, matériaux) tout en respectant strictement les contraintes de l'utilisateur.

## Fonctionnalités

* **Architecture de Prompt :** Conversion d'une idée simple en un objet JSON complet (`subject`, `lighting`, `camera`, `style`, etc.).
* **Extrapolation Intelligente :** Le système invente les détails manquants (ex: type de lentille, ambiance atmosphérique) pour garantir un rendu visuel riche.
* **Sortie JSON Standardisée :** Format strict prêt pour l'automatisation ou l'intégration dans des pipelines de génération.
* **Interface Web :** Interface intuitive développée avec Streamlit pour saisir sa description, visualiser le JSON et télécharger le résultat.
* **Déploiement conteneurisé :** Support complet pour Docker et Docker Compose.

## Démonstration en ligne

Une version de démonstration de l’application est accessible à l’adresse suivante :  
https://prompt.alexeber.fr

## Prérequis techniques

* Docker et Docker Compose (recommandé).
* Une clé API OpenAI valide (accès à GPT-4o requis).
* Python 3.11 (si exécution locale sans Docker).

## Installation et Démarrage

### Utilisation avec Docker (Recommandé)

Le projet inclut un fichier `docker-compose.yml` pour un déploiement rapide.

1.  **Configuration de l'environnement :**
    Créez un fichier `.env` à la racine du projet contenant votre clé API :
    ```bash
    OPENAI_API_KEY=sk-votre_cle_api_ici
    ```

2.  **Lancement du service :**
    Exécutez la commande suivante à la racine du projet :
    ```bash
    docker-compose up -d --build
    ```
    L'application sera accessible sur le port **8501**.

3.  **Accès à l'application :**
    Ouvrez votre navigateur et accédez à l'adresse : `http://localhost:8501`.

### Installation Locale (Sans Docker)

1.  **Installation des dépendances :**
    Il est recommandé d'utiliser un environnement virtuel. Installez les paquets requis :
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration de la clé API :**
    Créez un fichier `.env` à la racine ou exportez la variable dans votre terminal :
    ```bash
    export OPENAI_API_KEY=sk-votre_cle_api_ici
    ```

3.  **Lancement de l'application :**
    Démarrez le serveur Streamlit :
    ```bash
    streamlit run app.py
    ```

## Structure du Projet

* `app.py` : Point d'entrée de l'application Streamlit. Gère l'interface utilisateur.
* `nano_prompt.py` : Cœur du système. Contient le "System Prompt" d'architecture, l'appel à l'API OpenAI et la logique de nettoyage des noms de fichiers.
* `Dockerfile` : Configuration pour la construction de l'image Docker (basée sur Python 3.11-slim).
* `docker-compose.yml` : Orchestration du conteneur.
* `requirements.txt` : Liste des dépendances Python (Streamlit, OpenAI, Python-dotenv, etc.).

## Utilisation

1.  Lancez l'application.
2.  Entrez une description (ex: *"Un chat cyberpunk sous la pluie"*).
3.  Cliquez sur **"Générer la structure JSON"**.
4.  L'application affiche le JSON généré et propose un téléchargement.
5.  Utilisez ce JSON pour configurer vos outils de génération d'images.

## Auteur

Développé par Alexandre Eberhardt.

## Licence

Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.
