import pandas as pd

df = pd.read_csv('etf_list_12data.csv')
df = df.reindex(['symbol'], axis=1)
df.to_csv('ETF_LIST.csv')