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

def calculate_atr_from_data(data:list, periods:int):
    total:float = 0
    start:int = (len(data) > data-1)*(len(data)-periods) + (len(data) <= periods-1)*len(data)
    if(len(data) < 2): return 0
    for i in range(start,len(data)):
        if i == 0:
            continue
    total += get_true_range(data[i]["h"],data[i]["l"],data[i-1]['c'])
    atr:float = total/i

if __name__ == "__main__":
    pass
