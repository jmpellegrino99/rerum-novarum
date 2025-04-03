import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbol
ticker = "DIS"
comp_ticker = "SPY"

# Fetch the stock data
dis = yf.Ticker(ticker)
comp = yf.Ticker(comp_ticker)

dis_price = dis.history(period="1d")["Close"].tolist()[0]
comp_price = comp.history(period="1d")["Close"].tolist()[0]

print(f"DIS: {round(dis_price, 2)}")
print(f"SPY: {round(comp_price, 2)}")