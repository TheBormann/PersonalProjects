import requests
import json
import datetime
import os

# fetch the data
response = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"
    "&sparkline=false")
print(response.status_code)

date = datetime.datetime.now().date().strftime("%Y_%m_%d")
newData = response.json()

# read json
try:
    if os.path.isdir("../../data/gathered"):
        with open("../../data/gathered/crypto.json", "r") as read_file:
            data = json.load(read_file)
            data[date] = newData
    else:
        with open("./data/gathered/crypto.json", "r") as read_file:
            data = json.load(read_file)
            data[date] = newData

except:
    data = {date: newData}

# save it
if os.path.isdir("../../data/gathered"):
    with open('../../data/gathered/crypto.json', 'w') as json_file:
        json.dump(data, json_file)
else:
    with open('./data/gathered/crypto.json', 'w') as json_file:
        json.dump(data, json_file)

