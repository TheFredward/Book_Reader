# Initial imports requests and json
import requests
import json
from _collections import OrderedDict

# function to store request list to a list


def sortList():
    i = 0
    title_and_descr_list = [{} for sub in range(len(json_initial_request))]
    while i < len(json_initial_request):
        if 'title' in json_initial_request[i]:
            title_and_descr_list[i]['title'] = json_initial_request[i]['title']
            title_and_descr_list[i]['desc'] = json_initial_request[i]['description']
            title_and_descr_list[i]['id'] = json_initial_request[i]['id']
        else:
            title_and_descr_list[0]['title'] = 'NA'
            title_and_descr_list[0]['desc'] = 'NA'
            title_and_descr_list[0]['id'] = 'NA'
        i += 1
    return title_and_descr_list


# Get the requests from the initial api, unsorted
# Id in the json gets the specific title
r = requests.get("https://api.j-novel.club/api/series/")
json_initial_request = json.loads(r.text)
new_dict = [{} for sub in range(len(json_initial_request))]
new_dict[0]['title'] = json_initial_request[0]['title']
new_dict[0]['desc'] = json_initial_request[0]['description']

sorted_list = sortList()
print(sorted_list)

