"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""

"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random

rand_nums = []
for i in range(10):
    rand_nums.append(random.randint(1, 100))

"""
Programming Activity 4 

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""
count = 0
print(rand_nums)
for num in rand_nums:
    if count > 0:
      # print("num:", rand_nums[count])
      # print("previous num:", rand_nums[count - 1])
      if rand_nums[count] % 2 == 0 and rand_nums[count - 1] % 2 == 0:
            print(rand_nums[count])
            print(rand_nums[count -1])
            print("two evens in a row")
    count += 1