#!/usr/bin/python3
"""This is a call to a REST API"""

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
    with open(f"{emp_id}.csv", "w") as files:
        for task in todo_data:
            files.write(f'"{emp_id}","{user_data.get("username")}",'
                        f'"{task.get("completed")}","{task.get("title")}"\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)
    return_employee_info(sys.argv[1])
