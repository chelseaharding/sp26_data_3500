# split and join 

text = "I really love Aggie Basketball. They can totally beat Villanova."

words = text.split(" ")

print("words:", words)

# .join

paragraph = "👀".join(words)
print("paragraph:", paragraph)

# person data
person_data = ["Bob", "Bobson", "56", "Engineer", "Athens"]

with open("person_data.csv", "w") as file:
    file.write(", ".join(person_data))

# char test

string = "pAssword123"

print(string.isalnum())

password = input("Enter your password. Password must contain 8 letters or numbers but no special characters: ")

if password.isalnum() and len(password) >= 8:
    print("password is acceptable")
else:
    print("try another password")