import json
import csv
import os

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class TaskManager:
    def __init__(self, storage):
        self.tasks = []
        self.storage = storage
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title if title else task.title
                task.description = description if description else task.description
                task.due_date = due_date if due_date else task.due_date
                task.status = status if status else task.status
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if not filtered_tasks:
            print("No tasks with this status.")
        for task in filtered_tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load()

class CSVStorage:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self):
        if not os.path.exists(self.filename):
            return []
        tasks = []
        with open(self.filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                task = Task(row[0], row[1], row[2], row[3], row[4])
                tasks.append(task)
        return tasks

class JSONStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            data = json.load(file)
            return [Task(task["task_id"], task["title"], task["description"], task["due_date"], task["status"]) for task in data]

# Choose storage format: CSV or JSON
storage = CSVStorage()  # Change to JSONStorage() if needed
task_manager = TaskManager(storage)

while True:
    print("\nWelcome to the To-Do Application!")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Filter tasks by status")
    print("6. Save tasks")
    print("7. Load tasks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(task_id, title, description, due_date, status)
        task_manager.add_task(task)

    elif choice == "2":
        task_manager.view_tasks()

    elif choice == "3":
        task_id = input("Enter Task ID to update: ")
        title = input("Enter new title (or press Enter to skip): ")
        description = input("Enter new description (or press Enter to skip): ")
        due_date = input("Enter new due date (or press Enter to skip): ")
        status = input("Enter new status (or press Enter to skip): ")
        task_manager.update_task(task_id, title or None, description or None, due_date or None, status or None)

    elif choice == "4":
        task_id = input("Enter Task ID to delete: ")
        task_manager.delete_task(task_id)

    elif choice == "5":
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        task_manager.filter_tasks(status)

    elif choice == "6":
        task_manager.save_tasks()

    elif choice == "7":
        task_manager.load_tasks()
        print("Tasks loaded successfully!")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
