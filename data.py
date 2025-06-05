import json
import websocket
import pandas as pd

socket = "wss://stream.binance.com:9443/stream?streams="
data = []

def current_statistics(ticker):
    asset = ticker.lower() + "@kline_1m"
    socket_msg = socket+asset
    ws = websocket.WebSocketApp(socket_msg, on_message=on_message)
    ws.run_forever()

def on_message(ws,message):
    message = json.loads(message)
    data.append(message)
    print(len(data))

def parallel_current_statistics(tickers):
