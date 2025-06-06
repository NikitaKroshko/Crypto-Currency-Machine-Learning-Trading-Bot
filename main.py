import data
import time

def save_data(tickers,filename, duration = 1):
    # Takes as an input tickers in a list, filename as a string, and durtaion as an int
    # Runs the ticker data collection for duration minutes
    with open(filename, "w") as file:
        t = 60 * duration 
        data.parallel_current_statistics(tickers, t)
        file.writelines(str(data.data))

tickers = input("Which tickers do you want to track (split by ,): ")
input_list = tickers.split(",")
filename = input("Name of the file you want the tickers to be stored into: ")
duration = int(input("Enter the length of time you want the tickers to be tracker for: "))
save_data(input_list, filename, duration)


