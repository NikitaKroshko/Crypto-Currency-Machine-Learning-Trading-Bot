import data
import analyze
import time

def save_data(tickers, filename, duration = 1):
    # Takes as an input tickers in a list, filename as a string, and durtaion as an int
    # Runs the ticker data collection for duration minutes
    # Saves it to the filename file
    with open(filename, "w") as file:
        t = 60 * duration
        data.parallel_current_statistics(tickers, t)
        file.writelines(str(data.data))

def run_from_terminal():
    # When run prompts the user for information so that the data can be collected
    tickers = input("Which tickers do you want to track (split by ,): ")
    input_list = tickers.split(",")
    filename = input("Name of the file you want the tickers to be stored into: ")
    duration = int(input("Enter the length of time you want the tickers to be tracker for: "))
    save_data(input_list, filename, duration)

run_from_terminal()
analyze.populate_df()
print(analyze.simple_statistics())
