#!/usr/bin/env python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

user_id = argv[1]
url = 'https://jsonplaceholder.typicode.com/'
# GET  METHOD
user = requests.get('{}users?id={}'.format(url, user_id)).json()[0]
request = requests.get('{}todos?userId={}'.format(url, user_id)).json()
name = user.get('name')
tasks = len(request)
# Method : List Comprehension
task_list = [todo.get("title") for todo in request if todo.get('completed')]
tasks_todo = len(task_list)
string = "Employee {} is done with tasks({}/{}):"
print(string.format(name, tasks, tasks_todo))
[print("\t{}".format(i)) for i in task_list]
