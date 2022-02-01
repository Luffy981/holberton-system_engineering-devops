#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


def GET_Api():
    """ GET data from API"""
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    # GET  METHOD
    user = requests.get('{}users?id={}'.format(url, user_id)).json()[0]
    request = requests.get('{}todos?userId={}'.format(url, user_id)).json()
    name = user.get('username')
    tasks = len(request)
    # Method : List Comprehension
    task_list = [todo.get("title") for todo in request
                 if todo.get('completed')]
    tasks_todo = len(task_list)
    string = "Employee {} is done with tasks({}/{}):"
    print(string.format(name, tasks_todo, tasks))
    [print("\t {}".format(i)) for i in task_list]
    list_dict = []
    for todo in request:
        dict_to_csv = {}
        dict_to_csv = {
            'USER_ID': user_id,
            'NAME': name,
            'TASK': str(todo.get('completed')),
            'TITLE': str(todo.get('title'))
        }
        list_dict.append(dict_to_csv)
    filename = "{}.csv".format(user_id)
    columns = ['USER_ID', 'NAME', 'TASK', 'TITLE']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=columns, quoting=csv.QUOTE_ALL)
        writer.writerows(list_dict)


if __name__ == "__main__":
    GET_Api()
