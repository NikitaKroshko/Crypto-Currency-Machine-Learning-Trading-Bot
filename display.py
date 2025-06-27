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
    # Basic print out of the mean of the column for the ticker
    print(analyze.mean(column, ticker))

def display_mode(column, ticker):
    print(analyze.mode(column, ticker))
