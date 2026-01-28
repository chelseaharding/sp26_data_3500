"""
This problem was asked by Google 

Given a list of numbers, and a number 'k', return whether any two numbers from the list add up to 'k'

For example: [10, 15, 3, 7], k = 17 print out "yes" or "true" since 10 + 7 = 17

"""

# augmented assignment
age = 14
age = age + 1
age += 1
print("age:", age)
age -= 1
print("age:", age)
age *= 1
print("age:", age)
age /= 1
print("age:", age)
age %= 2
print("age:", age)
age //= 1
print("age:", age)
age **= 2
print("age:", age)

num_miles = 0

while num_miles < 20:
    print("not done running yet...")
    num_miles += 1

# for loops

name = "Clayton Stoddard"
for x in name:
    print("letter:", x)

for i in range(10):
    print("i:", i)

names = ["Alexandra", "Lily", "Ronald"]

for name in names:
    print("name:", name)
    for character in name:
        print("character:", character)
    break

# for loop only runs as many times as specified unless we break
# a while loop runs forever unless we break or the condition becomes false

# pseudocode
# 0. variable to keep loop going
# 1. set up a loop to have the user keep guessing
# 2. create variables to track user guesses
# 3. compare guess to actual number
# 4. print responses for each guess
# 5. if they get it right, make the loop stop

import random
secret_num = random.randint(1, 100)

for i in range(10):
    guess = int(input("Enter your guess: "))

    if guess > secret_num:
        print("Too high!")
    elif guess < secret_num:
        print("Too low!")
    else:
        print("You got it!")
        break

    if i == 9:
        print("You are out of guesses")

# count even numbers
evens = 0

for i in range(2, 21, 2):
        print("i:", i)

# print("there are", counter, "even numbers between 1 and 20")