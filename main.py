#import tensorflow as tf # type: ignore
import load_data as data
import time
#needs pythoin 3.7 or above at minimum

def init() -> None:
    pass

def main() -> None:
    pass
    

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
        
