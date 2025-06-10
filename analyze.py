import numpy as np
import pandas as pd
import json

df = None

def populate_df():
    df_data = data.data
    json_data = json.dumps(df_data)
    global df
    df = pd.read_json(json_data)
    return df
