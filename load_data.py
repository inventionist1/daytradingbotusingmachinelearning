from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np

#init of module
load_dotenv()
np.set_printoptions(precision=3, suppress=True)

#function definitions
def get_api_keys() -> dict:
    ALPACA_KEYS:list[str] = {
        "TRADE_API_ENDPOINT":os.getenv("ENDPOINT"),
        "TRADE_API_SECRET":os.getenv("SECRET"),
        "TRADE_API_KEY":os.getenv("KEY"),
        "PAPER_ACCOUNT":os.getenv("PAPER")
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

if __name__ == "__main__":
    print(get_training_data("/home/valkyrie/Desktop/trading bot/daytradingbotusingmachinelearning/week_data.csv"))