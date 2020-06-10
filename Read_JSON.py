# Initial imports requests and json
import requests
import json
# Get the requests from the initial api, unsorted
r = requests.get("https://api.j-novel.club/api/series/")
json_initial_request = json.loads(r.text)
print(len(json_initial_request))
print(json_initial_request)

