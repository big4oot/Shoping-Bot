import requests
import json

headers = {
    'content-type': "application/json",
    'x-apikey': "",
    'cache-control': "no-cache"
    }

def get_lists(user_id):
    url = "https://practice-2abd.restdb.io/rest/lists?filter=" + str(user_id)
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)

def get_formatted_lists(user_id):
    lists = get_lists(user_id)
    msg = "Ваши списки:\n"
    n = 1
    for _list in lists:
        msg += f"{n}. {_list['list_title']}\n"
        n += 1
    msg += "Выберите номер списка"
    return msg, len(lists)

