#!/usr/bin/python3
"""
export all employees
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            use.get("id"): [{
                "task": tos.get("title"),
                "completed": tos.get("completed"),
                "username": use.get("username")
            } for tos in requests.get(url + "todos",
                                    params={"userId": use.get("id")}).json()]
            for use in users}, jsonfile)
