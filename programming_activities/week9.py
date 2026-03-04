"""
Programming Activity 1

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""

evens = [i for i in range(2, 101, 2)]
print("evens", evens)


"""
Programming Activity 2

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""



"""
Programming Activity 3

Write a Python program which asks the user their name.  
Store their name in a string variable. Use the Upper() function to make all of the letters in their name upper case. Then, print to the console: 
welcome, NAME ALLCAPS!.
 - using input get the user name
 - change the string to be all upper case
 - print to the console: "welcome, NAME ALLCAPS!" (adding an exclamation
"""

"""
Programming Activity 4

Create a variable that stores the sentence below, and print the sentence to the console, before making any changes. Change the first letter in the sentence to be capitalized. Change the first instance of Whoa to be whoa (all lower case), and the second instance of Whoa to be WHOA(all upper case).  
Append a exclamation point to the end of the sentence. 
Then re-print the sentence to the console.

sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"
 - using the string variable sentence, change the first letter to upper 
   case using capitalize()
 - create a list called "words" that stores all the words in the sentence 
   in a list using the split() function.
 - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
 - append an exclamation point.
 - print the new sentence.
"""
sentence = "dude, I just biked down that mountain and at first I was like Whoa and then I was like Whoa"

words = sentence.split()

first_whoa = False

for i in range(len(words)):
    print(words[i])

    if words[i].lower() == "whoa" and first_whoa == False:
        words[i] = words[i].lower()
        first_whoa = True
    if words[i].lower() == "whoa" and first_whoa == True:
        words[i] = words[i].upper()


new_sentence = ""
for word in words:
    new_sentence = new_sentence + word + " "

print(new_sentence)
