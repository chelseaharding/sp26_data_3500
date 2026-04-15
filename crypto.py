import json
import requests
import datetime
import time

# break up the url so we can add variables to it 
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

# keys for the api json 
market_key  = "market_data"
price_key   = "current_price"
usd_key     = "usd"

coins = ["ethereum", "bitcoin"]

for coin in coins:
    start_date = datetime.datetime.now() - datetime.timedelta(days=366)
    file = open(coin+".csv", "w")
    file_lines = []
    for i in range(4):
        time.sleep(10)
        # add one day to the start date 
        start_date += datetime.timedelta(days=1)
        formatted_date = start_date.strftime("%d-%m-%Y")
        complete_url = url1 + coin + url2 + str(formatted_date) + url3
        print(complete_url)
        # make the request with the new formatted URL
        request = requests.get(complete_url)
        eth_dictionary = json.loads(request.text)
        try:
            file_lines.append(formatted_date + ", " + str(eth_dictionary[market_key][price_key][usd_key]) + "\n")
        except:
            print("You ran out of API calls")
    file.writelines(file_lines)