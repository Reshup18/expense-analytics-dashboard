# Expense Analytics Dashboard

## Project Overview

The Expense Analytics Dashboard is an interactive data analytics application that helps users analyze their personal spending patterns. Users can upload a CSV file containing transaction data and explore insights such as category-wise spending, daily spending trends, and monthly summaries through an interactive web dashboard.

The application processes financial data using Python and Pandas and presents insights using dynamic visualizations built with Streamlit.

---
## Dashboard Preview

### Overview

![Dashboard Overview](images/dashboard_overview.png)

### Spending Distribution

![Spending Distribution](images/spending_distribution.png)

### Date Range Analysis

![Date Filter Analysis](images/date_filter_analysis.png)

## Features

* Upload expense data using CSV files
* Key financial KPI metrics (Total spending, average transaction, highest spending day)
* Category-wise spending analysis
* Spending distribution pie chart
* Daily spending trend visualization
* Monthly spending summary
* Date range filtering for custom analysis
* Category-based filtering
* Automated financial insights
* Interactive dashboard interface
* Live cloud deployment

---

## Tech Stack

* Python
* Pandas
* Matplotlib
* Streamlit
* Git & GitHub
* Streamlit Cloud (Deployment)

---

## Project Structure

```
expense-analytics-dashboard
│
├── src
│   ├── dashboard.py
│   └── analysis.py
│
├── data
│   └── sample_expense.csv
│
├── requirements.txt
└── README.md
```

---

## Sample CSV Format

The uploaded CSV file should contain the following columns:

```
date,category,amount
2025-01-01,Food,250
2025-01-02,Transport,120
2025-01-03,Shopping,800
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/Reshup18/expense-analytics-dashboard.git
```

2. Navigate to the project directory

```
cd expense-analytics-dashboard
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the dashboard

```
streamlit run src/dashboard.py
```

---

## Live Demo

Access the deployed dashboard here:

https://expense-analytics-dashboard-reshu.streamlit.app/

---

## Key Insights Generated

The dashboard automatically highlights important financial insights such as:

* Highest spending category
* Average daily spending
* Monthly spending trends

These insights help users better understand their financial behavior.

---

## Future Improvements

* Automatic expense category detection
* Integration with financial APIs
* Database storage instead of CSV files
* Machine learning based spending prediction
* User authentication system

---

## Author

Reshu Pathak

---
