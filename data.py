import json
import websocket
import pandas as pd
import time

socket = "wss://stream.binance.com:9443/stream?streams="
data = []

def current_statistics(ticker):
    #Takes a ticker symbol for crypto_currencies and populates a data list of the file with that ticker symbols data
    asset = ticker.lower() + "@kline_1m"
    socket_msg = socket+asset
    ws = websocket.WebSocketApp(socket_msg, on_message=on_message)
    ws.run_forever()

def on_message(ws,message):
    # Message handler for the websocket
    message = json.loads(message)
    data.append(message)
    print(len(data))

def parallel_current_statistics(tickers):
    # Same principle as for the current statistics but this takes a list of tickers and returns data for all of them
    assets = []
    for asset in tickers:
        assets.append(asset.lower() + "@kline_1m")
    socket_msg = socket+("/".join(assets))
    ws = websocket.WebSocketApp(socket_msg, on_message=on_message)
    ws.run_forever()

def parallel_current_statistics(tickers, duration):
    # Same principle as for the current statistics but this takes a list of tickers and returns data for all of them
    assets = []
    for asset in tickers:
        assets.append(asset.lower() + "@kline_1m")
    socket_msg = socket+("/".join(assets))
    ws = websocket.WebSocketApp(socket_msg, on_message=on_message)
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.start()
    time.sleep(duration)
    ws.close()
    ws_thread.join()
