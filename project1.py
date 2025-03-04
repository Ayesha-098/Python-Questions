import csv

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Show Total Expenses")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")

            csv.writer(open("expenses.csv", "a", newline="")).writerow([category, amount, date])

            print("Expense added successfully!")
        except ValueError:
            print("Invalid input! Please enter a numeric value for amount.")

    elif choice == "2":
        try:
            reader = csv.reader(open("expenses.csv", "r"))
            next(reader)

            total = 0
            for row in reader:
                total += float(row[1])
            
            print(f"Total Expenses: {total}")
        except Exception as e:
            print("Error reading file:", e)

    elif choice == "3":
        print("Exiting the Expense Tracker.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
