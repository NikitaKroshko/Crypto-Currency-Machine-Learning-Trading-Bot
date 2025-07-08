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

The display.py module functions as the presentation layer of the trading bot, providing various output methods to visualize collected data and analysis results. This supporting module works in conjunction with main.py to present information to users in a readable format.

Key features include:
- **Raw data output**: `display_data()` function prints the unprocessed cryptocurrency data collected from the WebSocket streams
- **Analyzed data presentation**: `display_analyzed_data()` function outputs the processed DataFrame containing analyzed market information
- **Statistical displays**: Dedicated functions for showing calculated statistics:
  - `display_mean()` - displays the mean value for a specified column and ticker symbol
  - `display_mode()` - displays the mode value for a specified column and ticker symbol
- **Modular design**: Each display function is focused on a specific type of output, making the code maintainable and extensible

The module serves as an interface between the data processing components (data.py and analyze.py) and the user, ensuring that complex market data and statistical analysis results are presented in an accessible format. This separation of concerns allows for easy modification of output formats without affecting the core data collection and analysis functionality.

The analyze.py module serves as the analytical engine of the trading bot, responsible for processing and analyzing the cryptocurrency market data collected by the data module. This supporting module transforms raw WebSocket data into structured DataFrames and provides comprehensive statistical analysis capabilities for informed trading decisions.

Key features include:
- **Data transformation**: `populate_df()` function converts raw data from the global data array into a structured pandas DataFrame
- **File-based data loading**: `populate_df_from_file()` function loads previously saved market data from JSON files for analysis
- **Comprehensive statistics**: `simple_statistics()` function provides detailed statistical summaries using pandas' describe() method
- **Targeted statistical analysis**: Individual functions for specific statistical measures:
  - `mean()` - calculates mean values for specified columns and ticker symbols
  - `median()` - computes median values for specified columns and ticker symbols
  - `mode()` - determines mode values for specified columns and ticker symbols
- **Global DataFrame management**: Maintains a global DataFrame variable for efficient data access across functions
- **Error handling**: Includes validation to ensure DataFrame is populated before performing analysis

The module acts as a bridge between raw market data collection and meaningful statistical insights, utilizing scientific computing libraries (NumPy, pandas, SciPy) to perform robust mathematical analysis. This processed information forms the foundation for the machine learning components and trading decision algorithms within the broader trading bot ecosystem.
