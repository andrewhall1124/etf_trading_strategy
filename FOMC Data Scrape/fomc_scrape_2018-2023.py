import requests
from bs4 import BeautifulSoup
import pandas as pd

meetings = []
url = f"https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
response = requests.get(url)
if response.status_code == 200:
  soup = BeautifulSoup(response.content, "html.parser")
  calendars = soup.find_all("div", {"class": "panel panel-default"})
  for calendar in calendars:
    year = calendar.find("a").text.strip().split()[0]
    dates = calendar.find_all("div", {"class": "fomc-meeting"})
    for date in dates:
      data = []
      month = date.find("div", {"class": "fomc-meeting__month"}).find("strong").text.strip()
      data.append(month)
      month = month.split("/")[-1]
      day = date.find("div", {"class": "fomc-meeting__date"}).text.strip()
      data.append(day)
      data.append("Meeting")
      data.append(year)
      day = day.split()[0].split("-")[-1].strip("*")
      meetings.append([data, month, day, "Meeting", year])
else:
  print(response)

df = pd.DataFrame(meetings,columns=['data', 'month', 'day', 'event', 'year'])
df.to_csv('fomc_events_2.csv')

