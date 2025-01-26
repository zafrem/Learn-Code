# pip install pandas-datareader
# https://pandas-datareader.readthedocs.io/en/latest/

import pandas_datareader.data as web
#import pandas as pd
import datetime as dt

df = web.DataReader('005930', 'naver', start='2025-01-01', end='2025-01-20')

print(df.head())

start_date = dt.datetime(2025, 1, 1)
end_date = dt.datetime(2025, 1, 20)

data = web.DataReader('AAPL', 'stooq', start=start_date, end=end_date)

print(data.head())