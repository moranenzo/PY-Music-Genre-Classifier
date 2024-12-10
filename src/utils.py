import joblib  # used to save Scikit-learn models as .pkl


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
