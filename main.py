from src.ui.menu import show_menu
from src.models.expense import Expense
from src.services.analytics import get_total_expense
from src.services.file_handler import (
    save_expense,
    view_expenses,
    delete_expense,
    update_expense,
    get_expense_by_id
)

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

        view_expenses()

        expense_id = int(input("\nEnter Expense ID to delete: "))

        if delete_expense(expense_id):
            print("Expense Deleted Successfully!")

        else:
            print("Invalid Expense ID")


    elif choice == "4":

        view_expenses()

        try:

            expense_id = int(input("\nEnter Expense ID to update: "))

            expense = get_expense_by_id(expense_id)

            if expense is None:
                print("\nInvalid Expense ID")
                continue

            print("\nPress Enter to keep current value.\n")

            new_date = input(f"Current Date ({expense[0]}): ")
            if new_date == "":
                new_date = expense[0]

            new_category = input(f"Current Category ({expense[1]}): ")
            if new_category == "":
                new_category = expense[1]

            new_amount = input(f"Current Amount ({expense[2]}): ")
            if new_amount == "":
                new_amount = expense[2]

            new_description = input(f"Current Description ({expense[3]}): ")
            if new_description == "":
                new_description = expense[3]

            updated_expense = Expense(
                new_date,
                new_category,
                new_amount,
                new_description
            )

            if update_expense(expense_id, updated_expense):
                print("\nExpense Updated Successfully!")

            else:
                print("\nFailed to Update Expense.")

        except ValueError:
            print("\nPlease enter a valid number!")

    elif choice == "5":

        total = get_total_expense()

        print(f"\nTotal Expense : ₹{total}")

    elif choice == "6":

        print("\nThank You!")
        break
    else:

        print("Invalid Choice")