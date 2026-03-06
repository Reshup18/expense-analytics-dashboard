import matplotlib.pyplot as plt
import os


def category_bar_chart(category_data):
    
    os.makedirs("../outputs", exist_ok=True)

    category_data.plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.savefig("../outputs/category_spending.png")

    plt.show()


def monthly_line_chart(monthly_data):

    os.makedirs("../outputs", exist_ok=True)

    monthly_data.plot(kind="line", marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount")

    plt.savefig("../outputs/monthly_spending.png")

    plt.show()