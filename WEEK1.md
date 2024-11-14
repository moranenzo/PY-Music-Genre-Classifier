1. **Jour 1 : Choix des genres et recherche de datasets**
   - [ ] Discuter avec l'équipe pour sélectionner 5 à 7 genres de musique à cibler (ex. rock, rap, pop, jazz, country).
   - [ ] Rechercher des datasets contenant des paroles étiquetées par genre (ex. Million Song Dataset, Genius Lyrics, GTZAN).
   - [ ] Identifier des API de collecte de paroles (ex. Genius, Musixmatch) en cas de besoin supplémentaire.

2. **Jour 2 : Téléchargement et structuration des données**
   - [ ] Télécharger le dataset ou configurer une API pour récupérer les paroles.
   - [ ] Organiser les fichiers dans des dossiers séparés par genre.
   - [ ] Créer un script pour automatiser la collecte des paroles, si nécessaire, et collecter environ 500-1000 chansons par genre.

3. **Jour 3 : Nettoyage initial des données**
   - [ ] Créer un script pour normaliser les caractères (tout en minuscules).
   - [ ] Supprimer la ponctuation et les caractères spéciaux.
   - [ ] Tokeniser les paroles (transformer les chansons en liste de mots).
   - [ ] Supprimer les stop words (mots peu informatifs) avec une liste adaptée à la langue choisie (anglais ou français).

4. **Jour 4 : Structuration et sauvegarde des données nettoyées**
   - [ ] Enregistrer les données nettoyées dans un format structuré (CSV ou JSON) avec colonnes : **genre**, **paroles nettoyées**, et **titre** (optionnel).
   - [ ] Consolider le dataset nettoyé pour chaque genre en un seul fichier pour faciliter les manipulations ultérieures.

5. **Jour 5 : Analyse préliminaire des données**
   - [ ] Analyser la distribution des chansons par genre pour vérifier l’équilibre entre les catégories.
   - [ ] Rechercher les doublons ou incohérences dans les données.
   - [ ] Documenter toutes les observations ou problèmes rencontrés dans un fichier texte pour référence future.

6. **Jour 6 : Planification de la pipeline NLP**
   - [ ] Décider des étapes de transformation des paroles en données numériques (ex. vectorisation avec TF-IDF ou Word2Vec).
   - [ ] Identifier les outils/bibliothèques nécessaires (ex. NLTK, spaCy) pour le traitement NLP.
   - [ ] Créer un plan structuré de pipeline pour le traitement des données textuelles.

7. **Jour 7 : Validation des données et documentation**
   - [ ] Vérifier manuellement un échantillon de données pour s’assurer que le nettoyage et l'étiquetage sont corrects.
   - [ ] Rédiger un fichier `README.md` pour documenter la structure du dataset et les étapes de pré-traitement.
   - [ ] Archiver tous les scripts de nettoyage dans le répertoire du projet.
