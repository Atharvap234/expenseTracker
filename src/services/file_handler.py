import csv

FILE_PATH = "data/expenses.csv"


def save_expense(expense):
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def view_expenses():
    with open(FILE_PATH, mode="r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        print("\n" + "=" * 80)
        print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
        print("=" * 80)

        for index, row in enumerate(reader, start=1):
            print(f"{index:<5}{row[0]:<15}{row[1]:<15}{row[2]:<12}{row[3]}")

        print("=" * 80)