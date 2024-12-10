<h1> PY-project </h1>
<p>deadline : Dimanche 29 Décembre à 23h59</p>
<p>soutenances : Vendredi 10 Janvier</p>
<p>https://pythonds.linogaliana.fr/content/annexes/evaluation.html</p>

<h2>Project Structure</h2>
<pre>
Genre-Detection-with-Spotify-API/
├── notebooks/
│   ├── 01_data_collection.ipynb        # Notebook for data collection via the Spotify API
│   ├── 02_data_cleaning.ipynb          # Notebook for cleaning and preprocessing the data
│   ├── 03_feature_exploration.ipynb    # Notebook for exploratory data analysis of features
│   ├── 04_model_training.ipynb         # Notebook for training classification models
│   └── 05_model_evaluation.ipynb       # Notebook for evaluating and visualizing model performance
├── src/
│   ├── data_collection.py         # Script to collect data from the Spotify API
│   ├── data_preprocessing.py      # Script for cleaning and preprocessing the data
│   ├── feature_engineering.py     # Script for feature creation and selection
│   ├── model_training.py          # Script for training and saving the models
│   ├── model_evaluation.py        # Script for evaluation and performance metrics
│   └── utils.py                   # Utility functions (e.g., data loading, metrics, etc.)
├── models/
│   └── trained_genre_model.pkl    # Saved trained genre classification model
├── reports/
│   ├── figures/                   # Graphs and visualizations from analysis and results
│   └── final_report.md            # Final report with methodology, results, and conclusions
├── tests/
│   ├── test_data_collection.py    # Unit tests for data collection
│   ├── test_data_preprocessing.py # Unit tests for data preprocessing
│   ├── test_model_training.py     # Unit tests for model training
│   └── test_model_evaluation.py   # Unit tests for model evaluation
├── models/                   # Saved trained models (if relevant)
├── results/                  # Results and generated figures
├── README.md                 # Project description
├── requirements.txt          # Dependencies (s3fs, pandas, sklearn, etc.)
└── .gitignore                # Files to ignore (notebooks, models, raw data)
</pre>

<h2>Data</h2>
<pre>
  The data frame we worked on, has been created by ourselves thanks to the api spotify. You can download it by using src/df_downloader.py
</pre>
