import requests
import json
from pprint import pprint

params = {
    "api_key"  : "d3123200062e5d472498a849b790c73444fe4464",
    "country"  : "pl",
    "year"     : "2020"

}


r = requests.get("https://calendarific.com/api/v2/holidays", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("incompatible json format input")
else:
    for kay, holidays in questions["response"].items():
        print("Liczba swiat w Polsce: ", len(holidays))
        for idx, holiday in enumerate(holidays):
            print(idx+1, "\t", ((holiday["date"])["iso"])[0:10], "\t", holiday["description"])
