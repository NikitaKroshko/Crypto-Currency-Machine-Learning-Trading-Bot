import numpy as np
import pandas as pd
import json
import data

df = None

def populate_df():
    # Take data in from the data.data array and produces a dataframe
    # object in the df global file variable.
    df_data = data.data
    json_data = json.dumps(df_data)
    global df
    df = pd.read_json(json_data)
    return df

def populate_df_from_file(file_path):
    # Take data in from the file_path associated file and produces a dataframe
    # object in the df global file variable.
    global df
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        df = pd.read_json(json_data)
    return df

def simple_statistics():
    # Returns a dataframe with simple statistics about the data in the df global file variable.
    global df
    if df is None:
        raise ValueError("DataFrame is not populated.")
    return df.describe()

def mean(column_name, ticker_symbol):
#
