#List to store expense dictionaries
expenses = []


def add_expense():
    #Get expense details from user
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    #Store expense in a dictionary
    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    #Add dictionary to list
    expenses.append(expense)

    print("Expense added successfully!\n")


def view_expenses():
    #Display all expenses
    if len(expenses) == 0:
        print("No expenses recorded.\n")
        return

    print("\nAll Expenses:")
    for exp in expenses:
        print("Category:", exp["category"],
              "| Amount: $", exp["amount"],
              "| Date:", exp["date"])
    print()


def menu():
    print("Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses by Category")
    print("4. Calculate Total Expenses")
    print("5. Delete Expense")
    print("6. Exit")


while True:
    menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        pass 