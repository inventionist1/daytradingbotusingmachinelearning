from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import alpaca_trade_api as tradeapi

#init of module
load_dotenv()
np.set_printoptions(precision=3, suppress=True)

#function definitions
def connect():
    print(os.getenv("KEY"))
    live_api = tradeapi.REST(
        os.getenv("KEY"), 
        os.getenv("SECRET"), 
        os.getenv("ENDPOINT"), 
        api_version='v2')
    return live_api

def connect_w_endpoint(ENDPOINT:str):
    live_api = tradeapi.REST(
        os.getenv("KEY"), 
        os.getenv("SECRET"), 
        ENDPOINT, 
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

def get_bid_ask_price(symbol:str, API) -> tuple:
    try:
        quote = API.get_latest_quote(symbol.replace('-', '.'))
        bid_price = quote.bp
        ask_price = quote.ap
    except Exception as e:
        print("an error has occured")
        print(e)
        return None
    return (bid_price, ask_price)

def get_time_till_market_open(API):
    clock = API.get_clock()
    if(clock.is_open):
        return 0
    open_time = pd.Timestamp(clock.next_open)
    curr_time = pd.Timestamp(clock.timestamp)
    wait_time = open_time - curr_time
    return(wait_time)
        

if __name__ == "__main__":
    pass
