import requests
import json


url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=NG9C9EPVYBMQT0C8"

request = requests.get(url)
stock_dictionary = json.loads(request.text)
# print(stock_dictionary)

# keys i need
time = "Time Series (Daily)"
# key2 = "2026-04-06"
price = "4. close"

file = open("/workspaces/sp26_data_3500/stock_market_trading_project/TSLA.csv", "w")

for date in stock_dictionary[time].keys():
    # print(date, stock_dictionary[time][date][price])
    file.write(date + ", " + stock_dictionary[time][date][price] + "\n")

file.close()







