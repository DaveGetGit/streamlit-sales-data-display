import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import string
import time


@st.cache_data
def get_data():
    """Generate random sales data for widget A through Z"""
    product_names = ["widget " + letter for letter in string.ascii_uppercase]
    average_daily_sales = np.random.normal(1000, 300, len(product_names))
    products = dict(zip(product_names, average_daily_sales))
    data = pd.DataFrame({})
    sales_dates = np.arange(
        date(2023, 1, 1), date(2024, 1, 1), timedelta(days=1))
    for product, sales in products.items():
        data[product] = np.random.normal(sales, 300, len(sales_dates)).round(2)
    data.index = sales_dates
    data.index = data.index.date
    return data


@st.experimental_fragment
def show_daily_sales(data):
    time.sleep(1)
    selected_date = st.date_input("Pick a date", value=date(2023, 1, 1), min_value=date(
        2023, 1, 1), max_value=date(2023, 12, 31), key="selected_date")
    if "previous_date" not in st.session_state:
        st.session_state.previous_date = selected_date
    previous_date = st.session_state.previous_date
    st.session_state.previous_date = selected_date
    is_new_month = selected_date.replace(
        day=1) != previous_date.replace(day=1)
    if is_new_month:
        st.rerun()
    st.header(f"Best sellers, {selected_date:%B %d,%Y}")
    top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
    cols = st.columns([5, 10])
    cols[0].dataframe(top_ten)
    cols[1].bar_chart(top_ten)
    st.header(f"Worst sellers, {selected_date:%B %d,%Y}")
    bottom_ten = data.loc[selected_date].sort_values()[0:10]
    cols = st.columns([5, 10])
    cols[0].dataframe(bottom_ten)
    cols[1].bar_chart(bottom_ten)


data = get_data()
show_daily_sales(data)
