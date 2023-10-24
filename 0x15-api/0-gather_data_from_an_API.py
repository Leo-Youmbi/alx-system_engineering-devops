#!/usr/bin/python3
"""Api"""
import requests as req
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = req.get(url + f"/users/{sys.argv[1]}").json()
    todos = req.get(url + "/todos", params={'userId': sys.argv[1]}).json()
    completedTasks = [todo for todo in todos if todo['completed']]
    # print(user)
    # print(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'],
        len(completedTasks),
        len(todos)))
    for todo in completedTasks:
        print(f"\t {todo['title']}")
