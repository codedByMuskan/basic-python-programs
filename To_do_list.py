tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({'task': task_name, 'done': False})
    print("Task added!")

def mark_complete():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        tasks[task_num - 1]['done'] = True
        print("Task marked as complete.")
    except:
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        print("Task deleted.")
    except:
        print("Invalid input!")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
