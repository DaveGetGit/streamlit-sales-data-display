"""
  Imports 
"""
import time
import streamlit as st

st.title("Cats!")
with st.spinner("Wait for it..."):
    time.sleep(5)

row1 = st.columns(3)
row2 = st.columns(3)

# Create a grid of containers
grid = [col.container(height=200) for col in row1 + row2]
# Create a safe grid of empty containers
safe_grid = [card.empty() for card in grid]


def black_cats():
    """
    Display black cat emojis.
    """
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")


def orange_cats():
    """
    Display orange cat emojis.
    """
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")


@st.experimental_fragment
def herd_black_cats(card_a, card_b, card_c):
    """
    Display a button to herd black cats and display black cat emojis in the given containers.
    """
    st.button("Herd the black cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()


@st.experimental_fragment
def herd_orange_cats(card_a, card_b, card_c):
    """
    Display a button to herd orange cats and display orange cat emojis in the given containers.
    """
    st.button("Herd the orange cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()


# Add buttons to the sidebar to herd the cats
with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
    herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
    st.button("Herd all the cats")
