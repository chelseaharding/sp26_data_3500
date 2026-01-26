# # dynamic types
# x = 1
# x = "aggie basketball"
# x = True

# print(type(x))

# # input
# age = input("Please enter your age: ")
# print(type(age))

# print("on your next birthday you will be", int(age) + 1)

# # input example:
# f_a_b_p = int(input("Enter the number of your favorite aggie basketball player: "))
# print(type(f_a_b_p))

# # casting 
# # int()
# # str()
# # float()
# # bool()
# # eval() # tries to figure out the best type

# # if
age = 12

# if age > 20:
#     print("The twenties are the best years of your life")
# if age >= 13: # false
#     print("You are a teenager. Have fun :)")
# else:
#     print("You are still a child :)")


if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# hurd premium

student = input("Are you a current USU student: (Y/N)")
hurdP = input("Do you have Hurd Premium: (Y/N)")

if student == "Y":
    print("You get into the game free!")
if hurdP == "Y":
    print("You get into the game 15 minutes early!")
else:
    print("You need to buy a ticket. They're not too expensive!")

# min, max, range

# grades = [89, 56, 90, 0, 5]

# print("min:", min(grades))
# print("max:", max(grades))

# range(10)


# half marathon 
"""
Adam is running a half marathon. His avg mile time is 5:55.
For the half (13.1), what is his projected finish time?
Output the result in this format:
"Time: hr:min:sec"
"""

minute = 5
sec = 55
pace_seconds = sec + (minute * 60)
print("pace in seconds:", pace_seconds)

total_half_sec = pace_seconds * 13.1
print("total time in seconds for the half:", total_half_sec)

projected_hours = total_half_sec // 3600
# print("projected hours:", projected_hours)

projected_minutes = (total_half_sec % 3600) // 60
# print("projected minutes:", projected_minutes)

projected_seconds = total_half_sec % 60
# print("projected seconds:", projected_seconds)

print("Time:", int(projected_hours), ":", int(projected_minutes), ":", projected_seconds)