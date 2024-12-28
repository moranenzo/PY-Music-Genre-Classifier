import joblib  # used to save Scikit-learn models as .pkl
import s3fs
import pandas as pd


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

