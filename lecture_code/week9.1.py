# # """
# # Write a function that implements division with two positive integers without using the division, multiplication, or modulous operator. Return the quotient as an integer, and ignore the remainder.

# # """

# # # set up function definition

# # # two numbers as arguments, one is divisor and one is dividend

# # # loop

# # # in the loop, 


# # def division(divisor, dividend):
# #     quotient = 0
# #     sum = 0
# #     while divisor >= dividend:
# #         sum += dividend
# #         quotient += 1

# #     return quotient

# # print(division(25, 5))


# # list comprehension!!! :)

# """
# newList = [expression for item in iterable if condition]
# """

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evenNums = [num for num in nums if num % 2 == 0]
# print(evenNums)


# # new list of the characters that aren't spaces 
# text = "teach a man to fish"

# # chars = [char for char in text if char != " "]
# # print(chars)
# chars = []

# for char in text:
#     if char != " ":
#         chars.append(char)

# # palindromes

# words = ["level", "dog", "racecar", "rain", "swag", "civic"]

# pals = [word[0:4] for word in words if word[::-1] == word and word.startswith("l")]
# print("our best pals :)", pals)



# non-list comprehension way to load in my prices
with open("/workspaces/sp26_data_3500/lecture_code/TSLA.txt") as file:
    lines = file.readlines()

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

# reverse the prices since they load in backwards from NASDAQ
prices = prices[::-1]

# list comprehension to load in my proces
daily_prices = [float(line) for line in open("/workspaces/sp26_data_3500/lecture_code/TSLA.txt").readlines()]

# reverse the prices since they load in backwards from NASDAQ
prices = prices[::-1]

# counter to determine when to start analysis
i = 0
buy = 0
for price in daily_prices:
    if i > 5:
        # price                 these should be the same number
        # daily_prices[i]
        moving_avg = (daily_prices[i-1] + daily_prices[i-2] + daily_prices[i-3] + daily_prices[i-4] + daily_prices[i-5]) / 5

        if price < moving_avg * 0.98:
            pass
            #buy
            #update buy variable
            #update first_buy variable if this is the first time you buy
        elif price > moving_avg * 1.02:
            pass
            #sell
            #calculate profit of this individual trade
            #keep a running total of all profit
        else:
            pass
            # do nothing this iteration

    i += 1
