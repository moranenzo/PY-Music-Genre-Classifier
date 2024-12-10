# Required imports
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from df_downloader import get_df
from utils import save_model

from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb

df_path = "/tlaflotte/genre_detector/spotify_tracks.csv"


# Load the dataset
def load_data(path):
    try:
        df = get_df(path)
        print("Data successfully loaded.")
        return df
    except FileNotFoundError:
        print("Error: Data file not found.")
        return None


# Data preprocessing
def preprocess_data(df):
    target = "track_genre"  # Target variable
    features = df.drop(columns=[target, "track_id", "track_name", "artists"])
    X = features
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)


# Dummy CatBoost model
cat_model = CatBoostClassifier(
        iterations=500,
        learning_rate=0.1,
        depth=8,
        loss_function='MultiClass',
        verbose=100
    )

# Dummy Models
rf_model = RandomForestClassifier()
xgb_model = xgb.XGBClassifier()
lgb_model = lgb.LGBMClassifier()


# Train the model
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy:.2f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))
    return accuracy


# Main function
if __name__ == "__main__":
    df = load_data(df_path)
    if df is not None:
        X_train, X_test, y_train, y_test = preprocess_data(df)
        model = train_model(cat_model, X_train, y_train)
        evaluate_model(model, X_test, y_test)
        save_model(model, model_name="catboost")
