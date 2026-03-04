# strings

# string concatenation
string1 = "hello"
string2 = "world"

print(string1 + string2)
print(string1, string2)

age = 20
name = "Steve"
sentence = "Hi, my name is " + name + " and I am " + str(age) + " years old."
print(sentence)

# with open("creativity.txt", "w") as file:
#     file.write("Hi, my name is", name, "and I am ", str(age), " years old.")

fruit = "apple"
fruit *= 20
print(fruit)

# string whitespace
name = "          Big Blue          "
print(name)
name.rstrip()
name.lstrip()
name.strip()

print(name.strip())

# string capitalize and such
print(name.strip().capitalize())
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.istitle())
print(name.isdigit())

name = "professor H"
name2 = "Professor H"

print(name.lower() == name2.lower())

paragraph = "Today is Wednesday and I sometimes don't like those days because I want it to be the end of the week and it's only the middle. Also, I feel like Wednesday is literally mid. Adding in a sentence to make this complete."

# split function
string = "i"
words = paragraph.split(string.upper())
print("words:", words)

count = 0
for word in words:
    for char in word:
        if char.lower() == "a":
            count += 1

# print("count:", count)



