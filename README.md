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
    <strong>PY-Music-Genre-Classifier</strong> permet de prédire les genres musicaux en se basant sur les caractéristiques audio. Le projet utilise des modèles d'apprentissage supervisé tels que CatBoost, LightGBM et RandomForest pour classer les morceaux dans des genres prédéfinis.
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
        <li><a href="#dataset-construction">Construction du jeu de données</a></li>
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
    <li><a href="#acknowledgments">Remerciements</a></li>
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



<h2 id="repository-structure">📁 Repository Structure</h2>
<pre>
Music-Genre-Classifier/
├── data/                     # Dossier contenant les jeux de données (si possible, exclure les fichiers lourds du repo)
├── notebooks/                # Notebooks Jupyter pour exploration et visualisation
│   └── data_processing.ipynb
├── src/                      # Code source
│   ├── import_data.py        # Script d'import des données via l'API Spotify
│   ├── train_model.py        # Entraînement du modèle de ML
│   └── utils.py              # Fonctions utiles et scripts partagés
├── models/                   # Sauvegardes des modèles entraînés (si pertinent)
├── results/                  # Résultats et figures générées
├── README.md                 # Description du projet
├── requirements.txt          # Dépendances (s3fs, pandas, sklearn, etc.)
└── .gitignore                # Fichiers à ignorer (notebooks, modèles, données brutes)
</pre>


<h2 id="dataset-construction">Dataset Construction</h2>
<p>We constructed our dataset using Spotify's API. For each track, we retrieved the following features:</p>
<ul>
  <li><strong>Audio Features</strong>: danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo.</li>
  <li><strong>Metadata</strong>: track name, artist, popularity, explicit flag, duration (ms), time signature, genre label.</li>
</ul>
<p>The API calls were automated and stored in CSV format.</p>


<h2 id="machine-learning-approach">Machine Learning Approach</h2>
<p>We experimented with several machine learning models:</p>
<ul>
  <li><strong>Data Preprocessing</strong>: Handled missing values, scaled numerical features, and encoded categorical data.</li>
  <li><strong>Models Used</strong>:
    <ul>
      <li>CatBoost</li>
      <li>LightGBM</li>
      <li>RandomForest</li>
    </ul>
  </li>
  <li><strong>Evaluation Metrics</strong>: Accuracy, Precision, Recall, F1-Score.</li>
</ul>


<h2 id="built-with">Built With</h2>
<ul>
  <li>Python 3</li>
  <li>Pandas</li>
  <li>Scikit-Learn</li>
  <li>CatBoost</li>
  <li>LightGBM</li>
</ul>



<h1 id="getting-started">Getting Started</h1>
<p>Follow these steps to set up the project locally:</p>

<h3 id="prerequisites">Prerequisites</h3>
<ul>
  <li>Python 3.x installed</li>
  <li>Required libraries:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ul>


<h3 id="installation">Installation</h3>
<ol>
  <li>Clone the repo:
    <pre><code>git clone https://github.com/moranenzo/PY-Music-Genre-Classifier.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd PY-Music-Genre-Classifier</code></pre>
  </li>
  <li>Set up the Spotify API (if applicable):
    <ul>
      <li>Create an API key <a href="https://developer.spotify.com/" target="_blank">here</a>.</li>
      <li>Add it to a .env file in the project root.</li>
    </ul>
  </li>
</ol>


<h1 id="usage">Usage</h1>
<p>Run the following command to train the model:</p>
<pre><code>python src/train_model.py</code></pre>

<p>Run the following command to evaluate the model:</p>
<pre><code>python src/evaluate_model.py</code></pre>

<p><em>For more examples, please refer to the <strong><a href="https://github.com/moranenzo/PY-Music-Genre-Classifier/docs" target="_blank">Documentation</a></strong></em></p>



<h1 id"contact">Contact</h1>
<ul>
  <li><strong>Enzo MORAN</strong> - <a href="https://www.linkedin.com/in/moranenzo/" target="_blank">LinkedIn</a> - <a href="mailto:enzo.moran@ensae.fr">enzo.moran@ensae.fr</a></li>
  <li><strong>Martin CONTE</strong> - <a href="https://www.linkedin.com/in/martin-conte-7a3139286/" target="_blank">LinkedIn</a> - <a href="mailto:martin_conte@ensae.fr">martin_conte@ensae.fr</a></li>
  <li><strong>Tom LAFLOTTE</strong> - <a href="https://www.linkedin.com/in/tom-laflotte-19a351293/" target="_blank">LinkedIn</a> - <a href="mailto:tom.laflotte@ensae.fr">tom.laflotte@ensae.fr</a></li>
</ul>

<p>Project Link: <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier" target="_blank">https://github.com/moranenzo/PY-Music-Genre-Classifier</a></p>



<h1 id="acknowledgments">Acknowledgments</h1>
<ul>
  <li><a href="https://developer.spotify.com/documentation/web-api/" target="_blank">Spotify API Documentation</a></li>
  <li><a href="https://contrib.rocks" target="_blank">Contrib.rocks</a></li>
  <li><a href="https://docs.python.org/3/" target="_blank">Python Documentation</a></li>
</ul>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/moranenzo/PY-Music-Genre-Classifier.svg?style=for-the-badge
[contributors-url]: https://github.com/moranenzo/PY-Music-Genre-Classifier/graphs/contributors
[product-screenshot]: images/screenshot.png
