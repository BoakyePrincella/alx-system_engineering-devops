#!/usr/bin/python3
"""This is a call to a REST API"""

import json
import requests
import sys


def return_employee_info(emp_id):
    """This method returns the todo  progress of the employer"""

    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/user/{emp_id}/todos"

    req_user = requests.get(user_url)
    req_todo = requests.get(todo_url)

    if req_user.status_code != 200 or req_todo.status_code != 200:
        print("Error: Can't fetch any data from API")
        return
    user_data = req_user.json()
    todo_data = req_todo.json()

    total_task = len(todo_data)
    task_done = len([task for task in todo_data if task.get("completed")])

    task_json = []
    for task in todo_data:
        task_json.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get("username"),
            })
    with open(f"{emp_id}.json", "w") as files:
        json.dump({f"{emp_id}": task_json}, files)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)
    return_employee_info(sys.argv[1])
