import pandas as pd
import data
import analyze

def display_data():
    # Basic print out of the data
    print(data.data)

def display_analyzed_data():
    # Basic print out of the df of the analyzed data
    print(analyze.df)

def display_mean(column, ticker):
    print(analyze.mean(column, ticker))
