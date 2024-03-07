import json
from datetime import datetime, timedelta

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, description, priority="medium", due_date=None):
        task = {
            "description": description,
            "priority": priority,
            "due_date": due_date,
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{description}" added successfully.')

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f'Task "{removed_task["description"]}" removed successfully.')
        else:
            print("Invalid task index.")

    def mark_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print(f'Task "{self.tasks[index]["description"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("\nTask List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            due_date = f"Due on {task['due_date']}" if task["due_date"] else "No due date"
            print(f"{index + 1}. {task['description']} - Priority: {task['priority']} | Status: {status} | {due_date}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark as Completed\n4. Display Tasks\n5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ").lower()
            due_date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(description, priority, due_date)

        elif choice == "2":
            index = int(input("Enter the index of the task to remove: ")) - 1
            todo_list.remove_task(index)

        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_list.mark_as_completed(index)

        elif choice == "4":
            todo_list.display_tasks()

        elif choice == "5":
            print("Quitting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
