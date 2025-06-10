import numpy as np
import pandas as pd
import json
import data

df = None

def populate_df():
    df_data = data.data
    json_data = json.dumps(df_data)
    global df
    df = pd.read_json(json_data)
    return df

def populate_df_from_file(file_path):
    global df
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        df = pd.read_json(json_data)
    return df

def simple_statistics():
    global df
    if df is None:
        raise ValueError("DataFrame is not populated.")
    return df.describe()
