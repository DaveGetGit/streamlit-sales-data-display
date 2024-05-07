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


data = get_data()
data
