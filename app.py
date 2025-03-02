import streamlit as st
import pandas as pd

# Title
st.title("Expense Tracker")

# Sidebar for User Input
st.sidebar.header("Add New Expense")
title = st.sidebar.text_input("Expense Title")
amount = st.sidebar.number_input("Amount", min_value=0.0, format="%.2f")
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Others"])
add_expense = st.sidebar.button("Add Expense")

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["Title", "Amount", "Category"])

def add_expense_to_data():
    new_expense = pd.DataFrame([[title, amount, category]], columns=["Title", "Amount", "Category"])
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

if add_expense and title:
    add_expense_to_data()
    st.sidebar.success("Expense Added!")

st.dataframe(st.session_state.expenses)

if not st.session_state.expenses.empty:
    expense_summary = st.session_state.expenses.groupby("Category")["Amount"].sum()
    st.bar_chart(expense_summary)
else:
    st.write("No expenses added yet!")

