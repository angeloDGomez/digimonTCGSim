import http.client
import json
import os
import requests
from urllib.parse import urlparse

conn = http.client.HTTPSConnection("digimoncard.io")
payload = ''
headers = {}
conn.request("GET", "/api-public/search.php?n=Gorillamon&sort=code&sortdirection=asc&series=Digimon%20Card%20Game", payload, headers)
res = conn.getresponse()
data = res.read()


data = json.loads(data)
# get the images for the two gorillamon
for i in range(len(data)):   
    image_url = data[i]['image_url']
    imgName = urlparse(image_url)
    imgName = os.path.basename(imgName.path)
    img_data = requests.get(image_url).content
    with open(f'/Users/Angelo/Documents/GitHub/digimonTCGSim/Assets/CardImages/TestRecieve/{imgName}', 'wb') as handler:
        handler.write(img_data)
    print(data[i]['image_url'])

with open('/Users/Angelo/Documents/GitHub/digimonTCGSim/Assets/CardData/BT-01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# also try with no indent var
