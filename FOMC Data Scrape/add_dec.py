import pandas as pd
import numpy as np

df1 = pd.read_csv('./FOMC_DATES.csv')
df2 = pd.read_csv('DFEDTAR.csv')
merged_df = df1.merge(df2, on='date', how='left')
merged_df.sort_values(by='date', inplace=True)
merged_df = merged_df.rename(columns={'rate': 'rate_after'})
merged_df['rate_before'] = merged_df['rate_after'].shift(1)
merged_df = merged_df.reindex(['date', 'rate_before', 'rate_after'], axis = 1)
conditions = [
    (merged_df['rate_after'] > merged_df['rate_before']),
    (merged_df['rate_after'] < merged_df['rate_before']),
    (merged_df['rate_after'] == merged_df['rate_before'])
]
actions = ['raise', 'lower', 'nothing']
merged_df['action'] = np.select(conditions, actions, default='unknown')
merged_df.to_csv('FOMC_DATA.csv')


