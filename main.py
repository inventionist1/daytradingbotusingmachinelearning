#import tensorflow as tf # type: ignore
import load_data as data
import time
import datetime
#needs pythoin 3.10 or above at minimum


def init() -> None:
    global API, SYMBOL, past_atr, last_bar_closing_price, curr_high, curr_low
    API = data.connect()
    SYMBOL = "AAPL"
    past_atr, last_bar_closing_price = data.calculate_past_15m_average_trading_range(SYMBOL,API)
    bid_price, ask_price = data.get_bid_ask_price(SYMBOL,API)
    curr_high = ask_price
    curr_low = ask_price
    

def main() -> None:
    global API, SYMBOL, past_atr, last_bar_closing_price, curr_high, curr_low
    bid_price, ask_price = data.get_bid_ask_price(SYMBOL,API)
    if(datetime.datetime.now().strftime('%S') == "00"):
        curr_high = ask_price
        curr_low = ask_price
        past_atr = data.calculate_past_15m_average_trading_range(SYMBOL,API)
    if(ask_price > curr_high):
        curr_high = ask_price
    if(ask_price < curr_low):
        curr_low = ask_price
    atr = data.calculate_current_average_trading_range(past_atr, data.get_true_range(curr_high,curr_low,last_bar_closing_price))


    

if __name__ == "__main__":
    init()
    while True:
        time0 = time.monotonic()
        main()
        time1 = time.monotonic()
        if(1-(time1-time0) > 0):
            time.sleep(1-(time1-time0))
        else:
            print("Can't keep up! running", int((1-(time1-time0))*-1000), "ms behind!")
        
