# web JSON APIs

import json
import requests

# url = "https://v2.jokeapi.dev/joke/Programming"

# request = requests.get(url)
# print(type(request.text))
# dictionary = json.loads(request.text)
# # print(dictionary)


new_url = 'https://api.datamuse.com/words?rel_trg=cow'

request = requests.get(new_url)
dictionary_list = json.loads(request.text)
# print(dictionary_list)

for dictionary in dictionary_list:
    # print(dictionary)
    if dictionary["word"] == "cheese":
        print(dictionary["word"], dictionary["score"])

