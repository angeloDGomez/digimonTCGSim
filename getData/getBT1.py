import http.client
import json
import requests
from urllib.parse import urlparse
import os

conn = http.client.HTTPSConnection("digimoncard.io")
payload = ''
headers = {}
conn.request("GET", "/api-public/search.php?pack=BT-01:%20Booster%20New%20Evolution&sort=code&sortdirection=asc&series=Digimon%20Card%20Game")
res = conn.getresponse()
data = res.read()
data = json.loads(data)

for i in range(len(data)):
    imgURL = data[i]['image_url']
    imgData = requests.get(imgURL).content
    imgName = urlparse(imgURL)
    imgName = os.path.basename(imgName.path)
    with open(f'/Users/Angelo/Documents/GitHub/digimonTCGSim/Assets/CardImages/BT-01/{imgName}', 'wb') as handler:
        handler.write(imgData)
with open('/Users/Angelo/Documents/GitHub/digimonTCGSim/Assets/CardData/BT-01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
