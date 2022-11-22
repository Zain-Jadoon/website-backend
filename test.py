import requests
import json
base_url = "http://localhost:5000/transact"
obj = {
    "from":"Zain",
    "from_passwd":"hello",
    "to":"Zaid",
    "ammount":100
}
for x in range(5):
    responce = requests.post(base_url, json.dumps(obj))
    print(responce.json())
