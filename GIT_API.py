import json
from pprint import pprint

import requests

url = "https://api.github.com"
user = "IvanJarunin"

r = requests.get(f"{url}/users/{user}/repos")

with open("data.json", "w") as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i["name"])


def pipeline(username):
    new_data = {}
    with open("data.json", "w") as f:
        new_data = json.dump(r.json(), f)
    return new_data
