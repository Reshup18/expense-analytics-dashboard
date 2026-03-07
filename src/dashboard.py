import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analysis import category_spending, daily_spending, monthly_spending

st.title("Expense Analytics Dashboard")

uploaded_file = st.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file is not None:

    try:
        data = pd.read_csv(uploaded_file)

        required_columns = {"date", "category", "amount"}

        if not required_columns.issubset(data.columns):
            st.error("CSV must contain: date, category, amount")

        else:

            data["date"] = pd.to_datetime(data["date"])

            # KPI Calculations
            total_spending = data["amount"].sum()
            avg_spending = data["amount"].mean()
            transactions = len(data)
            highest_day = data.groupby("date")["amount"].sum().idxmax()

            # KPI Display
            st.subheader("Key Financial Insights")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Total Spending", f"₹{total_spending:.2f}")
            col2.metric("Average Transaction", f"₹{avg_spending:.2f}")
            col3.metric("Total Transactions", transactions)
            col4.metric("Highest Spending Day", str(highest_day.date()))

            st.subheader("Raw Data")
            st.dataframe(data)

            categories = data["category"].unique()

            selected_category = st.selectbox("Select Category", categories)

            filtered_data = data[data["category"] == selected_category]

            st.subheader("Filtered Data")
            st.dataframe(filtered_data)

            # Category Spending
            st.subheader("Category Spending")

            cat_data = category_spending(data)

            fig, ax = plt.subplots()
            cat_data.plot(kind="bar", ax=ax)
            ax.set_ylabel("Amount")

            st.pyplot(fig)

               #Pie Chart for Spending Distribution
            st.subheader("Spending Distribution")
            fig_pie, ax_pie = plt.subplots()
            cat_data.plot(kind = "pie" , autopct = "%1.1f%%" , ax = ax_pie) 
            ax_pie.set_ylabel("")
            st.pyplot(fig_pie)  

            # Daily Spending
            st.subheader("Daily Spending")

            daily = daily_spending(filtered_data)

            fig2, ax2 = plt.subplots()
            daily.plot(ax=ax2)
            ax2.set_ylabel("Amount")

            st.pyplot(fig2)

            # Monthly Spending
            st.subheader("Monthly Spending")

            monthly = monthly_spending(data)

            fig3, ax3 = plt.subplots()
            monthly.plot(kind="bar", ax=ax3)
            ax3.set_ylabel("Amount")

            st.pyplot(fig3)

    except Exception as e:
        st.error(f"Error processing file: {e}")