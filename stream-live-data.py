"""
  Imports 
"""
from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import numpy as np


def get_recent_data(last_timestamp):
    """
    Generate and return data from last timestamp to now, at most 60 seconds.

    Parameters:
    last_timestamp (datetime): The last timestamp from which to generate data.

    Returns:
    data (DataFrame): A DataFrame with random data from the last timestamp to now.
    """
    now = datetime.now()
    if now - last_timestamp > timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data


# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = get_recent_data(
        datetime.now() - timedelta(seconds=60))

if "stream" not in st.session_state:
    st.session_state.stream = False


def toggle_streaming():
    """
    Toggle the streaming state in the session state.
    """
    st.session_state.stream = not st.session_state.stream


# Set up Streamlit interface
st.title("Data feed")
st.sidebar.slider("Check for updates every: (seconds)",
                  0.5, 5.0, value=1.0, key="RUN_EVERY")
st.sidebar.button("Start streaming",
                  disabled=st.session_state.stream, on_click=toggle_streaming)
st.sidebar.button("Stop streaming",
                  disabled=not st.session_state.stream, on_click=toggle_streaming)

# Determine update frequency
RUN_EVERY = None


@st.experimental_fragment(RUN_EVERY=RUN_EVERY)
def show_latest_data():
    """
    Show the latest data in a line chart, updating according to the RUN_EVERY parameter.
    """
    last_timestamp = st.session_state.data.index[-1]
    print(f"Last timestamp: {last_timestamp}")
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)])
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)


# Run the data display function
show_latest_data()
