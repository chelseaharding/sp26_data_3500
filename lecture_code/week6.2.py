# random numbers

import random

# random.randint()
# random.randrange()

# files

file = open("/workspaces/sp26_data_3500/lecture_code/spectrum_magic.txt")
# print("file:", file)
file_lines = file.readlines()
# print("lines of the file:", file_lines)

# open numbers.txt

file = open("/workspaces/sp26_data_3500/lecture_code/numbers.txt")
numbers_lines = file.readlines()
sum = 0
for number in numbers_lines:
    # print("number:", number)
    sum += int(number)

avg = sum/len(numbers_lines)
print("avg:", avg)

# create a new file

"""
3 ways to open a file:
    1. read mode   (r)
    2. write mode  (w)
    3. append mode (a)
"""

thursday_file = open("/workspaces/sp26_data_3500/lecture_code/thursday.txt", "a")

# for line in file_lines:
#     file.write(line)

thursday_file.writelines(file_lines)

thursday_file.write("\n" + str(avg))
thursday_file.close()

