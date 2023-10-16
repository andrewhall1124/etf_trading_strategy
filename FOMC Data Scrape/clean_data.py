# Create date objects from the different columns

import pandas as pd

df = pd.read_csv('fomc_events_1.csv')
df1 = df[['month', 'day', 'event', 'year']]
month_to_number = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}
df1['month'] = df1['month'].map(month_to_number)
df1['date'] = pd.to_datetime(df1[['year', 'month', 'day']], format='%Y-%m-%d')
df1 = df1.query("event == 'Meeting'")

df = pd.read_csv('fomc_events_2.csv')
df2 = df[['month', 'day', 'event', 'year']]
df2['month'] = df2['month'].map(month_to_number)
df2['date'] = pd.to_datetime(df2[['year', 'month', 'day']], format='%Y-%m-%d')

df3 = pd.merge(df1, df2, how='outer')
df3 = df3.drop(columns=['month', 'day', 'event', 'year'])
df3.to_csv('FOMC_DATES.csv')