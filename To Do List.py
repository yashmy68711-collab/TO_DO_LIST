tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

     if task.strip() == "":
            print("Task cannot be empty")
        else:
            tasks.append(task)
            print("Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            print("\nTasks:")
            for t in tasks:
                print("-", t)
                
    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Wrong choice")
