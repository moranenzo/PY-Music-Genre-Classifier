# Importation des librairies
import pandas as pd

from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

file_path = "/tlaflotte/genre_detector/spotify_tracks.csv"



# Téléchargement de la base de données
df = pd.read_csv("https://minio.lab.sspcloud.fr" + file_path)


# Colonnes à modifier
columns_to_drop = ["track_name","track_id","track_artist","track_album_id","track_album_name","track_album_release_date", "playlist_name", "playlist_id","track_popularity", "playlist_subgenre"]

columns_to_winsorize = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo', 'duration_ms']

columns_to_standardize = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

predictors = [ 'speechiness', 'instrumentalness', 'energy', 'danceability', 'acousticness', 'tempo', 'duration_ms', 'loudness', 'key', 'mode']


# Winsorisation
def winsorize_outliers(df, columns, threshold=3):
    """
    Winsorise les valeurs aberrantes (outliers) dans les colonnes continues d'un DataFrame.

    Parameters:
    - df (pd.DataFrame): DataFrame contenant les colonnes continues.
    - columns (list): Liste des colonnes à traiter.
    - threshold (float): Seuil z-score pour définir les outliers.

    Returns:
    - pd.DataFrame: Nouveau DataFrame avec les colonnes ajustées.
    """
    for column in columns:
        z_scores = zscore(df_copy[column])
        
        # Calcul des limites
        lower_bound = df[column][z_scores > -threshold].min()
        upper_bound = df[column][z_scores < threshold].max()
        
        # Winsorisation
        df[column] = np.clip(df[column], lower_bound, upper_bound)


# Remplissage des NaN
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
    train_data = df[df[target_column].notna()]
    test_data = df[df[target_column].isna()]

    if test_data.empty:
        return df

    X_train = train_data[predictors]
    y_train = train_data[target_column]

    X_test = test_data[predictors]

    rf_model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    rf_model.fit(X_train, y_train)

    predicted_values = rf_model.predict(X_test)

    df.loc[df[target_column].isna(), target_column] = predicted_values


# Fonction Principale
if __name__ == "__main__":
    data = df.copy()

    data.drop(columns_to_drop, inplace = True)

    winsorize_outliers(data, columns_to_winsorize, 3)

    scaler = StandardScaler()
    data[columns_to_standardize] = scaler.fit_transform(df_standardized[columns_to_standardize])

    impute_with_random_forest(df, target_column='liveness', predictors=predictors)
    impute_with_random_forest(df, target_column='valence', predictors=predictors)
