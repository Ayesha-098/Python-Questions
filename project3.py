contacts = {}

while True:
    print("1. Enter contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Count contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in contacts:
            print(f"Contact name {name} already exists")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter Mobile Number: ")
            contacts[name] = {'age' : int(age), 'email': email, 'mobile': mobile}
            print(f"Contact name {name} has been added successfully")
    
    elif choice == "2":
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {age}, Mobile Number: {mobile}")
        else:
            print("Contact not found!")
        
    elif choice == "3":
        name = input("Enter the name you want to update: ")
        if name in contacts:
            age = input("Enter updated age: ")
            email = input("Enterupdated email: ")
            mobile = input("Enter Updated Mobile Number: ")
            print(f"Name: {name}, Age: {age}, Mobile Number: {mobile}")
        else:
            print("Contact Not found!")
        
    elif choice == "4":
        name = input("Enter the name you want to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print("Contact not found!")
    
    elif choice == "5":
        print(f'Total contacts stored:  {len(contacts)}')
    
    elif choice == "6":
        print("Goodbye")
        break

    else:
       print("Invalid Value")





