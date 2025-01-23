# pip install yfinance
# https://pypi.org/project/yfinance/

import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.info)
print(msft.calendar)
print(msft.analyst_price_targets)
print(msft.quarterly_income_stmt)
print(msft.history(period='1mo'))
print(msft.option_chain(msft.options[0]).calls)

aapl = yf.download('AAPL')
print(aapl.head())

spy = yf.Ticker('SPY').funds_data
print(spy.description)
print(spy.top_holdings)