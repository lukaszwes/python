import requests
import json
import webbrowser
from datetime import datetime, timedelta
from pprint import pprint


animals ={
    "pies" : "dog",
    "kot"  : "cat"
}


input = input("Wybierz rodzaj zwierzecia (pies lub kot): ")

if input == "pies":
    type = animals[input]
elif input == "kot":
    type = animals[input]
else:
    print("wWrowadziles niepoprawna nazwe zwierzecia")
    exit()

# type = "cat"

params = {
    "amount"      : 5,
    "animal_type" : type
}

r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("nieprawidlowy format json")
else:
   print(params["amount"], "faktow na temat wybranego wierzecia: ")
   for cat in content:
        print(cat["text"])