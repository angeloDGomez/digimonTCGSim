import http.client
import json
import requests

conn = http.client.HTTPSConnection("digimoncard.io")
payload = ''
headers = {}
conn.request("GET", "/api-public/search.php?pack=BT-01:%20Booster%20New%20Evolution&sort=code&sortdirection=asc&series=Digimon%20Card%20Game")
res = conn.getresponse()
data = res.read()
data = json.loads(data)

# for i in range(len(data)):
