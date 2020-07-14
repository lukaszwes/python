import requests
import json
import webbrowser
from datetime import datetime, timedelta
from pprint import pprint

one_week  =timedelta(days = 7)
today = datetime.today()

one_week_ago = today - one_week
one_week_ago = int(one_week_ago.timestamp())
# print(one_week_ago)

"""
minimum 10 punktow (score)
posegregowane malejasco
z ostatniego tygodnia
kategorii python

"""

params = {
    "site"     : "stackoverflow",
    "sort"     : "votes",
    "order"    : "desc",
    "fromdate" : one_week_ago,
    "tagged"   : "python",
    "min"      : "10"
}


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecoderError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])


