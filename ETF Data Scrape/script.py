import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tickers = ['AAPL']

data = yf.download(tickers, period='max')
df = pd.DataFrame(data)
birthday = df.index[0]
print(f"Birthday: {birthday}")

# df.to_csv("tickers_data.csv")