import json
import pprint 
import requests

#webpage url
URL = r"https://api.covidtracking.com/v1/us/daily.json"

WEB = requests.get(url = URL).json()

dates, cases = [2020, 2021, 2022], []

first, second, third = 0, 0, 0

for i in range(419, 0, -1):
    if str(WEB[i]['date']).startswith("2020"):
        if WEB[i]["positive"]:
            first += WEB[i]["positive"]
        
    if str(WEB[i]['date']).startswith("2021"):
        if WEB[i]["positive"]:
            second += WEB[i]["positive"]
        
    if str(WEB[i]['date']).startswith("2022"):
        if WEB[i]["positive"]:
            third += WEB[i]["positive"]


cases.append(first / 1e6)
cases.append(second / 1e6)
cases.append(third / 1e6)



#pprint.pprint(first)
#pprint.pprint(second)
#pprint.pprint(third)
