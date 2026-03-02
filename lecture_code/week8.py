"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
Write a Python program to read in the stock prices from a file, into a list.
Create a list of floats from the list of strings you read in, from step 2.
Calculate the average of the first 4 days in your list.
Calculate the average of the last 4 days in your list.
In a for loop, calculate a 4 day moving average for the floats in the list.
Add logic in the for loop to implement a simple moving average 
trading strategy.
Display the profit from the strategy, after the for loop has finished.
"""
# Activity 5
# create file variable to pull data into cloud9
file = open("/workspaces/sp26_data_3500/lecture_code/AAPL.2023.txt")

# convert file object into list of lines
lines = file.readlines()

# convert lines into rounded floats and put them in a new list
prices = []
for line in lines:
    prices.append(float(line))


# moving avg

# five_day_avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
# print("five_day_avg:", five_day_avg)

i = 0

for price in prices:
    moving_avg = (prices[i] + prices[i+1] + prices[i+2] + prices[i+3] + prices[i+4]) / 5
    i += 1