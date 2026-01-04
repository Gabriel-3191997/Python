def tasks():

    # inserting tasks

    tasks_1 = input("Task 1: ")
    tasks_2 = input("Task 2: ")
    tasks_3 = input("Task 3: ")

    my_daily_tasks = []
    my_daily_tasks.append(tasks_1)
    my_daily_tasks.append(tasks_2)
    my_daily_tasks.append(tasks_3)

    
    for i, task in enumerate(my_daily_tasks, start=1):

        print("\nMy Daily Tasks:\n")

        print(f"{i}. {task}")

    # deleting tasks

    def delete_tasks():

        task_to_delete = int(input("\nEnter the task number to delete: "))

        if 1 <= task_to_delete <= len(my_daily_tasks):

            deleted_task = my_daily_tasks.pop(task_to_delete - 1)

            print(f"\nDeleted task: {deleted_task}\n")

            print("\nDaily Tasks:\n")
            
            for i, task in enumerate(my_daily_tasks, start=1):


                print(f"{i}. {task}")

        else:

            print("\nInvalid task number.\n")

    
    delete_tasks()

tasks()
