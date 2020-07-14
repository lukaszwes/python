import requests
import json
import webbrowser
from pprint import pprint

params ={
    "breed_ids" : "acur",
    "limit"     : 3
}


r = requests.get("https://api.thecatapi.com/v1/images/search?", params)

questions = r.json()

for item in questions:
    # pprint(item["url"])
    webbrowser.open_new_tab(item["url"])