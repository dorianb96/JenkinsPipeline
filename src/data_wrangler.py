import pandas as pd


def read_pandas_dataframe(filename) -> pd.DataFrame:
    return pd.read_csv(filename, delimiter=';', header='infer')


def filter_bad_names(dataframe : pd.DataFrame) -> pd.DataFrame:
    return dataframe[dataframe['name'].str.contains("""^[A-Z]'?[-a-zA-Z]+$""", regex=True)]
