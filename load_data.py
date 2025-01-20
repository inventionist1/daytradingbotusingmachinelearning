from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame

#init of module
load_dotenv()
np.set_printoptions(precision=3, suppress=True)

#function definitions
def connect():
    live_api = tradeapi.REST(
        os.getenv("KEY"), 
        os.getenv("SECRET"), 
        os.getenv("ENDPOINT"), 
        api_version='v2')
    return live_api

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

def get_bid_ask_price(symbol:str, API) -> float:
    try:
        quote = API.get_latest_quote(symbol.replace('-', '.'))
        bid_price = quote.bp
        ask_price = quote.ap
    except Exception as e:
        print("an error has occured")
        print(e)
        return None
    return (bid_price, ask_price)

#math from https://www.investopedia.com/terms/a/atr.asp#toc-the-average-true-range-atr-formula
def get_true_range(high:float, low:float, closing_price:float) -> float:
    return max(
        (high-low),
        abs(high-closing_price),
        abs(low-closing_price)
    )

def calculate_current_average_trading_range(past_atr:float, true_range:float, periods:int=14):
    return ((past_atr*(periods-1)) + true_range)/periods

def calculate_past_15m_average_trading_range(symbol:str, API) -> tuple:
    cvs_bars_data = API.get_bars(symbol, TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw', feed="IEX").df
    clean_bars_data = np.array(cvs_bars_data)
    clean_bars_data = clean_bars_data.astype(np.float64)
    total:float = 0
    #get average of the true ranges of each bar
    for i in range(len(clean_bars_data)):
        if i == 0:
            continue
        total += get_true_range(clean_bars_data[i][1],clean_bars_data[i][2],clean_bars_data[i-1][0])
    atr:float = total/i
    return (atr, clean_bars_data[i][0])

if __name__ == "__main__":
    pass
