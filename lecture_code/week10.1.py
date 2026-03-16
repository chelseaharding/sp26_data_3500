"""
Given an even number (greater than 2), return two prime numbers whoes sum will be equal to the given number.

A solution will ALWAYS exist :) (see Goldbach's Conjecture)

Example:

Input: 8
Output: 3 + 5 = 8

*note* 
This is sort of challenging so you can start by just writing a function is_prime(num) which returns if a number is prime or not
"""
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_prime_pairs():
    # later :)
    pass


# String substrings
emojis = "👀😍💞🥰🤣😭🥹🫂💖😬"

message = "I love Python 😍😍💞💖"

new_emojis = [char for char in message if char in emojis]
print(new_emojis)

letters = ["z", "t", "c", "l"]

if "l" in letters:
    print("l is in letters")

word1_list = ["l", "e", "a", "d"]
word2_list = ["d", "a", "l", "e"]

for letter in word1_list:
    if letter in word2_list:
        pass

# String Replacing

sentence = "Our offices are in New York and California."

sentence = sentence.replace("New York", "NY")
sentence = sentence.replace("California", "CA")

print("sentence:", sentence)

# activity with tweets.txt
"""
1 - read in the file
2 - get rid of @VirginAmerica
3 - find the average length of all the tweets

"""

file = open("/workspaces/sp26_data_3500/lecture_code/tweets.txt")
lines = file.readlines()

total = 0

#step 2
for line in lines:
    tweet = line.replace("@VirginAmerica", "")
    # step 3
    total += len(tweet)

print("the average tweet length is:", total/len(lines))
