"""
Programming Activity 1

 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""

apple_price = 1.28
num_purchased = 5
tax = 1.07
total_bill = apple_price * num_purchased * tax

print("you bought", num_purchased, "apples for", apple_price, "a piece. Your total bill was", total_bill)