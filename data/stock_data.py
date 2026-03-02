import yfinance as yf
import pandas as pd

stocks = ["TSLA", "NVDA", "AAPL", "AMZN", "MSFT"]

for ticker in stocks:
    print(f"Fetching data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period="30d")
    df.to_csv(f"data/{ticker}_price.csv")
    print(f"{ticker} data saved!")

print("All stock data collected!")
