import http.client
import json
from PIL import Image
import requests

conn = http.client.HTTPSConnection("digimoncard.io")
payload = ''
headers = {}
conn.request("GET", "/api-public/search.php?n=Gorillamon&sort=code&sortdirection=asc&series=Digimon%20Card%20Game", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

data = json.loads(data)
dataLen = len(data)
image_url = data[0]['image_url']
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
print(data[0]['image_url'])

#with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)
# also try with no indent var
