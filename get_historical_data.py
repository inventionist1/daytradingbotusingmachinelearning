#this time imma use yahoo finance cuz free :3
import yfinance as yf
import pandas as pd
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2,  Duration.SECOND*5)),
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache")
)

yf.set_tz_cache_location("daytradingbotusingmachinelearning/__yfinance__")

tickerStrings = ['AAPL','NMQ']
df_list = []
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker",period='2d')
    data['ticker'] = ticker
    df_list.append(data)

df = pd.concat(df_list)
df.to_csv('ticker.cvs')
print(df)