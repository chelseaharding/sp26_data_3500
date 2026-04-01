import json

def meanReversionStrategy():
    # run strategy and output buys/sells, final profit, and final percentage returns
    # return profit and returns
    pass

def simpleMovingAverageStrategy():
    # run strategy and output buys/sells, final profit, and final percentage returns
    # return profit and returns
    pass

def saveResults(results):
    json.dump(results, open("/workspaces/sp26_data_3500/hw5/results.json"), "w", indent=4)

# create list to store 10 tickers
tickers = ["AAPL", "GOOG", "ADBE", "TLSA"]




# create dictionary called results to store prices, profits and return percentages
