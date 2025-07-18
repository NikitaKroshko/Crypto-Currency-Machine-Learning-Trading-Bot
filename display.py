# This is a supporting file for main.py
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
    # Basic print out of the mode of the column for the ticker
    print(analyze.mode(column, ticker))

def display_median(column, ticker):
    # Basic print out of the median of the column for the ticker
    print(analyze.median(column, ticker))

def main():
    # This function displays the data for the ticker of btcusdt this is for simple testing purposes
    print("############")
    print("Displaying data")
    display_data()
    print("############")
    print("Displaying analyzed data")
    display_analyzed_data()
    print("############")
    print("Displaying mean")
    display_mean("price", "BTCUSDT")
    print("############")
    print("Displaying mode")
    display_mode("price", "BTCUSDT")
    print("############")
    print("Displaying median")
    display_median("price", "BTCUSDT")
    print("############")

# Run the main function to display btc usdt data
main()
