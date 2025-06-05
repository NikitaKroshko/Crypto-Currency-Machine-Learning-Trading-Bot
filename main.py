import data
import time

def save_data(tickers,filename, duration = 1):
    with open(filename, "w") as file:
        t_end = time.time() + 60 * time
        while(time.time() < t_end):
            parallel_current_statistics(tickers)
        for line in data.data:
            file.write(line + "\n")

tickers = input("Which tickers do you want to track (split by ,): ")
input_list = tickers.split(",")
filename = input("Name of the file you want the tickers to be stored into: ")
duration = int(input("Enter the length of time you want the tickers to be tracker for: "))
save_data(input_list, filename, duration )


