#!/usr/bin/python3
"""
JSON export
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_Id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_Id)
    response = requests.get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
        format(employee_Id)
    response = requests.get(url)
    tasks = response.json()
    dict = {employee_Id: []}
    for task in tasks:
        dict[employee_Id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "name": name
                                    })
    with open('{}.json'.format(employee_Id), 'w') as file:
        json.dump(dict, file)
