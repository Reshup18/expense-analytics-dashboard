from analysis import load_data, category_spending, daily_spending, monthly_spending, largest_expense
from visualization import category_bar_chart, monthly_line_chart


data = load_data("../expenses.csv")

print("Largest Expense:")
print(largest_expense(data))

print("\nCategory Spending:")
category_data = category_spending(data)
print(category_data)

print("\nDaily Spending:")
print(daily_spending(data))

print("\nMonthly Spending:")
monthly_data = monthly_spending(data)
print(monthly_data)

category_bar_chart(category_data)
monthly_line_chart(monthly_data)