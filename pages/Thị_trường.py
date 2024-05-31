import streamlit as st
from streamlit_navigation_bar import st_navbar

# Set initial configuration for the Streamlit app
st.set_page_config(page_title="GoodStock Analysis", initial_sidebar_state="collapsed")

# Define the pages and custom styles for the navigation bar
pages = ["Home", "Documentation", "Examples", "Community", "About"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "width": "100%",
    },
    "div": {
        "width": "100%",
        "margin": "auto"
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.025 rem",  # Tăng khoảng cách ngang giữa các mục
        "padding": "0.4375rem 0.625rem",
        "display": "inline-block",
        "white-space": "nowrap",
        "font-size": "14px"
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)"
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)"
    },
}

# Implement navigation bar and get the currently selected page
selected_page = st_navbar(pages, styles=styles)

# Define the content for each page and display it
def home():
    st.title("Home")
    st.write("Welcome to the home page!")

def documentation():
    st.title("Documentation")
    st.write("Here you can find all the documentation.")

def examples():
    st.title("Examples")
    st.write("Check out these cool examples.")

def community():
    st.title("Community")
    st.write("Join our vibrant community!")

def about():
    st.title("About")
    st.write("Learn more about our project.")

if selected_page == "Home":
    home()
elif selected_page == "Documentation":
    documentation()
elif selected_page == "Examples":
    examples()
elif selected_page == "Community":
    community()
elif selected_page == "About":
    about()

# Sidebar content
with st.sidebar:
    st.write("Sidebar")
