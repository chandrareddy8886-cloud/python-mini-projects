while True:
    print("\nContact manager")
    print("1. Add contact ")
    print("2. View contact ")
    print("3. Exit ")
    choice = input("Enter choice : ")
    if choice == "3":
        print("\nGood bye for now ! ")
        break
    if choice == "1":
        name = input("Enter contact name : ")
        phone = input("Enter phone : ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name} - {phone}\n")
            print("Contact saved successfully")
    if choice == "2":
        with open("contacts.txt", "r") as file:
            contacts = file.read()
            print("\ncontacts : ")
            print(contacts)
