import json
import websocket
import pandas as pd

def current_statistics(ticker):
    asset = ticker.lower() + "@kline_1m"

def on_message(ws,message):
    return json.loads(message)

