import requests
import json
from alpaca.trading.stream import TradingStream

API_FILE:str = "C:\\Users\\Isaac\\Desktop\\trading bot\\daytradingbotusingmachinelearning\\apikey.json"

def get_API_keys(filename:str) -> str:
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    return ''

def connect(is_paper:bool=True):
    keys = get_API_keys(API_FILE)
    if not(is_paper):
        alpaca_keys:list[str] = {
            "TRADE_API_KEY":keys['real_key'],
            "TRADE_API_SECRET":keys['real_secret'],
            "TRADE_API_ENDPOINT":keys['real_endpoint']
        }
    else:
        alpaca_keys:list[str] = {
            "TRADE_API_KEY":keys['paper_key'],
            "TRADE_API_SECRET":keys['paper_secret'],
            "TRADE_API_ENDPOINT":keys['paper_endpoint']
        }
    stream_client = TradingStream(api_key=alpaca_keys["TRADE_API_KEY"], secret_key=alpaca_keys["TRADE_API_SECRET"], paper=is_paper)
    stream_client.run()



if __name__ == "__main__":
    print(get_API_keys(""))