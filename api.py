import requests
import sys
import json 

method, url = sys.argv[1], sys.argv[2]

if method == "GET":
    try:
        r = requests.get(url)
        print(f"Status Code: {r.status_code}\n")
        try:
            print(json.dumps(r.json(), indent=2))

        except ValueError:
            print("Response is not valid JSON")
            print(f"Response content: {r.text}")

    except requests.RequestException as e:
        print(f"Error: {e}")
