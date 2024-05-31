import streamlit as st
import streamlit_antd_components as sac

# Initialize the page configuration
st.set_page_config(page_title="AntD Menu Sidebar", initial_sidebar_state="expanded")

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
