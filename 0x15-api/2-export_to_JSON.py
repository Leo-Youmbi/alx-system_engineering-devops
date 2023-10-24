#!/usr/bin/python3
"""Returns todo list information for a given ID."""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]

    with open(f'{user_id}.json', 'w') as jsonFile:
        data = {user_id: []}
        for todo in todos:
            data[user_id].append(
                {'task': todo['title'],
                 'completed': todo['completed'],
                 'username': user_name})
        json.dump(data, jsonFile)
