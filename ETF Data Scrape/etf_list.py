import requests
import pandas as pd

url = "https://twelve-data1.p.rapidapi.com/etf"

querystring = {"format":"json"}

headers = {
	"X-RapidAPI-Key": "482b6ddc86mshc78eb4c3ba92cf6p12a7c7jsn7b0fbc094db1",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
df = pd.DataFrame(response.json()['data'])
df = df.query("country == 'United States'")
df.to_csv('etf_list_12data.csv')