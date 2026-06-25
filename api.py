import requests
import sys
import json 

method, url = sys.argv[1], sys.argv[2]

if method == "GET":
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    print(json.dumps(r.json(), indent=2))