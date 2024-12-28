# Required imports
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from df_downloader import get_df
from notebooks.utils import save_model

from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb

df_path = "/tlaflotte/genre_detector/data_tracks_cleaned.csv"


# Load the dataset
df = pd.read_csv("https://minio.lab.sspcloud.fr" + df_path)


# Best Hyperparameters
rf_best_params = {'max_depth': 20, 'min_samples_split': 2, 'n_estimators': 4000}
xgb_best_params =
cat_best_params =


# Dummy Models
rf_model = RandomForestClassifier(n_estimators=4000, max_features='sqrt', max_depth=20, min_samples_split=2, min_samples_leaf=1, bootstrap=True, criterion='gini' ,random_state=0)
xgb_model = xgb.XGBClassifier()
cat_model = 


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
    data = df.copy()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(cat_model, X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, model_name="catboost")
