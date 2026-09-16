# Task Tracker CLI

A simple command-line interface (CLI) application built with Python to track and manage your day-to-day tasks interactively. Built as part of the [roadmap.sh](https://roadmap.sh/projects/task-tracker/) backend developer projects.

* **Project Repository:** [https://github.com/HE1MER25/task-tracker-cli](https://github.com/HE1MER25/task-tracker-cli)

## Features
* Interactive welcome menu with guided step-by-step prompts.
* Add new tasks with automatic unique ID generation and timestamps.
* Update existing task descriptions.
* Delete tasks by ID.
* Mark tasks as `pending`, `in-progress`, or `done`.
* List all tasks, or filter them by their status.
* Automatically renumber task IDs sequentially.
* Manually reorder tasks by sequence.
* Local data persistence using a lightweight JSON file.

## Prerequisites
* Python 3.x installed on your system.

## Getting Started
1. Clone the repository:
   git clone https://github.com/HE1MER25/task-tracker-cli.git
   cd task-tracker-cli

2. Launch the interactive application:
   python tracker.py

## Interactive Menu Options
When you run the script, you will be greeted with an interactive menu. Simply type a number from **1 to 9** to perform actions:

1. **Add a Task:** Prompts you to enter a description and saves it with a unique ID.
2. **List Tasks:** Displays all tasks or lets you filter by status (`pending`, `in-progress`, `done`).
3. **Update a Task Description:** Prompts for the Task ID and the new text.
4. **Delete a Task:** Prompts for the Task ID to remove it from storage.
5. **Mark Task as In-Progress:** Updates the target task status to `in-progress`.
6. **Mark Task as Done:** Updates the target task status to `done`.
7. **Renumber Tasks:** Automatically cleans up IDs to be sequential (1, 2, 3...).
8. **Reorder Tasks:** Prompts for all active task IDs in your desired new sequence (e.g., `2 1 3`).
   * *Important Rule:* You must provide all active task IDs when reordering.
9. **Exit:** Safely closes the application.

## Project Structure
```text
task-tracker-cli/
│
├── tracker.py       # Main Python script containing interactive menu logic
├── tracker.json     # Local data store (generated automatically)
└── README.md        # Project documentation