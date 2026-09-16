import os
import json
from datetime import datetime

FILENAME = "tracker.json"

# Load tasks from the JSON file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the tracker file.")
        return []

# Save the task list into the JSON file
def save_tasks(tasks):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except IOError:
        print("Error: Failed to write to the tracker file.")

# Add a new task with a unique ID and timestamps
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

# Update an existing task's description or status
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

# Delete a task by its ID
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Error: Task with ID {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task with ID {task_id} deleted successfully.")

# Change the status of a specific task (e.g., in-progress, done)
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

# Display all tasks or filter them by status
def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task["status"] == status_filter]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['created_at'][:10]}, Updated At: {task['updated_at'][:10]}")

# Reorder tasks based on a custom sequence of IDs provided by the user
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

# Automatically reassign sequential IDs (1, 2, 3...) based on current order
def renumber_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to renumber.")
        return
    for index, task in enumerate(tasks):
        task["id"] = index + 1
    save_tasks(tasks)
    print("Tasks renumbered successfully.")

# Main command-line argument parser and dispatcher
def main():
    while True:
        print("\n==============================")
        print("    WELCOME TO TASK TRACKER   ")
        print("==============================")
        print("1. Add a Task")
        print("2. List Tasks")
        print("3. Update a Task Description")
        print("4. Delete a Task")
        print("5. Mark Task as In-Progress")
        print("6. Mark Task as Done")
        print("7. Renumber Tasks")
        print("8. Reorder Tasks")
        print("9. Exit")
        
        choice = input("\nChoose an option (1-9): ").strip()
        
        if choice == '1':
            desc = input("Enter task description: ").strip()
            if desc:
                add_task(desc)
            else:
                print("\n[Error] Description cannot be empty.")
            input("\nPress Enter to continue...")
                
        elif choice == '2':
            print("\nFilter options: [1] All [2] pending [3] in-progress [4] done")
            f_choice = input("Select filter view (press Enter for all): ").strip()
            if f_choice == '2':
                list_tasks("pending")
            elif f_choice == '3':
                list_tasks("in-progress")
            elif f_choice == '4':
                list_tasks("done")
            else:
                list_tasks()
            input("\nPress Enter to continue...")
                
        elif choice == '3':
            try:
                task_id = int(input("Enter the Task ID to update: "))
                desc = input("Enter the new description: ").strip()
                if desc:
                    update_task(task_id, desc)
                else:
                    print("\n[Error] Description cannot be empty.")
            except ValueError:
                print("\n[Error] Task ID must be a valid number.")
            input("\nPress Enter to continue...")
                
        elif choice == '4':
            try:
                task_id = int(input("Enter the Task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("\n[Error] Task ID must be a valid number.")
            input("\nPress Enter to continue...")
                
        elif choice == '5':
            try:
                task_id = int(input("Enter the Task ID to mark as in-progress: "))
                mark_task(task_id, "in-progress")
            except ValueError:
                print("\n[Error] Task ID must be a valid number.")
            input("\nPress Enter to continue...")
                
        elif choice == '6':
            try:
                task_id = int(input("Enter the Task ID to mark as done: "))
                mark_task(task_id, "done")
            except ValueError:
                print("\n[Error] Task ID must be a valid number.")
            input("\nPress Enter to continue...")
                
        elif choice == '7':
            renumber_tasks()
            input("\nPress Enter to continue...")
            
        elif choice == '8':
            ids_input = input("Enter all active task IDs in your desired new order separated by spaces (e.g. 2 1 3): ").strip()
            try:
                new_order = [int(x) for x in ids_input.split()]
                reorder_tasks(new_order)
            except ValueError:
                print("\n[Error] Please enter valid integer IDs separated by spaces.")
            input("\nPress Enter to continue...")
                
        elif choice == '9':
            print("\nThank you for using Task Tracker. Goodbye!")
            break
            
        else:
            print("\n[Error] Invalid option. Please choose a number from 1 to 9.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()