import csv

FILE_PATH = "data/expenses.csv"


def save_expense(expense):
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def view_expenses():
    with open(FILE_PATH, mode="r") as file:
        reader = csv.reader(file)

        print("\n{:<15} {:<15} {:<10} {:<25}".format(
            "Date", "Category", "Amount", "Description"))
        print("-" * 70)

        next(reader)  # Skip the header row

        for row in reader:
            print("{:<15} {:<15} {:<10} {:<25}".format(
                row[0], row[1], row[2], row[3]))