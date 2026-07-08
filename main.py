from ui.menu import show_menu
from models.expense import Expense
from services.file_handler import save_expense, view_expenses


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        date = input("Enter Date (DD-MM-YYYY): ")
        category = input("Enter Category: ")
        amount = input("Enter Amount: ")
        description = input("Enter Description: ")

        expense = Expense(
            date,
            category,
            amount,
            description
        )

        save_expense(expense)

        print("Expense Saved Successfully!")

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")