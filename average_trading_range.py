from alpaca_trade_api.rest import TimeFrame
import numpy as np
import datetime

#math from https://www.investopedia.com/terms/a/atr.asp#toc-the-average-true-range-atr-formula
def get_true_range(high:float, low:float, closing_price:float) -> float:
    return max(
        (high-low),
        abs(high-closing_price),
        abs(low-closing_price)
    )

def calculate_new_average_trading_range(past_atr:float, true_range:float, periods:int=14):
    return ((past_atr*(periods-1)) + true_range)/periods

def calculate_past_15m_average_trading_range(symbol:str, API) -> tuple:
    #get and clean bar data
    cvs_bars_data = API.get_bars(symbol, TimeFrame.Minute, "2023-06-08", "2023-06-08", adjustment='raw', feed="IEX").df
    clean_bars_data = np.array(cvs_bars_data)
    clean_bars_data = clean_bars_data.astype(np.float64)


    #get the average trading range of the last 14 bar data, or of all the bar data if less than 14
    total:float = 0
    start:int = (len(clean_bars_data) > 13)*(len(clean_bars_data)-14) + (len(clean_bars_data) <= 13)*len(clean_bars_data)
    for i in range(start,len(clean_bars_data)):
        if i == 0:
            continue
    total += get_true_range(clean_bars_data[i][1],clean_bars_data[i][2],clean_bars_data[i-1][0])
    atr:float = total/i
    return (atr, clean_bars_data[i][0], len(clean_bars_data)-start)
    
def calculate_current_average_trading_range(ask_price:float,SYMBOL,API) -> tuple:
    global past_atr, last_bar_closing_price, curr_high, curr_low, periods, atr
    try:
        if(datetime.datetime.now().strftime('%S') == "00"):
            curr_high = ask_price
            curr_low = ask_price
            last_bar_closing_price = ask_price
            past_atr = atr

        if(ask_price > curr_high):
            curr_high = ask_price

        if(ask_price < curr_low):
            curr_low = ask_price

        atr = calculate_new_average_trading_range(past_atr, get_true_range(curr_high,curr_low,last_bar_closing_price))
        return atr
    except NameError:
        past_atr, last_bar_closing_price, periods = calculate_past_15m_average_trading_range(SYMBOL,API)
        curr_high, curr_low = (ask_price,ask_price)
        return (past_atr, curr_high, curr_low)
    

if __name__ == "__main__":
    pass
