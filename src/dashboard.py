import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analysis import category_spending, daily_spending, monthly_spending

st.title("Expense Analytics Dashboard")

uploaded_file = st.file_uploader("Upload Expense CSV", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)
    data["date"] = pd.to_datetime(data["date"])

    st.subheader("Raw Data")
    st.write(data)

    categories = data["category"].unique()
    selected_category = st.selectbox("Select Category", categories)

    filtered_data = data[data["category"] == selected_category]

    st.subheader("Filtered Data")
    st.write(filtered_data)

    st.subheader("Category Spending")

    cat_data = category_spending(data)

    fig, ax = plt.subplots()
    cat_data.plot(kind="bar", ax=ax)

    st.pyplot(fig)

    st.subheader("Daily Spending")

    daily = daily_spending(filtered_data)

    fig2, ax2 = plt.subplots()
    daily.plot(ax=ax2)

    st.pyplot(fig2)

    st.subheader("Monthly Spending")

    monthly = monthly_spending(data)

    fig3, ax3 = plt.subplots()
    monthly.plot(kind="bar", ax=ax3)

    st.pyplot(fig3)