import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    st.sidebar.page_link("pages/llm_model.py", label="LLM Model")
    st.sidebar.page_link("pages/sales_dashboard.py", label="Sales Dashboard")
    st.sidebar.page_link("pages/stream-live-data.py", label="Stream Live Data")
    st.sidebar.page_link("pages/cats.py", label="Cat Herding")
    st.sidebar.page_link("pages/shakespeare_query.py",
                         label="[BigQuery]Shakespeare Query")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
