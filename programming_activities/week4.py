"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta 2024
 - Gen Alpha 2010
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
useryear = int(input("what year were you born?"))
if useryear >= 1997:
    print ("you are a zoomer")
elif useryear >= 1981 and useryear < 1997:
    print ("You are a millenial")
elif useryear >= 1965 and useryear < 1981:
    print ("You are gen x.")
else:
    print ("you are a baby boomer")
"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
current_year=2026
user_age=int(input("Please enter the ageyou have turned or will turn THIS year>"))
while user_age>0:
    print(f"You were alive in {current_year}")
    user_age-=1
    current_year-=1
else:
    print(f"You were born in {current_year}")


"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""
for i in range(5, 100, 5):
    print("i:", i)

"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""

num = 5
while num < 96:
    print("num:", num)
    num += 5