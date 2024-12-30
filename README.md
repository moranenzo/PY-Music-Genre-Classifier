<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]



<!-- PROJECT BANNER -->
<br />
<div align="center">
  <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier">
    <img src="banner.png">
  </a>

<h1 align="center">PY-Music-Genre-Classifier</h3>

  <p>
    <strong>PY-Music-Genre-Classifier</strong> est un projet qui prédit les genres musicaux en analysant les caractéristiques audio des morceaux. En utilisant des modèles d'apprentissage supervisé tels que RandomForest, XGBoost et CatBoost, ce projet classe les chansons en fonction de leurs attributs sonores, offrant ainsi une approche automatisée pour catégoriser les genres musicaux de manière précise.
    <br />
    <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier"><strong>Explorer »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#about-the-project">À propos du projet</a>
      <ul>
        <li><a href="#repository-structure">Structure du repository</a></li>
        <li><a href="#dataset">Jeu de données</a></li>
        <li><a href="#built-with">Modèles utilisés</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Pour commencer</a>
      <ul>
        <li><a href="#prerequisites">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Utilisation</a></li>
    <li><a href="#contact">Contacts</a></li>
    <li><a href="#acknowledgments">Sources</a></li>
  </ol>
</details>



<h1 id="about-the-project">À propos du projet</h1>

<p>
Ce projet repose sur la construction d'un ensemble de données combinant les informations collectées via l'API de Spotify et un second jeu de données provenant de Kaggle. Ces données contiennent des caractéristiques audio et des métadonnées de morceaux, permettant ainsi de classifier des genres musicaux. Le pipeline inclut la collecte automatisée des données, le prétraitement, ainsi que l'ingénierie des caractéristiques. Des modèles d'apprentissage supervisé tels que RandomForest, XGBoost et CatBoost sont ensuite entraînés et évalués à l'aide de métriques de performance telles que l'accuracy et le score F1, afin de garantir une prédiction précise des genres musicaux.
</p>

<p> Fonctionnalités principales :
  <br />- Collecte des données via l'API Spotify.
  <br />- Prétraitement des données et ingénierie des caractéristiques.
  <br />- Entraînement et évaluation des modèles.
</p>



<h2 id="repository-structure">📁 Structure du Repository</h2>
<pre>
Music-Genre-Classifier/
├── notebooks/
│   ├── main.ipynb              # Notebook détaillé contenant toutes les fonctions utilisées
│   ├── simplified_main.ipynb   # Notebook allégé pour une lecture et une exécution plus rapide
│   └── utils.py                # Fonctions utiles et scripts partagés
├── src/
│   ├── data_collection.py      # Script d'import des données via l'API Spotify
│   ├── data_processing.py      # Nettoyage des données brutes
│   └── train_model.py          # Entraînement du modèle de ML
├── README.md
├── requirements.txt
└── .gitignore
</pre>


<h2 id="dataset">📊 Données</h2>
<p>Nous avons d'abord construit notre jeu de données à l'aide de l'API Spotify. Pour chaque morceau, nous avons récupéré les caractéristiques suivantes :</p>
<ul>
  <li><strong>Caractéristiques audio</strong> : danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo.</li>
  <li><strong>Métadonnées</strong> : nom du morceau, artiste, popularité, drapeau explicite, durée (ms), signature temporelle, étiquette de genre.</li>
</ul>
<p>Les appels à l'API ont été automatisés et les données ont été enregistrées au format CSV.</p>
<p>Cependant comme expliqué dans les notebooks, un <a href="https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api">changement dans la politique de Spotify</a> apparu fin Novembre 2024 nous a empeché de terminer la construction de notre dataset. Voilà pourquoi nous utilisons dans les parties data-preprocessing, feature-engineering et train-model les données issues d'un <a href="https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs">dataframe Kaggle</a> collectées quelques années auparavant de la même manière que nous avons pu mettre en place.
  </p>



<h2 id="machine-learning-approach">📈 Approche Machine Learning</h2>
<p>Nous avons expérimenté avec plusieurs modèles de machine learning :</p>
<ul>
  <li><strong>Prétraitement des données</strong> : Gestion des valeurs manquantes, standardisation des variables numériques et encodage des données catégorielles.</li>
  <li><strong>Modèles utilisés</strong> :
    <ul>
      <li>RandomForest</li>
      <li>XGBoost</li>
      <li>CatBoost</li>
    </ul>
  </li>
  <li><strong>Métriques d'évaluation</strong> : Accuracy, Précision, Rappel, Score F1.</li>
</ul>



<h2 id="built-with">🛠️ Conçu avec</h2>
<ul>
  <li>Python 3</li>
  <li>Pandas</li>
  <li>Scikit-Learn</li>
  <li>CatBoost</li>
  <li>XGBoost</li>
</ul>




<h1 id="getting-started">🚀 Pour commencer</h1>
<p>Suivez ces étapes pour configurer le projet en local :</p>

<h3 id="prerequisites">⚙️ Prérequis</h3>
<ul>
  <li>Python 3.x installé</li>
  <li>Bibliothèques nécessaires :
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ul>



<h3 id="installation">💻 Installation</h3>
<ol>
  <li>Clonez le dépôt :
    <pre><code>git clone https://github.com/moranenzo/PY-Music-Genre-Classifier.git</code></pre>
  </li>
  <li>Accédez au répertoire du projet :
    <pre><code>cd PY-Music-Genre-Classifier</code></pre>
  </li>
</ol>



<h1 id="usage">⚡ Utilisation</h1>
<p>Exécutez la commande suivante pour entraîner le modèle <i>(CatBoost par défaut)</i>:</p>
<pre><code>python src/train_model.py</code></pre>

<p>Exécutez la commande suivante pour évaluer le modèle :</p>
<pre><code>python src/evaluate_model.py</code></pre>





<h1 id="contact">📞 Contact</h1>
<ul>
  <li><strong>Enzo MORAN</strong> - <a href="https://www.linkedin.com/in/moranenzo/" target="_blank">LinkedIn</a> - <a href="mailto:enzo.moran@ensae.fr">enzo.moran@ensae.fr</a></li>
  <li><strong>Martin CONTE</strong> - <a href="https://www.linkedin.com/in/martin-conte-7a3139286/" target="_blank">LinkedIn</a> - <a href="mailto:martin_conte@ensae.fr">martin_conte@ensae.fr</a></li>
  <li><strong>Tom LAFLOTTE</strong> - <a href="https://www.linkedin.com/in/tom-laflotte-19a351293/" target="_blank">LinkedIn</a> - <a href="mailto:tom.laflotte@ensae.fr">tom.laflotte@ensae.fr</a></li>
</ul>

<p>Projet : <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier" target="_blank">https://github.com/moranenzo/PY-Music-Genre-Classifier</a></p>




<h1 id="acknowledgments">📚 Sources</h1>
<ul>
  <li><a href="https://developer.spotify.com/documentation/web-api/" target="_blank">Documentation de l'API Spotify</a></li>
  <li><a href="https://contrib.rocks" target="_blank">Contrib.rocks</a></li>
  <li><a href="https://docs.python.org/3/" target="_blank">Documentation Python</a></li>
</ul>

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/moranenzo/PY-Music-Genre-Classifier.svg?style=for-the-badge
[contributors-url]: https://github.com/moranenzo/PY-Music-Genre-Classifier/graphs/contributors
[product-screenshot]: images/screenshot.png
