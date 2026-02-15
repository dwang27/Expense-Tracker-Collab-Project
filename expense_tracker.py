#List to store dictionaries
expenses = []
import time
date_format = None
def add_expense():
    global date_format
    #Get expense details from user
    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    while True: 
        if date_format is None:     
            date_format = input("which format would you like? (dmy, mdy, ymd): ").upper()
            if date_format in ("DMY", "MDY", "YMD"):
               break
            print("invalid format, try again")
            date_format = None
            continue
        else:
            break
 #asks and checks for if month is valid
    while True:
        try:
            month = int(input("enter month: "))
            if 1<=month<=12:
                break
            print("Invalid Month. Try again")
        except ValueError:
            print ("Sorry, months can't have letters. Try again")
    #asks and checks for if year is valid
    while True:
        try:
            year = int(input("enter year: "))
            break
        except ValueError:
            print("Sorry, years can't have letters. Try again")
    while True:
        try:
            day = int(input("enter day: "))
            #check for leap years
            def leap(year):
             return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            if month in [1, 3, 5, 7, 8, 10, 12]:
                max_day = 31
            elif month in [4, 6, 9, 11]:
                max_day = 30
            else:  
                max_day = 29 if leap(year) else 28
            if not (1 <= day <= max_day):             
                print ("thats not a valid date, sorry. Try again")
                continue
            break
        except ValueError:
            print("Sorry, days can't have letters. Try again")
    #using that format to convert the string
    if date_format == ("DMY"):
        date = (f"{day}/{month}/{year}")
    elif date_format == ("MDY"):
        date = (f"{month}/{day}/{year}")
    elif date_format == ("YMD"):
        date = (f"{year}/{month}/{day}")
    #Add dictionary to list
    expenses.append({
        "category": category,
        "amount": amount,
        "date": date
    })
    print("Expense added successfully!\n")


#function to view expenses
def view_expenses():   
    #first sorts the expenses     
    if date_format == "DMY":
        expenses.sort(key=lambda exp: (
            int(exp["date"].split("/")[2]),  
            int(exp["date"].split("/")[1]),  
            int(exp["date"].split("/")[0])   
        ))
    elif date_format == "MDY":
        expenses.sort(key=lambda exp: (
            int(exp["date"].split("/")[2]),  
            int(exp["date"].split("/")[0]),  
            int(exp["date"].split("/")[1])   
        ))
    elif date_format == "YMD":
        expenses.sort(key=lambda exp: (
            int(exp["date"].split("/")[0]),  
            int(exp["date"].split("/")[1]),  
            int(exp["date"].split("/")[2])    
        ))
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

#function to calculate total expenses
def total_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.\n")
        return
    category_totals = {}
    # Sum amounts per category
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
    grand_total = 0
    # Print category totals
    for cat, total in category_totals.items():
        print(f"{cat} total: ${total:.2f}")
        grand_total += total
    print(f"\nTotal expenses: ${grand_total:.2f}\n")

#function for menu
def menu():
    print("Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

#function to assign number to expenses
def view_expenses_numbered():
    if len(expenses) == 0:
        print("No expenses recorded.\n")
        return
    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. Category: {exp['category']} | Amount: ${exp['amount']} | Date: {exp['date']}")
    print()
#function to delete expense
def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.\n")
        return
    view_expenses_numbered()  # Show numbered list for deletion
    while True:
        try:
            index = int(input("Enter the number of the expense to delete: ")) - 1
            if 0 <= index < len(expenses):
                removed = expenses.pop(index)
                print(f"Deleted expense: {removed['category']} ${removed['amount']} on {removed['date']}\n")
                break
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

#user interface
while True:
    t = time.localtime()
    menu()
    choice = input("Choose an option (1-5): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n") 
