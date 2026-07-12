import pandas as pd


def load_data(file_path):
    """
    Load the diabetes dataset.
    """

    return pd.read_csv(file_path)