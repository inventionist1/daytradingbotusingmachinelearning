from dotenv import load_dotenv
import os

load_dotenv()

def get_api_keys():
    ALPACA_KEYS:list[str] = {
        "TRADE_API_ENDPOINT":os.getenv("ENDPOINT"),
        "TRADE_API_SECRET":os.getenv("SECRET"),
        "TRADE_API_KEY":os.getenv("KEY"),
        "PAPER_ACCOUNT":os.getenv("PAPER")
    }
    return ALPACA_KEYS

if __name__ == "__main__":
    pass