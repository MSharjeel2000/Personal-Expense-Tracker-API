from main import take_expense_input , view_expenses , calculate_total , calculate_category_total , search_by_category , del_expense , update_expense

while True :
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category Total")
    print("5. Search by Category")
    print("6. Delete Expense")
    print("7. Update Expense")
    print("8. Exit")

    choice = input("Enter your choice :")

    if choice == "1":
        take_expense_input()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print(calculate_total())
    elif choice == "4":
            category = input("Enter category: ")
            existing_category, category_total = calculate_category_total(category)
            if existing_category:
                print("Total spending for", category, ":", category_total)
            else:
                print("No expenses found for", category)
    elif choice == "5":
        search_by_category()
    elif choice == "6":
        view_expenses()
        valid_index = False
        while not valid_index :
            try :
                index = int(input("Enter the index you want to delete: "))
                valid_index = True
            except :
                print("Enter valid index")
        del_expense(index)
    elif choice == "7":
        update_expense()
    elif choice == "8":
        print("....")
        break
    else:
        print("Invalid Choice")


# if __name__ == "__main__":
#     print("practice.py is being run directly")
    
# import json
# file = open("expense.json" , "r")
# result1 = file.read()
# print("The result 1 is: " , result1)
# file.seek(0)
# result2 = file.read()
# print("The result 2 is: " , result2)
# file.close()
# with open("expense.json" , "r") as file :
#     data = json.load(file)