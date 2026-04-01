# # handling exceptions

# try: 
#     2/0
# except:
#     print("You can't divide by zero :(")

# try:
#     with open("python.py", "r") as file:
#         print(file.readlines())
# except:
#     print("that file does not exist")

# # creating a json file
# import json

# person = {}

# person["full_name"] = "Jonas Lockhart"
# person["car"] = "Ford Focus"
# person["grade"] = "So"
# person["classes"] = ["DATA3500", "DATA3300", "DATA3330", "DATA3400", "BUS1700"]

# json.dump(person, open("/workspaces/sp26_data_3500/lecture_code/jonas.json", "w"), indent=2)

# # load a json file

# jonas = json.load(open("/workspaces/sp26_data_3500/lecture_code/jonas.json"))

# try:
#     # print(jonas["full_name"])
#     jonas["classes"].append("PE1750")
#     print(jonas["classes"])
# except:
#     print("")

# for class_ in jonas["classes"]:
#     print(class_)


# json url
import json
import requests

url = "https://v2.jokeapi.dev/joke/Programming"

request = requests.get(url)
joke_dictionary = json.loads(request.text)

# print(joke_dictionary)
try:
    print(joke_dictionary["setup"])
    input("press enter to hear the punchline")
    print(joke_dictionary["delivery"])
except:
    print(joke_dictionary["joke"])