import requests
from bs4 import BeautifulSoup
import pandas as pd

years = [year for year in range(1994, 2018)]
meetings = []
for year in years:
  url = f"https://www.federalreserve.gov/monetarypolicy/fomchistorical{year}.htm"
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    headings = soup.find_all("h5")
    for heading in headings:
      text = heading.text.strip()
      meetings.append(text)
  else:
    print(response)

df = pd.DataFrame({'data': meetings})
df['data'] = df['data'].str.split()
df['month'] = df['data'].apply(lambda x: x[0] if len(x) > 0 else None)
df['month'] = df['month'].str.split("/").apply(lambda x: x[-1] if len(x) > 0 else None)
df['day'] = df['data'].apply(lambda x: x[1] if len(x) > 0 else None)
df['day'] = df['day'].str.split("-").apply(lambda x: x[-1] if len(x) > 0 else None)
df['event'] = df['data'].apply(lambda x: x[2] if len(x) > 0 else None)
df['year'] = df['data'].apply(lambda x: x[len(x)-1] if len(x) > 0 else None)
df.to_csv('fomc_events_1.csv')

