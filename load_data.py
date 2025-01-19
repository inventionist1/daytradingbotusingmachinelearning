from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import requests
import alpaca_trade_api as tradeapi

#init of module
load_dotenv()
np.set_printoptions(precision=3, suppress=True)

#function definitions
def connect(LIVE_API_KEY, LIVE_SECRET_KEY, LIVE_BASE_URL):
    live_api = tradeapi.REST(LIVE_API_KEY, LIVE_SECRET_KEY, LIVE_BASE_URL, api_version='v2')
    return live_api

def get_api_keys() -> dict:
    ALPACA_KEYS:list[str] = {
        "TRADE_API_ENDPOINT":os.getenv("ENDPOINT"),
        "TRADE_API_SECRET":os.getenv("SECRET"),
        "TRADE_API_KEY":os.getenv("KEY")
    }
    return ALPACA_KEYS

def get_training_data(file:str) -> list:
    training_data = pd.read_csv(file,names = ["Date", 
                                              "Close", 
                                              "Volume", 
                                              "Open", 
                                              "High", 
                                              "Low"])
    training_data_features = training_data.copy()
    training_data_features.pop("Date")
    training_data_features = training_data_features.drop(index = 0, axis = 0)
    training_data_features = np.array(training_data_features)
    training_data_features = training_data_features.astype(np.float32)
    return(training_data_features)

def get_bid_ask_price(symbol:str, live_api) -> float:
    try:
        quote = live_api.get_latest_quote(symbol.replace('-', '.'))
        bid_price = quote.bp
        ask_price = quote.ap
    except Exception as e:
        print("an error has occured")
        print(e)
        return None
    return [bid_price, ask_price]

if __name__ == "__main__":
    ALPACA_KEYS = get_api_keys();
    print(get_bid_ask_price("TSLA",connect(ALPACA_KEYS["TRADE_API_KEY"],ALPACA_KEYS["TRADE_API_SECRET"],ALPACA_KEYS["TRADE_API_ENDPOINT"])))
