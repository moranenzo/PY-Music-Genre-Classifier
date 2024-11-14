### Semaine 1 : Collecte et Exploration des Données

1. **Configuration de l'environnement de travail**
   - [ ] Installer toutes les bibliothèques nécessaires pour la gestion des données (par exemple, pandas, numpy) et la visualisation (matplotlib, seaborn).
   - [ ] Créer une structure initiale de votre repository GitHub avec des dossiers pour les scripts (`src`), les données (`data`), et les notebooks d'exploration (`notebooks`).

2. **Chargement des données et premières vérifications**
   - [ ] Charger le dataset de 10 000 chansons avec leurs caractéristiques via l'API Spotify ou depuis une source de données existante.
   - [ ] Vérifier l'intégrité des données : s'assurer qu'il n'y a pas de valeurs manquantes, notamment dans les colonnes critiques (track_id, genre, caractéristiques audio).
   - [ ] Analyser la répartition des genres dans le dataset pour s’assurer que les données sont suffisamment équilibrées. Si un genre est sous-représenté, envisager des techniques de rééquilibrage (oversampling, undersampling).

3. **Exploration des caractéristiques de Spotify**
   - [ ] Visualiser la distribution de chaque caractéristique Spotify (par exemple, `danceability`, `energy`, `loudness`) pour mieux comprendre leurs valeurs typiques et repérer d’éventuelles anomalies.
   - [ ] Pour chaque caractéristique, calculer les statistiques descriptives (moyenne, médiane, écart-type) afin de comprendre les valeurs centrales et la variabilité.

4. **Analyse de la répartition des genres par caractéristiques**
   - [ ] Créer des visualisations (par exemple, boxplots, histogrammes) pour observer comment certaines caractéristiques varient en fonction des genres. Par exemple :
     - Un boxplot pour `energy` en fonction du genre pour voir si les genres dynamiques comme le rock ou la techno ont des valeurs d’énergie élevées.
     - Un histogramme pour `tempo` pour comparer des genres avec des tempos typiquement rapides ou lents.
   - [ ] Identifier des caractéristiques clés qui semblent différencier les genres les plus éloignés (ex. `acousticness` pour différencier la musique acoustique du rock ou de la techno).

5. **Préparer une liste de caractéristiques pertinentes**
   - [ ] Sur la base des observations, sélectionner les caractéristiques qui semblent avoir un potentiel discriminant pour la prédiction de genres (par exemple, `danceability`, `energy`, `acousticness`, `valence`).
   - [ ] Noter les caractéristiques à évaluer plus en profondeur lors de l’entraînement du modèle.

6. **Documentation et conclusion de l'exploration**
   - [ ] Rédiger un rapport préliminaire sur vos premières observations : quelles caractéristiques pourraient être les plus utiles pour prédire les genres ? Quelles tendances et relations avez-vous identifiées ?
   - [ ] Discuter avec l’équipe des résultats initiaux pour décider si des ajustements sont nécessaires dans la préparation des données pour la suite du projet.

---
