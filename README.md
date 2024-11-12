<h1> PY-project </h1>
<p>deadline : Dimanche 29 Décembre à 23h59</p>
<p>soutenances : Vendredi 10 Janvier</p>
<p>https://pythonds.linogaliana.fr/content/annexes/evaluation.html</p>

<h2>Project Structure</h2>
<pre>
Emotion-Detection-In-Lyrics/
├── README.md
├── data/
│   ├── raw/                   # Contient les fichiers bruts de paroles avant traitement
│   ├── processed/             # Données nettoyées et structurées prêtes pour la modélisation
│   └── lexicons/              # Lexiques spécifiques d’émotions (ex. NRC Emotion Lexicon)
├── notebooks/
│   ├── 01_data_collection.ipynb       # Notebook pour la collecte de données de paroles
│   ├── 02_data_cleaning.ipynb         # Notebook pour le nettoyage et la préparation des données
│   ├── 03_exploratory_analysis.ipynb  # Notebook pour l'analyse exploratoire des paroles
│   ├── 04_model_training.ipynb        # Notebook pour l'entraînement des modèles de machine learning
│   └── 05_model_evaluation.ipynb      # Notebook pour l’évaluation du modèle et les tests finaux
├── src/
│   ├── data_preprocessing.py    # Scripts pour le nettoyage et le prétraitement des paroles
│   ├── emotion_lexicon.py       # Scripts pour gérer le lexique des émotions
│   ├── model_training.py        # Scripts pour l’entraînement et la sauvegarde du modèle
│   ├── model_evaluation.py      # Scripts pour l’évaluation du modèle
│   └── utils.py                 # Fonctions utilitaires (ex. chargement de données, métriques)
├── models/
│   └── trained_model.pkl        # Fichier du modèle entraîné sauvegardé
├── reports/
│   ├── figures/                 # Graphiques et visualisations des résultats d’analyse
│   └── final_report.md          # Rapport final avec explication de la méthodologie, résultats et conclusions
├── tests/
│   ├── test_data_preprocessing.py    # Tests unitaires pour le prétraitement de données
│   ├── test_model_training.py        # Tests unitaires pour l’entraînement de modèle
│   └── test_model_evaluation.py      # Tests unitaires pour l’évaluation du modèle
└── requirements.txt
</pre>