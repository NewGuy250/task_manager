def load_tasks(filename):
    # Load tasks from a file into a dictionary.
    try:
        with open(filename, 'r') as file:
            tasks = {i + 1: line.strip() for i, line in enumerate(file)}
        return tasks
    except FileNotFoundError:
        return {}

def save_tasks(tasks, filename):
    # Save tasks from a dictionary to a file.
    with open(filename, 'w') as file:
        for task in tasks.values():
            file.write(task + '\n')

def reindex_tasks(tasks):
    # Reindex tasks to maintain continuous numbering.
    return {i + 1: task for i, task in enumerate(tasks.values())}

filename = 'tasks.txt'
tasks = load_tasks(filename)

print("\nWelcome to the To-Do List Manager!\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit\n")

while True:
    # Get user input
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Action
    if choice == 1:  # Add Task
        task = input("Enter a task: ")
        tasks[len(tasks) + 1] = task
        save_tasks(tasks, filename)  # Save tasks to file
        print("Task added!\n")

    elif choice == 2:  # View Tasks
        if tasks:
            for key, value in tasks.items():
                print(f"{key}. {value}")
            print("")
        else:
            print("No tasks available.\n")

    elif choice == 3:  # Delete Task
        if tasks:
            try:
                delete = int(input("Enter task number to delete: "))
                if delete in tasks:
                    del tasks[delete]
                    print("Task deleted!\n")
                    tasks = reindex_tasks(tasks)  # Reindex after deletion
                    save_tasks(tasks, filename)  # Save tasks to file
                else:
                    print("Error: Task number does not exist.\n")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.\n")

    elif choice == 4:  # Exit
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Enter a number 1-4.\n")
