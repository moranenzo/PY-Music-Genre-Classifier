# Required imports
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib

df_path = "/ponte/Projet_data/data_tracks_cleaned.csv"


# Chargement du jeu de données
df = pd.read_csv("https://minio.lab.sspcloud.fr" + df_path)


# Séparation en parties d'entraînement et de test
def preprocess_data(data):
    # isolation of the feature to predict
    genres = np.array(data['playlist_genre'])
    features = data.drop(['playlist_genre', 'playlist_subgenre_encoded'], axis = 1)
    features = np.array(features)

    # separation in training and testing sets
    train_features, test_features, train_genres, test_genres = train_test_split(features, genres, test_size = 0.25, random_state = 0, shuffle = True)

    return train_features, test_features, train_genres, test_genres


# Meilleurs hyperparamètres
rf_best_params = {'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 4000}
xgb_best_params = {'learning_rate': 0.1, 'max_depth': 20, 'n_estimators': 300, 'subsample': 0.8}
cat_best_params = {'iterations': 1000, 'learning_rate': 0.05, 'depth': 5, 'l2_leaf_reg': 1, 'border_count': 64}


# Modèles non entrainés
rf_model = RandomForestClassifier(n_estimators=4000, max_features='sqrt', max_depth=20, min_samples_split=2, min_samples_leaf=1, bootstrap=True, criterion='gini' ,random_state=0)
xgb_model = XGBClassifier(objective='multi:softprob', colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=20, min_child_weight=1, n_estimators=300, subsample=0.8, random_state = 42)
cat_model = CatBoostClassifier(**cat_best_params, cat_features=[], verbose=0)


# Dictionnaire des modèles
models = {
    'randomforest': rf_model,
    'xgboost': xgb_model,
    'catboost': cat_model
}


# Encodage du genre
def genre_to_num(genre):
    if genre == 'edm':
        return 0
    if genre == 'latin':
        return 1
    if genre == 'pop':
        return 2
    if genre == 'r&b':
        return 3
    if genre == 'rap':
        return 4
    if genre == 'rock':
        return 5


# Entraînement du modèle
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


# Évaluation du modèle
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy:.2f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))
    return accuracy


# Sauvegarde
def save_model(model_name, save_name="model", model_dir="./models"):
    file_path = None

    if model_name == "catboost":
        file_path = f"{model_dir}/{save_name}.cbm"
        model.save_model(file_path)
    elif model_name == "xgboost":
        file_path = f"{model_dir}/{save_name}.json"
        model.save_model(file_path)
    elif model_name == "randomforest":
        file_path = f"{model_dir}/{save_name}.pkl"
        joblib.dump(model, file_path)
    else:
        print("Type de modèle non pris en charge.")
        return

    print(f"Modèle sauvegardé à {file_path}")


# Fonction principale
if __name__ == "__main__":
    data = df.copy()
    model_name = 'catboost'      # changer le model_name pour modifier le type de modèle utilisé
    data['playlist_genre'] = data['playlist_genre'].apply(genre_to_num)
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(models[model_name], X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model_name, save_name=model_name + '_trained_model')
