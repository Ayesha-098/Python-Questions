import csv

while True:
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        with open("users.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print("Signup successful!")
    
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        try:
            with open("users.csv", "r") as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if row and row[0] == username and row[1] == password:
                        print("Login successful!")
                        found = True
                        break
                if not found:
                    print("Invalid username or password.")
        except FileNotFoundError:
            print("No users found. Please sign up first.")
    
    elif choice == "3":
        print("bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
