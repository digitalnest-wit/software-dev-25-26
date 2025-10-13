# To-Do List Manager

tasks = []

print("To-Do List Manager")
print()

# Add tasks
print("Add tasks to your to-do list.")
num_tasks = int(input("How many tasks would you like to add? "))

for i in range(num_tasks):
    task = input(f"Enter task {i + 1}: ")
    tasks.append(task)

# Display tasks
print("\n--- Tasks ---")
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task}")

# Remove a task
print()
remove_choice = input("Would you like to remove a task? (yes/no): ")

if remove_choice == "yes":
    task_to_remove = int(input("Enter the task number to remove: "))
    
    if task_to_remove > 0 and task_to_remove < len(tasks):
        removed = tasks.pop(task_to_remove - 1)
        print(f"Removed Task {task_to_remove}: {removed}")
    else:
        print("Bad task index provided")


# Display tasks
print("\n--- Tasks ---")
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")

if len(tasks) == 0:
    print("No tasks remaining.")
