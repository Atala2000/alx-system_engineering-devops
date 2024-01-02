#!/usr/bin/python3
"""
Uses REST API and extends from the previous
information to display more
"""
import csv
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

    file_name = f'{employee_Id}.csv'
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for task in tasks:
            csv_writer.writerow([employee_Id, name,
                                 task.get('completed'), task.get('title')])
