import streamlit as st
from streamlit_navigation_bar import st_navbar
import streamlit_antd_components as sac

# Set initial configuration for the Streamlit app
st.set_page_config(page_title="GoodStock Analysis")

# CSS to reduce the width of the sidebar
css = """
<style>
    .css-1cpxqw2 {
        width: 50px !important; /* Giảm chiều rộng của sidebar xuống còn 200px */
    }
</style>
"""

# Apply the CSS
st.markdown(css, unsafe_allow_html=True)

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
        "margin": "0 1rem",
        "padding": "0.4375rem 0.625rem",
        "display": "inline-block",
        "white-space": "nowrap",
        "font-size": "16px"
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
    st.write("This is the sidebar. Its width has been adjusted.")
    # Initialize the page configuration
    # Define a function to display the Ant Design styled menu in the sidebar
    def display_antd_menu():
        menu_items = sac.menu([
            sac.MenuItem('home', icon='house-fill', tag=[
                sac.Tag('Tag1', color='green'),
                sac.Tag('Tag2', color='red')
            ]),
            sac.MenuItem('products', icon='box-fill', children=[
                sac.MenuItem('apple', icon='apple'),
                sac.MenuItem('other', icon='git', description='other items', children=[
                    sac.MenuItem('google', icon='google', description='item description'),
                    sac.MenuItem('gitlab', icon='gitlab'),
                    sac.MenuItem('wechat', icon='wechat'),
                ]),
            ]),
            sac.MenuItem('disabled', disabled=True),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group', children=[
                sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
                sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
            ]),
        ], open_all=True)
        return menu_items
    
    # Place the menu in the sidebar
    with st.sidebar:
        st.write("Navigation Menu")
        display_antd_menu()
    
    # Main page content
    st.title("AntD Menu in Streamlit Sidebar")
    st.write("This is an example of integrating Ant Design components into a Streamlit app's sidebar.")

