#List to store dictionaries
expenses = []
import time
date_format = None
def add_expense():
    global date_format
    #Get expense details from user
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
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
                max = 31
            elif month in [4, 6, 9, 11]:
                max = 30
            else:  
                max = 29 if leap(year) else 28
            if not (1 <= day <= max):             
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
    if date_format == "DMY":
        expenses.sort(
            key=lambda exp: (
                int(exp["date"].split("/")[2]),  
                int(exp["date"].split("/")[1]),  
                int(exp["date"].split("/")[0])   
            )
        )

    elif date_format == "MDY":
        expenses.sort(
            key=lambda exp: (
                int(exp["date"].split("/")[2]),  
                int(exp["date"].split("/")[0]),  
                int(exp["date"].split("/")[1])   
            )
        )

    elif date_format == "YMD":
        expenses.sort(
            key=lambda exp: (
                int(exp["date"].split("/")[0]),  
                int(exp["date"].split("/")[1]),  
                int(exp["date"].split("/")[2])   
            )
        )
    print("\nAll Expenses:")
    for exp in expenses:
        print("Category:", exp["category"],
              "| Amount: $", exp["amount"],
              "| Date:", exp["date"])
    print()

def total_expenses():
    #adding all expenses together
    expenses


def menu():
    print("Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")


while True:
    t = time.localtime()
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            pass 
