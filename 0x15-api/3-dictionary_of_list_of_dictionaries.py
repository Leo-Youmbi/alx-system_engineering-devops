#!/usr/bin/python3
"""Returns todo list information for a given ID."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    with open('todo_all_employees.json', 'w') as jsonFile:
        data = {}
        for user in users:
            data[user['id']] = [{
                            'username': user["username"],
                            'completed': todo['completed'],
                            'task': todo['title']
                        } for todo in todos if todo['userId'] == user['id']]
        json.dump(data, jsonFile)
