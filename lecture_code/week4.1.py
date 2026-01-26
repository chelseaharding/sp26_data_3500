# pseudocode 

# given a list of numbers, count how many are above the average of all the numbers in the list

# maybe :[
# nums = [1, 2, 3, 4, 5]
# count = 0

# for num in nums:
#     avg = avg + num / 5
#     if num > avg:
#         count = count + 1

"""
1. establish list of numbs
2. calculate avg
3. set up a counter to track the desired result
4. loop
5. compare num to avg and increment counter appropriately
"""
# 1
nums = [1, 2, 3, 4, 5]
# 2
# avg = mean(nums)
# 3
counter = 0


# leap year

year = 1900

if year % 4 == 0:
    if year % 100 == 0:
        print("not a leap year :(")
    else:
        print("it's a leap year!")
else:
    print("not a leap year")


# while loops/statements
while year % 4 == 0:
    print("it's a leap year")
    year = year + 1


age = 2

while age < 9:
    print("aww you're so cute!")
    age = age + 1
else:
    print("you're not it anymore. sorry")

# guess the secret number
# if user guess too high, tell them and let them keep guessing
# if too low, tell them and let them keep guessing
# if correct, print out that they are correct and stop running the code


# pseudocode
# 0. variable to keep loop going
# 1. set up a loop to have the user keep guessing
# 2. create variables to track user guesses
# 3. compare guess to actual number
# 4. print responses for each guess
# 5. if they get it right, make the loop stop

import random
secret_num = random.randint(1, 100)

not_guessed = True

while not_guessed == True:
    guess = int(input("Enter your guess: "))

    if guess > secret_num:
        print("Too high!")
    elif guess < secret_num:
        print("Too low!")
    else:
        print("You got it!")
        not_guessed = False
