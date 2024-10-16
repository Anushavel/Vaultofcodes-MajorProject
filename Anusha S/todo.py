import json

class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(title={self.title}, completed={self.completed})"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    print("Saving tasks...")  # Debugging
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)
    print("Tasks saved successfully.")  # Debugging

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = [Task(**data) for data in json.load(f)]
            print(f"Loaded tasks: {tasks}")  # Debugging
            return tasks
    except FileNotFoundError:
        print("tasks.json not found. Starting with an empty task list.")  # Debugging
        return []
    except json.JSONDecodeError:
        print("tasks.json is empty or corrupted. Starting with an empty task list.")  # Debugging
        return []

# Main function for user interaction
def main():
    tasks = load_tasks()  # Load tasks when the program starts

    while True:
        # Display options
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        # Get user choice
        choice = input("Choose an option: ")

        if choice == '1':  # Add a new task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            tasks.append(Task(title, description, category))
            print("Task added successfully.")

        elif choice == '2':  # View all tasks
            if tasks:
                for idx, task in enumerate(tasks):
                    status = "✓" if task.completed else "✗"
                    print(f"{idx + 1}. {task.title} [{task.category}] - {status}")
            else:
                print("No tasks available.")

        elif choice == '3':  # Mark a task as completed
            if tasks:
                task_num = int(input("Enter task number to mark completed: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num].mark_completed()
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to complete.")

        elif choice == '4':  # Delete a task
            if tasks:
                task_num = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_num < len(tasks):
                    del tasks[task_num]
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
            else:
                print("No tasks to delete.")

        elif choice == '5':  # Exit and save tasks
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

main()