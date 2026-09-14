# Task Tracker CLI

A simple command-line interface (CLI) application built with Python to track and manage your day-to-day tasks. Built as part of the [roadmap.sh](https://roadmap.sh/) backend developer projects.

* **Project Repository:** [https://github.com/HE1MER25/task-tracker-cli](https://github.com/HE1MER25/task-tracker-cli)

## Features
* Add new tasks with automatic unique ID generation.
* Update existing task descriptions.
* Delete tasks by ID.
* Mark tasks as `in-progress` or `done`.
* List all tasks, or filter them by status (`todo`, `in-progress`, `done`).
* Automatically renumber task IDs sequentially after modifications.
* Local data persistence using a lightweight JSON file.

## Prerequisites
* Python 3.x installed on your system.

## Getting Started
1. Clone the repository:
   git clone https://github.com/HE1MER25/task-tracker-cli.git
   cd task-tracker-cli

2. Run the script using Python:
   python tracker.py --help

## Usage & Commands
Here are the commands you can use in your terminal:

### 1. Add a Task
python tracker.py add "Buy groceries"

### 2. List Tasks
python tracker.py list
python tracker.py list done

### 3. Update a Task Description
python tracker.py update 1 "Buy groceries and cook dinner"

### 4. Mark Task Status
python tracker.py mark-in-progress 1
python tracker.py mark-done 1

### 5. Delete a Task
python tracker.py delete 1

### 6. Renumber Tasks
python tracker.py renumber

### 7. Reorder Tasks
python tracker.py reorder 2 1
* Important Rule: You must provide all active task IDs when reordering. If you have 2 tasks, you must pass both IDs in your new sequence (e.g., reorder 2 1). If you have 3 tasks, you must pass all three (e.g., reorder 3 1 2).

## License
This project is open-source and available under the MIT License.