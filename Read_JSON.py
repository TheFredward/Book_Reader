# Initial imports requests and json
import requests
import json
from _collections import OrderedDict

# function to store request list to a list


def title_description_list():
    """Create a list with the title and description only using the most recent list"""
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


def sort_list(user_choice, current_list):
    """Will use this for buttons and to format the list from
        title_description_list() per user request"""
    if user_choice == 'Favorites':
        return 1
    elif user_choice == 'A to Z':
        return sorted(current_list, key=lambda i: i['title'])
    elif user_choice == 'Z to A':
        return sorted(current_list, key=lambda i: i['title'], reverse=True)
    else:
        print("Most Recent is standard")

# Get the requests from the initial api, unsorted
# Id in the json gets the specific title
r = requests.get("https://api.j-novel.club/api/series/")
json_initial_request = json.loads(r.text)

sorted_list = title_description_list()
# Checking of sorted() is correct
fav_list = sort_list('Favorites', sorted_list)
a_z_list = sort_list('A to Z', sorted_list)
z_a_list = sort_list('Z to A', sorted_list)
print('------')
print(a_z_list[0]['title'])
print('------')
print(z_a_list[0]['title'])
print('------')
print(fav_list)
print('------')


