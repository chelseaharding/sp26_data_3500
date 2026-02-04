# # functions

# """
# 1 - modularity - smaller more manageable chunks
# 2 - readability - helps us read code easier
# 3 - testing - easier to find bugs 
# 4 - organization - organizes code
# """

# """
# Functions need 4 things:
# 1 - definition/name
# 2 - arguments/parameters
# 3 - main body of code
# 4 - return statement :)
# """

# degrees = int(input("What's the temperature in F: "))

# def f_to_c(degrees_f):
#     degrees_c = (degrees_f - 32) * (5/9)
#     print(degrees_c)

# f_to_c(degrees)

# def c_to_f(degrees_c):
#     degrees_f = degrees_c * (9/5) + 32
#     return(degrees_f)


# def secret_num_game():
#     import random
#     secret_num = random.randint(1, 100)

#     not_guessed = True

#     while not_guessed == True:
#         guess = int(input("Enter your guess: "))

#         if guess > secret_num:
#             print("Too high!")
#         elif guess < secret_num:
#             print("Too low!")
#         else:
#             print("You got it!")
#             not_guessed = False

# secret_num_game()

# # function arguments


# function defaults

print()

# can the child sit in the front seat?

age = int(input("How old is child: "))
weight = int(input("How much does child weight: "))


def front_seat_check(age=10, weight=50):
    criteria_1 = age > 12
    criteria_2 = age == 11 and weight > 90
    criteria_3 = age < 11 and weight > 100

    if criteria_1 or criteria_2 or criteria_3:
        return "The child can sit in the front seat"
    else:
        return "The child cannot sit in the front seat"
    
print(front_seat_check(age, 91))

