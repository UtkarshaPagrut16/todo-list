# Simple To-Do List

todo_list = []

while True:
    task = input("Enter a task (or 'exit' to quit): ")
    if task.lower() == 'exit':
        break
    todo_list.append(task)

print("\nYour To-Do List:")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")
