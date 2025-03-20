import json
import csv



def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)



def display_tasks(tasks):
    print("\nTasks List:")
    print("ID | Task Name        | Completed | Priority")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']}  | {task['task']:15} | {task['completed']} | {task['priority']}")



def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("\n✅ Tasks updated successfully!")



def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\n📊 Task Statistics:")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {avg_priority:.2f}")



def convert_to_csv(tasks):
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

    print("\n✅ Data successfully written to tasks.csv!")


tasks = load_tasks()
display_tasks(tasks)
calculate_stats(tasks)
convert_to_csv(tasks)
