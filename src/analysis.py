import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    data["date"] = pd.to_datetime(data["date"])
    return data


def category_spending(data):
    return data.groupby("category")["amount"].sum()


def daily_spending(data):
    return data.groupby("date")["amount"].sum()


def monthly_spending(data):
    data["month"] = data["date"].dt.to_period("M")
    return data.groupby("month")["amount"].sum()


def largest_expense(data):
    return data.loc[data["amount"].idxmax()]