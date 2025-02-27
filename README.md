# Streamlit Sales Data App

This Streamlit app displays sales data. It uses the concept of fragments and `st.rerun` to efficiently update the displayed data based on user input.

## Key Features

- **Fragments**: Streamlit lets you turn functions into fragments, which can rerun independently from the full script. When a user interacts with a widget inside a fragment, only the fragment reruns.
- **Full-script rerun**: Sometimes, you may want to trigger a full-script rerun from inside a fragment. To do this, call `st.rerun` inside the fragment.

## Prerequisites

- Streamlit version 1.33.0 or later.
- A clean working directory called `your-repository`.
- A basic understanding of fragments and `st.rerun`.

## App Overview

In this app, you'll build an interface to display sales data. The app has two sets of elements that depend on a date selection:

1. One set of elements displays information for the selected day.
2. The other set of elements displays information for the associated month.

If the user changes days within a month, Streamlit only needs to update the first set of elements. If the user selects a day in a different month, Streamlit needs to update all the elements.

You'll collect the day-specific elements into a fragment to avoid rerunning the full app when a user changes days within the same month.

Here's a brief excerpt from the provided code:

```python
@st.experimental_fragment
def show_daily_sales(data):
    selected_date = st.date_input("Pick a date", value=date(2023, 1, 1), min_value=date(
        2023, 1, 1), max_value=date(2023, 12, 31), key="selected_date")
    ...
    st.header(f"Best sellers, {selected_date:%B %d,%Y}")
    top_ten = data.loc[selected_date].sort_values(ascending=False)[0:10]
    ...
    st.header(f"Worst sellers, {selected_date:%B %d,%Y}")
    bottom_ten = data.loc[selected_date].sort_values()[0:10]
    ...
```
