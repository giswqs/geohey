"""This is the utils module that contains utility functions for the geohey package.
"""


def csv_to_df(csv_file):
    """Converts a CSV file to a pandas DataFrame.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The pandas DataFrame.
    """
    import pandas as pd

    return pd.read_csv(csv_file)
