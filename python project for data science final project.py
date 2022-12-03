
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#Q1
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
#Q2
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
data = requests.get(url).text
tesla_revenue = pd.read_html(url, match="Tesla Quarterly Revenue", flavor='bs4')[0]
tesla_revenue["Tesla Quarterly Revenue (Millions of US $).1"] = tesla_revenue['Tesla Quarterly Revenue (Millions of US $).1'].str.replace(',|\$',"")
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Tesla Quarterly Revenue (Millions of US $).1'] != ""]
tesla_revenue.rename(columns= {'Tesla Quarterly Revenue (Millions of US $)': "Date"}, inplace=True)
tesla_revenue.rename(columns= {'Tesla Quarterly Revenue (Millions of US $).1': "Revenue"}, inplace=True)
# print (tesla_revenue.tail())

#Q3
Gamestop = yf.Ticker("GME")
gme_data = Gamestop.history(period="max")
gme_data.reset_index(inplace=True)

# Q4
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
data = requests.get(url).text
soup = BeautifulSoup(data,'html.parser')
tables = soup.find_all('table')
gme_revenue = pd.read_html(str(tables[1]),flavor='bs4')[0]
gme_revenue["GameStop Quarterly Revenue (Millions of US $).1"] = gme_revenue['GameStop Quarterly Revenue (Millions of US $).1'].str.replace(',|\$',"")
gme_revenue.dropna(inplace=True)
gme_revenue.rename(columns= {'GameStop Quarterly Revenue (Millions of US $)': "Date"}, inplace=True)
gme_revenue.rename(columns= {'GameStop Quarterly Revenue (Millions of US $).1': "Revenue"}, inplace=True)
# print (gme_revenue.tail())

# Q5
# make_graph(tesla_data, tesla_revenue, 'Tesla')

#6
make_graph(gme_data, gme_revenue, 'GameStop')