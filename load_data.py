import requests


def getAPIKey(filename:str) -> str:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        return data
    except:
        print("an error occured, please check the filename and try again");
        return ""



if __name__ == "__main__":
    print(getAPIKey("/home/valkyrie/Desktop/trading bot/daytradingbotusingmachinelearning/apikey.txt"))