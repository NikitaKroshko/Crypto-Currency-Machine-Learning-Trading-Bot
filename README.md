# Crypto-Currency-Machine-Learning-Trading-Bot

This is a machine learning trading bot that learns based on previous data and gives call signs for buying and selling different crypto currencies. In the future there are plans to expand this into also working with the stock market.

It has a main.py file that imports the necessary modules (data, analyze, display, and time) and contains two main functions: save_data() for collecting ticker data over a specified duration and saving it to a file, and run_from_terminal() which prompts the user for ticker symbols, filename, and tracking duration. The main execution flow runs the terminal interface, populates the dataframe using the analyze module, and prints basic statistical analysis.
