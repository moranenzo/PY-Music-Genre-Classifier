Prédiction du genre musical en utilisant les données de l'API Spotify.

---

### Semaine 1 : Collecte et Exploration des Données
1. **Objectif** : Récupérer et structurer les données, analyser les caractéristiques pour chaque genre, et explorer les relations entre les différentes caractéristiques et les genres.
   - [ ] Charger le dataset de 10 000+ chansons, et s'assurer que les informations nécessaires (track_id, features, genre) sont bien complètes.
   - [ ] Étudier la distribution des genres pour vérifier l’équilibre du dataset.
   - [ ] Analyser la répartition des caractéristiques Spotify (ex. danceability, energy, tempo) selon chaque genre pour identifier des patterns initiaux.

### Semaine 2 : Préparation des Données et Nettoyage
1. **Objectif** : Nettoyer les données et préparer les caractéristiques pour le modèle de machine learning.
   - [ ] Supprimer les colonnes inutiles pour la prédiction (par exemple, `track_name` ou `artist` si elles ne sont pas pertinentes).
   - [ ] Normaliser les valeurs numériques (ex. durée, loudness) pour harmoniser les échelles.
   - [ ] Transformer les genres en labels numériques pour la classification (ex. Rock = 0, Pop = 1, etc.).
   - [ ] Créer un fichier structuré (par ex. CSV ou DataFrame) avec les données prêtes pour l'entraînement.

### Semaine 3 : Analyse Exploratoire Avancée
1. **Objectif** : Comprendre les corrélations et explorer les groupes de genres par les caractéristiques.
   - [ ] Visualiser la corrélation entre les différentes caractéristiques (ex. danceability vs. energy, valence vs. tempo).
   - [ ] Tester différentes combinaisons de caractéristiques pour voir lesquelles sont potentiellement les plus distinctives pour chaque genre.
   - [ ] Rédiger des conclusions provisoires sur les relations trouvées entre les genres et les caractéristiques Spotify.

### Semaine 4 : Construction et Entraînement du Modèle
1. **Objectif** : Sélectionner et entraîner un modèle de classification pour prédire le genre musical.
   - [ ] Diviser les données en sets d’entraînement, de validation et de test (ex. 70%-15%-15%).
   - [ ] Choisir des modèles de classification de base comme la régression logistique, les arbres de décision, et les SVM.
   - [ ] Entraîner chaque modèle et évaluer leur performance initiale (précision, F1-score).
   - [ ] Tester les hyperparamètres de chaque modèle pour affiner les résultats.

### Semaine 5 : Amélioration et Validation du Modèle
1. **Objectif** : Optimiser les performances et évaluer la robustesse du modèle sélectionné.
   - [ ] Comparer les modèles de base et sélectionner le plus performant pour des réglages avancés.
   - [ ] Expérimenter avec des modèles plus complexes (ex. forêts aléatoires, réseaux de neurones).
   - [ ] Utiliser la validation croisée pour vérifier la stabilité des performances.
   - [ ] Documenter les résultats de chaque modèle et sélectionner le modèle final.

### Semaine 6 : Tests Finals et Présentation
1. **Objectif** : Préparer le projet final et communiquer les résultats.
   - [ ] Tester le modèle final sur le set de test et calculer les métriques définitives (précision, rappel, courbe ROC).
   - [ ] Évaluer et documenter les cas d’erreurs fréquentes (ex. genres confondus).
   - [ ] Créer une visualisation de résultats (ex. matrice de confusion, graphiques interactifs).
   - [ ] Rédiger un rapport final expliquant le processus et les résultats, et préparer la présentation.

--- 
