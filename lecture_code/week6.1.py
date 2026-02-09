# """
# This problem was asked by Google 

# Given a list of numbers, and a number 'k', return whether any two numbers from the list add up to 'k'

# For example: [10, 15, 3, 7], k = 17 print out "yes" or "true" since 10 + 7 = 17

# """

# # lists

# numbers = [10, 15, 3, 7]
# k = 25

# def target_num(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 print("Found", target, "in number list")
#                 break


# target_num(numbers, k)


# basics
colors = ["purple", "green", "Aggie Blue", "orange", "yellow", "maroon", "brown"]
# print("colors:", colors)
colors.append("Fighting White")
# print("colors:", colors)

colors.pop(1)
# print("colors:", colors)

colors.insert(0, "pink")
# print("colors:", colors)

# search/slice and sorting lists


# for i in range(len(colors)):
#     print("colors[i]:", colors[i])

# for color in colors:
#     print("color:", color)

# normal slice (subset)
print(colors[3:5])
# just the last element
print(colors[-1:])
# reversed list
print(colors[::-1])
# every other element of list
print(colors[::2])

# list sorting
colors.sort()
print("sorted colors:", colors)

# figure out if two words are anagrams

def is_anagram(word1, word2):
    word_1_list = []
    word_2_list = []
    if len(word1) == len(word2):
        for letter in word1:
            word_1_list.append(letter)
        for letter in word2:
            word_2_list.append(letter)
        return sorted(word_1_list) == sorted(word_2_list)
    return False
    

if is_anagram("earth", "heart"):
    print("the two words are anagrams")
else:
    print("nope")
