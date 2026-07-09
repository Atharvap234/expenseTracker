import csv

FILE_PATH = "data/expenses.csv"


def save_expense(expense):
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())


def get_all_expenses():
    with open(FILE_PATH, mode="r") as file:
        reader = csv.reader(file)

        header = next(reader)
        rows = list(reader)

    return header, rows


def view_expenses():

    header, rows = get_all_expenses()

    print("\n" + "=" * 80)
    print(f"{'ID':<5}{'Date':<15}{'Category':<15}{'Amount':<12}{'Description'}")
    print("=" * 80)

    for index, row in enumerate(rows, start=1):
        print(f"{index:<5}{row[0]:<15}{row[1]:<15}{row[2]:<12}{row[3]}")

    print("=" * 80)


def get_expense_by_id(expense_id):

    header, rows = get_all_expenses()

    if expense_id < 1 or expense_id > len(rows):
        return None

    return rows[expense_id - 1]


def delete_expense(expense_id):

    header, rows = get_all_expenses()

    if expense_id < 1 or expense_id > len(rows):
        return False

    rows.pop(expense_id - 1)

    with open(FILE_PATH, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    return True


def update_expense(expense_id, updated_expense):

    header, rows = get_all_expenses()

    if expense_id < 1 or expense_id > len(rows):
        return False

    rows[expense_id - 1] = updated_expense.to_list()

    with open(FILE_PATH, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    return True