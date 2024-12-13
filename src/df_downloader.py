import s3fs
import pandas as pd

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
