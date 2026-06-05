print("-----To Do menu-----")
list = []
while True:
    menu = int(input(
        "Choose Menu (1 to 4)\n1.Add Task\n2.View Tasks\n3.Delete Tasks \n4.Exit \n= "))
    if menu == 1:
        add = (input("enter the task name ="))
        list.append(add)
        print(list)
    elif menu == 2:
        (print(list))
    elif menu == 3:
        print(list)
        delete = input("choose task to delete = ")
        list.remove(delete.lower())
        print(list)
    elif menu == 4:
        print("Exiting To Do App.....")
        break
