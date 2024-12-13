<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">PY-Music-Genre-Classifier</h3>

  <p>
    The <strong>PY-Music-Genre-Classifier</strong> predicts music genres based on audio features extracted from Spotify's API. The project uses supervised learning models such as CatBoost, LightGBM, and RandomForest to classify tracks into predefined genres.
    <br />
    <a href="https://github.com/moranenzo/PY-Music-Genre-Classifier"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#repository-structure">Repository Structure</a></li>
        <li><a href="#dataset-construction">Dataset Construction</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<h1 id="about-the-project">About the project</h1>

<p>
This project leverages Spotify's API to construct a dataset of audio features and track metadata for music genre classification. The pipeline includes automated data collection, preprocessing, and feature engineering. Supervised learning models such as CatBoost, LightGBM, and RandomForest are trained and evaluated using performance metrics like accuracy and F1-score, enabling accurate genre prediction.
</p>
<p> Key Features :
  <br />- Data preprocessing and feature engineering.
  <br />- Model training and evaluation.
  <br />- Genre prediction with an easy-to-use interface.
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
