import datetime
import json

with open("expense.json" , "r") as file:
    data = json.load(file)

daily_expense = data

for expense in daily_expense:
    expense["date"] = datetime.datetime.strptime(expense["date"] , "%d-%m-%Y").date()

def save_expenses() :
    expense_for_saving = []
    
    for expense in daily_expense:
        saving_expense = expense.copy()
        saving_expense["date"] = saving_expense["date"].strftime("%d-%m-%Y")
        expense_for_saving.append(saving_expense)
    
    with open("expense.json", "w") as file:
        json.dump(expense_for_saving, file, indent=4)

def add_expense(amount, category, date):
    daily_expense.append ({
        "amount" : amount, 
        "category" : category, 
        "date" : datetime.datetime.strptime(date, "%d-%m-%Y").date()
})
    save_expenses()

def take_expense_input ():
    
    keep_adding = True

    while keep_adding :
        valid_amount = False
        while not valid_amount:
            try :
                amount = float(input("Enter amount: "))
                valid_amount = True
            except :
                print("Enter amount in numbers")
        valid_category = False
        while not valid_category:
            category = input("Enter category: ")
            if category == "" or category.isdigit():
                print("Enter a valid category")
            else :
                valid_category = True
        valid_date = False
        while not valid_date :
            try:
                date = input("Enter date: ")
                datetime.datetime.strptime(date, "%d-%m-%Y")
                valid_date = True
            except :
                print("Enter date in DD-MM-YYYY format")
        add_expense(amount, category, date)
        valid_answer = False
        while not valid_answer :
            answer = input("Do you want to add another expense ? (yes/no): ").lower()
            if answer !="yes" and answer !="no" :
                print("Please enter either yes or no")
            else :
                valid_answer = True
    
        if answer == "no":
            keep_adding = False

def calculate_total():
    total = 0
    for expense in daily_expense:
        total += expense["amount"]  
    return total

def calculate_category_total(category):
    existing_category = False 
    category_total = 0 
    for expense in daily_expense:
        if expense["category"] == category:
            existing_category = True
            category_total += expense["amount"]
    return existing_category , category_total

def view_expenses():        
    if not daily_expense :
        print("There is no expense data to show")
    else :
        for index , expense in enumerate(daily_expense):
            print(index , "Amount:" , expense["amount"], "| Category:" , expense["category"] , "| Date:" , expense["date"])
        
def search_by_category():
    category = input("Enter the category to search: ")
    existing_category = False

    for expense in daily_expense:
        if expense["category"] == category:
            existing_category = True
            print("Amount:", expense["amount"], "| Category:", expense["category"], "| Date:", expense["date"])
            
    if existing_category == False:
        print("The category", category, "does not exist in the daily expense list.")

def del_expense(index):
    try :
        del daily_expense[index]
        print(daily_expense)
        save_expenses()
    except IndexError :
        print("This index does not exist")

def update_expense():
    print("==== UPDATE EXPENSE ====")
    view_expenses()
    valid_answer = False
    while not valid_answer :
        answer = input("Do you want to update any expense ? (yes/no): ").lower()
        if answer !="yes" and answer !="no" :
            print("Please enter either yes or no")
        else :
            valid_answer = True
    if answer == "no" :
        return
    valid_index = False
    while not valid_index :
        try :
            index = int(input("Choose the index you want to update : ")) 
            if index >= 0 and index < len(daily_expense) :
                valid_index = True
            else :
                print("The index does not exist")
        except :
            print("Enter a valid index")
    valid_choice = False 
    while not valid_choice:
        try :
            choice = int(input("Which part of expense you want to update ? 1.Amount , 2.Category , 3.Date :"))
            if choice >= 1 and choice <= 3:
                valid_choice = True
            else :
                print("Enter a valid choice")
        except :
            print("Enter a valid choice")
    try :
        if choice == 1:
            valid_amount = False
            while not valid_amount :
                try :
                    amount = float(input("Enter the updated amount: "))
                    valid_amount = True
                except :
                     print("Enter amount in numbers")
            daily_expense[index]["amount"] = amount 
            print("Expense updated successfully!")
            save_expenses()
        elif choice == 2:
            valid_category = False
            while not valid_category :
                category = input("Enter the updated category: ")
                
                if category == "" or category.isdigit():
                    print("Enter a valid category name")
                else :
                    valid_category = True
                    
            daily_expense[index]["category"] = category
            print("Expense updated successfully!")
            save_expenses()
        elif choice == 3:
            valid_date = False
            while not valid_date :
                try :
                    date = input("Enter the updated date: ")
                    daily_expense[index]["date"] = datetime.datetime.strptime(date, "%d-%m-%Y").date()
                    valid_date = True
                except :
                    print("Enter date in DD-MM-YYYY format")
            save_expenses()
    except Exception as e :
        print(e)