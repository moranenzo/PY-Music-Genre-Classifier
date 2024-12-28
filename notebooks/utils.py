import joblib  # used to save Scikit-learn models as .pkl
import s3fs
import pandas as pd
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.decomposition import PCA
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import time
import numpy as np
import os




def save_model(model, model_name="model", model_dir="../models/"):
    """
    Save the trained model based on its type.

    Parameters:
    - model: The trained model instance.
    - model_name: Name to save the model file.
    - model_dir: Directory where the model will be saved.
    """
    file_path = None

    # Save CatBoost model
    if "CatBoost" in str(type(model)):
        file_path = f"{model_dir}{model_name}.cbm"
        model.save_model(file_path)

    # Save XGBoost model
    elif "XGB" in str(type(model)):
        file_path = f"{model_dir}{model_name}.json"
        model.save_model(file_path)

    # Save LightGBM model
    elif "LGBM" in str(type(model)):
        file_path = f"{model_dir}{model_name}.txt"
        model.booster_.save_model(file_path)

    # Save Scikit-learn models
    elif hasattr(model, "predict"):
        file_path = f"{model_dir}{model_name}.pkl"
        joblib.dump(model, file_path)

    # Unsupported model type
    else:
        print("Error: Unsupported model type.")
        return

    print(f"Model saved at {file_path}")
    

fs = s3fs.S3FileSystem(client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"})


def get_df(file_path):
    """
    Reads a CSV file from a specified URL and returns it as a DataFrame.

    file_path ("/username/folder_name/file_name.csv") : path of the CSV file on ssp cloud.

    Returns:    pd.DataFrame: The DataFrame containing the data from the CSV file.

    Note:
    - The base URL is 'https://minio.lab.sspcloud.fr'.
    - Ensure that the file path provided is correct and accessible.
    - Requires the pandas library.
    """
    return pd.read_csv("https://minio.lab.sspcloud.fr" + file_path)

# from df_downloader import get_df



def count_outliers_zscore(df, threshold=3):
    """
    Compte le nombre d'outliers dans chaque colonne continue d'un DataFrame selon la méthode Z-Score.

    Parameters:
    - df (pd.DataFrame): Le DataFrame contenant les colonnes continues.
    - threshold (float): Seuil pour considérer une valeur comme outlier (par défaut : 3).

    Returns:
    - pd.Series: Série avec le nombre d'outliers pour chaque colonne.
    """
    outlier_counts = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):  # Vérifie que la colonne est numérique
            z_scores = zscore(df[column])
            outliers = np.abs(z_scores) > threshold
            outlier_counts[column] = np.sum(outliers)

    return pd.Series(outlier_counts)

def winsorize_outliers(df, columns, threshold=3):
    """
    Winsorise les valeurs aberrantes (outliers) dans les colonnes continues d'un DataFrame,
    sans modifier le DataFrame original.

    Parameters:
    - df (pd.DataFrame): DataFrame contenant les colonnes continues.
    - columns (list): Liste des colonnes à traiter.
    - threshold (float): Seuil z-score pour définir les outliers.

    Returns:
    - pd.DataFrame: Nouveau DataFrame avec les colonnes ajustées.
    """
    # Créer une copie du DataFrame pour ne pas modifier l'original
    df_copy = df.copy()

    for column in columns:
        z_scores = zscore(df_copy[column])
        
        # Calcul des limites
        lower_bound = df_copy[column][z_scores > -threshold].min()
        upper_bound = df_copy[column][z_scores < threshold].max()
        
        # Winsorisation
        df_copy[column] = np.clip(df_copy[column], lower_bound, upper_bound)
        
    return df_copy

def impute_with_linear_regression(df, target_column, predictors, test_size=0.2):
    clean_data = df[df[target_column].notna()]
    X = clean_data[predictors]
    y = clean_data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"{target_column} - MAE : {mae:.4f}, R^2 : {r2:.4f}")
    
def impute_with_random_forest(df, target_column, predictors, random_state=42):
    """
    Impute les valeurs manquantes d'une colonne avec un Random Forest Regressor.

    Arguments :
    - df : DataFrame pandas
    - target_column : Nom de la colonne cible à imputer
    - predictors : Liste des colonnes à utiliser comme prédicteurs
    - random_state : sert à la reproductibilité

    Retourne :
    - DataFrame avec les valeurs imputées pour la colonne cible
    """
    df_rf = df.copy()
    
    train_data = df_rf[df_rf[target_column].notna()]
    test_data = df_rf[df_rf[target_column].isna()]

    if test_data.empty:
        return df_rf

    X_train = train_data[predictors]
    y_train = train_data[target_column]

    X_test = test_data[predictors]

    rf_model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    rf_model.fit(X_train, y_train)

    predicted_values = rf_model.predict(X_test)

    df_rf.loc[df[target_column].isna(), target_column] = predicted_values

    return df_rf


def test_random_forest_imputation(df, target_column, predictors, missing_rate=0.2, random_state=42):
    """
    Teste la validité de l'imputation avec un Random Forest Regressor.

    Arguments :
    - df : DataFrame pandas original
    - target_column : Nom de la colonne cible
    - predictors : Liste des colonnes à utiliser comme prédicteurs
    - missing_rate : Proportion des données à masquer pour le test
    - random_state : Seed pour la reproductibilité

    Retourne :
    - MAE : Erreur absolue moyenne entre les vraies et les valeurs imputées
    - R^2 : Coefficient de détermination des valeurs imputées
    """
    np.random.seed(random_state)

    df_copy = df.copy()

    non_missing_indices = df_copy[target_column].dropna().index
    n_missing = int(missing_rate * len(non_missing_indices))
    missing_indices = np.random.choice(non_missing_indices, n_missing, replace=False)

    true_values = df_copy.loc[missing_indices, target_column]
    df_copy.loc[missing_indices, target_column] = np.nan

    df_rf = impute_with_random_forest(df_copy, target_column, predictors)

    imputed_values = df_rf.loc[missing_indices, target_column]

    mae = mean_absolute_error(true_values, imputed_values)
    r2 = r2_score(true_values, imputed_values)

    return mae, r2

def impute_with_xgboost(df, target_col, predictors, test_size=0.2, random_state=42):
    df_copy = df.copy()

    train_data = df_copy[df_copy[target_col].notna()]
    test_data = df_copy[df_copy[target_col].isna()]

    if test_data.empty:
        print(f"No missing values in {target_col}.")
        return df_copy, None

    X = train_data[predictors]
    y = train_data[target_col]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)

    xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=random_state)
    xgb_model.fit(X_train, y_train)

    X_test = test_data[predictors]
    y_pred = xgb_model.predict(X_test)

    df_copy.loc[test_data.index, target_col] = y_pred

    return df_copy, xgb_model

def evaluate_xgboost_model(df, model, target_col, predictors):
    """
    Évalue les performances du modèle XGBoost sur une colonne cible.
    Retourne la MAE et le R^2.
    """
    valid_data = df[df[target_col].notna()]
    X = valid_data[predictors]
    y_true = valid_data[target_col]
    
    y_pred = model.predict(X)
    
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    return mae, r2

def perform_PCA(df, continuous_vars, n_components=None):
    """
    Réalise une ACP sur les variables continues du DataFrame.
    Args:
        df (pd.DataFrame): DataFrame pandas
        continuous_vars (list): Liste des noms des colonnes continues
        n_components (int, optional): Nombre de composantes principales à conserver. 
                                      Par défaut, égal à len(continuous_vars).
    Returns:
        pd.DataFrame: DataFrame avec les composantes principales
        np.array: Variance expliquée par chaque composante principale
    """
    if n_components is None:
        n_components = len(continuous_vars)
    
    df_pca = df[continuous_vars]
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(df_pca)
    
    # Créer un DataFrame avec les composantes principales
    principal_df = pd.DataFrame(data=principal_components, 
                                columns=[f'PC{i+1}' for i in range(n_components)])
    
    # Afficher la variance expliquée par chaque composante principale
    components = pd.DataFrame(pca.components_, columns=df_pca.columns)
    explained_variance = pca.explained_variance_ratio_
    return principal_df, explained_variance, components

def get_importance_with_random_forest(df,target):
    """
    Calcule l'importance des variables avec un modèle Random Forest.
    Args:
        df (pd.DataFrame): DataFrame pandas
        features (list): Liste des noms des variables explicatives
        target (str): Nom de la variable cible
    Returns:
        pd.Series: Importance des variables
    """
    X = df.drop('target', axis=1)
    y = df['target_column']
    
    rf = RandomForestRegressor()
    rf.fit(X, y)
    
    importances = rf.feature_importances_
    feature_names = X.columns
    
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)
    
    return importance_df


# Initialize Spotify client
def spotify_client():
    """
    Initialize the Spotify API client with client credentials.
    Returns an authenticated Spotify client.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="c4536e618eac4bde8a40fb861828b092",
        client_secret="56deb037e3c54cc88e6071b30f6e5f18"
    ))
    
def fetch_artist_genre(track):
    """This function fetches the genre of an artist with a track from this artist, it will be 
    considerated as the genre of the song later

    Args:
        track a dict the countains infos about the track

    Returns: genre a string that is the genre of an artist
        
    """
    artist=track['artists'][0]['id']
    if spotify_client().artist(artist)['genres'] != []:
        return spotify_client().artist(artist)['genres'][0]
    else:
        return 'N/A'

# Fetch playlist tracks
def fetch_playlist_tracks(playlist_id):
    """
    Fetch all tracks from a Spotify playlist. 
    Params:
        -playlist_id: Spotify playlist ID.
    Returns a list of dictionaries containing track details.
    """
    tracks = []
    results = spotify_client().playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track:  # Ensure the track is not None
                tracks.append(track)
        time.sleep(0.1)
        results = spotify_client().next(results) if results['next'] else None
    return tracks

# Fetch detailed track information
def fetch_track_data(tracks):
    """
    Fetch metadata and audio features for each track in the playlist.
    Params:
        -tracks: List of tracks from the playlist.
    Returns a list of dictionaries containing track metadata and audio features.
    """
    track_data = []
    i=0
    for track in tracks:
        track_id = track['id']
        i+=1
        print(i)
        audio_features = spotify_client().audio_features([track_id])[0]
        genre=fetch_artist_genre(track)
        if audio_features:  # Ensure audio features are available
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track={"track Name": track['name'],
                "artists": artist_name,
                "track_id": track_id,
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'], 'genre': genre}
            for key in audio_features.keys():
                dict_track[key]=audio_features[key]
            track_data.append(dict_track)
    return track_data

# Save data to a CSV file
def save_to_csv(data, filename):
    """
    Save the list of track data to a CSV file.
    Params:
    :param data: List of dictionaries containing track details.
    :param filename: Output CSV file name.
    """
    keys = data[0].keys() if data else []
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


def get_playlists_data_to_csv(playlist_ids):
    """This function allows to fetch the data from different playlists into a csv 
    Params:
        - playlist_ids: a list of playlists we want to fetch our data from
    """
    names=[]
    track_data=[]
    file_name=''
    for playlist in playlist_ids: 
        print(f"Fetching playlist {playlist} tracks...")
        tracks = fetch_playlist_tracks(playlist)
        print("Fetching track data...")
        track_data+=(fetch_track_data(tracks))
    for id in playlist_ids:
        names.append(spotify_client().playlist(id)['name'])
    for name in names:
        file_name+=name+'+'
    file_name=file_name[:-1]
    print(file_name)
    if track_data:
        save_to_csv(track_data, f"playlists_{file_name}_data.csv")
    else:
        print("No data to save.")


def fetch_track_data_without_genre(tracks,genre):
    """
    Fetch metadata and audio features for each track in the playlist knowing the genre of the playlist
    Params:
        -tracks: List of tracks from the playlist.
    Returns a list of dictionaries containing track metadata and audio features.
    """
    track_data = []
    i=0
    for track in tracks:
        track_id = track['id']
        i+=1
        audio_features = spotify_client().audio_features([track_id])[0]
        if audio_features:  # Ensure audio features are available
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track={"track Name": track['name'],
                "artists": artist_name,
                "track_id": track_id,
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'], 'genre': genre}
            for key in audio_features.keys():
                dict_track[key]=audio_features[key]
            track_data.append(dict_track)
    return track_data

def get_playlists_data_to_csv_with_genre(playlist_ids):
    """This function allows to fetch the data from different playlists into a csv 
    Params:
        - playlist_ids: a dict whose keys are genres and values are playlists (strings)
    """
    names=[]
    track_data=[]
    file_name=''
    for key in playlist_ids.keys(): 
        print(f"Fetching playlist {playlist_ids[key]} tracks...")
        tracks = fetch_playlist_tracks(playlist_ids[key])
        print("Fetching track data...")
        track_data+=(fetch_track_data_without_genre(tracks, key))
    for key1 in playlist_ids.keys():
        names.append(spotify_client().playlist(playlist_ids[key1])['name'])
    for name in names:
        file_name+=name+'+'
    file_name=file_name[:-1]
    print(file_name)
    if track_data:
        save_to_csv(track_data, f"playlists_{file_name}_data.csv")
    else:
        print("No data to save.")

