import sys
import os
import json
from datetime import datetime

FILENAME = "tracker.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the tracker file.")
        return []

def save_tasks(tasks):
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error: Failed to write to the tracker file.")

def add_task(description):
    tasks = load_tasks()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    now = datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "created_at": now,
        "updated_at": now,
        "status": "pending"
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added with ID: {new_id}")

def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if description is not None:
                task["description"] = description
            if status is not None:
                task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} updated.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(new_tasks)
    print(f"Task with ID {task_id} deleted successfully.")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} marked as {status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task["status"] == status_filter]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at']}, Updated At: {task['updated_at']}")
def reorder_tasks(new_order):
    tasks = load_tasks()
    if len(new_order) != len(tasks):
        print("Error: The new order must include all task IDs.")
        return
    id_to_task = {task["id"]: task for task in tasks}
    try:
        reordered_tasks = [id_to_task[task_id] for task_id in new_order]
    except KeyError as e:
        print(f"Error: Task ID {e.args[0]} not found.")
        return
    save_tasks(reordered_tasks)
    print("Tasks reordered successfully.")

def renumber_task():
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        task["id"] = index + 1
    save_tasks(tasks)
    print("Tasks renumbered successfully.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python tracker.py <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Description is required for adding a task.")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Task ID and new description are required for updating a task.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        description = " ".join(sys.argv[3:])
        update_task(task_id, description=description)
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Task ID is required for deleting a task.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        delete_task(task_id)
    
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Task ID is required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        mark_task(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Task ID is required.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        mark_task(task_id, "done")

    elif command == "list":
        status_filter = None
        if len(sys.argv) > 2:
            status_filter = sys.argv[2]
            if status_filter not in ["pending", "in-progress", "done"]:
                print("Error: Status filter must be 'pending', 'in-progress', or 'done'.")
                return
        list_tasks(status_filter)
    
    elif command == "reorder":
        if len(sys.argv) < 3:
            print("Error: Provide the new order of task IDs. Usage: python tracker.py reorder <id1> <id2> <id3> ...")
            return
        try:
            # Convert all arguments after 'reorder' into integers
            new_order = [int(arg) for arg in sys.argv[2:]]
        except ValueError:
            print("Error: All task IDs must be integers.")
            return
        reorder_tasks(new_order)
    
    elif command == "renumber":
        renumber_task()

    else:
        print(f"Error: Unknown command '{command}'.")

if __name__ == "__main__":
    main()