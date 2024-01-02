#!/usr/bin/python3
"""
export all employees
"""
import json
import requests

if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_url)
    users = users_response.json()

    all_tasks_dict = {}

    for user in users:
        user_id = user['id']
        username = user['name']

        tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
            format(user_id)
        tasks_response = requests.get(tasks_url)
        tasks = tasks_response.json()

        user_tasks = [{"username": username, "task": task['title'],
                       "completed": task['completed']} for task in tasks]

        all_tasks_dict[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks_dict, file)
