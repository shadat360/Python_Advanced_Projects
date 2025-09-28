def task():
    tasks = []
    print("----Welcome To The Daily Task Management App----")
    
    while True:
        try:
           total_task =int(input("Enter how many task you want to add = "))
           break
        except:
           print("Invalid input! Please enter a valid number.")

    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are: ")
    i = 1
    for t in tasks:
        print(f"{i}. {t}")
        i += 1

    while True:
        try:
            operation = int(input("Enter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\n = "))
        
        except ValueError:
            print("Invalid input! Please enter a number between 1 to 5.")
            continue

        if operation == 1:
           add = input("Enter task you want to add =")
           tasks.append(add)
           print(f"Task {add} has been successfully added. . .")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
            
            else:
                print("Task not found!")    

        elif operation == 3:
            del_val = input("Which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted. . .")

            else:
                print("Task not found!") 


        elif operation == 4:
            print(f"Total tasks are: ")
            i = 1
            for t in tasks:
                print(f"{i}. {t}")
                i += 1


        elif operation ==5:
            print("Closing the program. . . ")         
            break

        else:
            print("Invalid Input!") 
                     
task()