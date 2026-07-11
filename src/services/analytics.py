import pandas as pd

FILE_PATH = "data/expenses.csv"


def get_total_expense():
    df = pd.read_csv(FILE_PATH)

    total = df["Amount"].sum()

    return total