#!/usr/bin/python3
"""Module that uses REST API to display data
"""
import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/"

employee_resources = requests.get(url + "users/" + argv[1])
employee_tasks = requests.get(url + "todos")
employee_tasks = employee_tasks.json()

employee_name = employee_resources.json().get("name")
completed_tasks = 0
total_tasks = 0
task_title = []

for x in employee_tasks:
    if x.get("userId") == int(argv[1]):
        total_tasks += 1
        if x.get("completed"):
            completed_tasks += 1
            task_title.append(x.get("title"))

print(
    f"""Employee {employee_name} is done with
tasks({completed_tasks}/{total_tasks}): """
)
for x in task_title:
    print(f"\t{x}")
