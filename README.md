# Crypto-Currency-Machine-Learning-Trading-Bot

This is a machine learning trading bot that learns based on previous data and gives call signs for buying and selling different crypto currencies. In the future there are plans to expand this into also working with the stock market.

It has a main.py file that imports the necessary modules (data, analyze, display, and time) and contains two main functions: save_data() for collecting ticker data over a specified duration and saving it to a file, and run_from_terminal() which prompts the user for ticker symbols, filename, and tracking duration. The main execution flow runs the terminal interface, populates the dataframe using the analyze module, and prints basic statistical analysis.

The data.py module serves as the core data collection component of the trading bot, responsible for gathering real-time cryptocurrency market data from the Binance WebSocket API. This module establishes connections to live market streams and continuously collects 1-minute candlestick (kline) data for specified cryptocurrency trading pairs.

Key features include:
- **Real-time data streaming**: Connects to Binance's WebSocket API to receive live market data
- **Single ticker monitoring**: `current_statistics()` function tracks a single cryptocurrency pair indefinitely
- **Multi-ticker support**: `parallel_current_statistics()` function simultaneously monitors multiple trading pairs
- **Duration-based collection**: `parallel_current_statistics_duration()` function collects data for a specified time period using threading
- **JSON data handling**: Processes incoming WebSocket messages and stores them in a global data list
- **Threaded execution**: Uses threading to enable non-blocking data collection with time constraints

The module maintains a persistent connection to the Binance stream endpoint and populates a data array with incoming market information, which can then be processed by other components of the trading system for analysis and decision-making.
