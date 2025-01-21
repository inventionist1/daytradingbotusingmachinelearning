#import tensorflow as tf # type: ignore
import load_data as data
import time
import average_trading_range as IndATR
#needs pythoin 3.10 or above at minimum

def init() -> None:
    global API, SYMBOL
    API = data.connect()
    SYMBOL = "TSLA"

def main() -> None:
    global API, SYMBOL
    bid_price, ask_price = data.get_bid_ask_price(SYMBOL,API)
    atr, curr_high, curr_low = IndATR.calculate_current_average_trading_range(ask_price,SYMBOL,API)
    

if __name__ == "__main__":
    init()
    time_till_open = data.get_time_till_market_open(API)
    if(time_till_open.total_seconds() > 0):
        time_till_open_components = time_till_open.components
        print("Market is closed, market will reopen in",time_till_open_components.days,
              "days,",time_till_open_components.hours,"hours,",
              time_till_open_components.minutes,"minutes, and",
              time_till_open_components.seconds, "seconds")
    while time_till_open.total_seconds() == 0:
        initintual_time = time.monotonic()
        main()
        final_time = time.monotonic()
        delta_time = final_time-initintual_time
        if(1-delta_time >= 0):
            time.sleep(1-(delta_time))
        else:
            print("Can't keep up! running", int((1-delta_time)*-1000), "ms behind!")    
