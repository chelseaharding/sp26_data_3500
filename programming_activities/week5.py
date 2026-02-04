"""
Programming Activity 4

Write a function named "welcome_fctn" which takes one argument, called "name".  Inside the function, print to the console "Welcome " name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome " name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""

"""
Programming Activity 5

Update the function in activity one, and create a new string variable in the function called, welcome_message. The variable welcome_message should be 
assigned the value "Welcome " name. The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""

"""
Programming Activity 6

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""




# 3.9
# we know the user input has to be between 7 - 10
user_input = int(input("Enter a number that is 7 to 10 digits long: "))

big_num = 10000000000

while big_num > 1:
    if big_num > user_input:
        big_num /= 10

# 3.14
sum = 0
denom = 1
for i in range(1, 3000):
    if i % 2 == 0:
        sum -= 4/denom
    else:
        sum += 4/denom
    denom += 2