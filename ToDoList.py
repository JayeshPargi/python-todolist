tasks = []  # list to store tasks
filename = "tasks.txt"  # file where tasks will be saved

# Load previous tasks from file when program starts
try:
    with open(filename, "r") as file:
        tasks = file.read().splitlines()  # read each line as a task
except FileNotFoundError:
    tasks = []  # if file doesn’t exist yet, start with empty list

# Ensure the file exists, even if empty
open(filename, "a").close()


# Save tasks to file
def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)  # save task in list
    save_tasks()  # save immediately after adding
    print(f"✅ Task added: {task}")


# View all tasks
def view_tasks():
    if not tasks:  # check if list is empty
        print("📭 No tasks yet.")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):  # show numbered list
            print(f"{i}. {task}")


# Remove a task
def remove_task():
    view_tasks()  # show tasks first
    if tasks:  # only allow removing if tasks exist
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):  # valid range
                removed = tasks.pop(num - 1)  # remove by index
                save_tasks()  # save immediately after removing
                print(f"❌ Task removed: {removed}")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")


# Main loop
while True:
    print("\n---- To-Do List Menu ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_tasks()  # final save before quitting
        print("👋 Goodbye! Your tasks are saved in tasks.txt")
        break
    else:
        print("⚠️ Invalid choice, please select 1-4.")
