import streamlit as st
import streamlit_antd_components as sac

def main():
    # This function will manage navigation and display content based on the current 'page'
    params = st.experimental_get_query_params()  # get current query params
    current_page = params.get('page', ['home'])[0]  # get 'page' parameter, default to 'home'

    # Define menu items and actions
    menu = sac.menu([
        sac.MenuItem('Home', key='home', icon='house-fill'),
        sac.MenuItem('Products', key='products', icon='box-fill', children=[
            sac.MenuItem('Apple', key='apple', icon='apple'),
            sac.MenuItem('Other', key='other', icon='git', children=[
                sac.MenuItem('Google', key='google', icon='google'),
                sac.MenuItem('Gitlab', key='gitlab', icon='gitlab'),
                sac.MenuItem('WeChat', key='wechat', icon='wechat'),
            ]),
        ]),
        sac.MenuItem('Disabled', key='disabled', disabled=True),
        sac.MenuItem(type='divider'),
        sac.MenuItem('Links', key='links', type='group', children=[
            sac.MenuItem('AntD Menu', key='antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('Bootstrap Icon', key='bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
        ]),
    ], defaultSelectedKeys=[current_page], mode="horizontal", onSelect=handle_select)

    st.sidebar.write(menu)
    display_page_content(current_page)

def handle_select(selected_key):
    # This function updates the query params based on selection to simulate page navigation
    st.experimental_set_query_params(page=selected_key['key'])  # set 'page' param to selected menu key
    st.experimental_rerun()  # rerun the app to reflect changes

def display_page_content(page):
    # Depending on the page parameter, display different content
    if page == 'home':
        st.header("Home Page")
        st.write("Welcome to the Home page.")
    elif page == 'apple':
        st.header("Apple Products")
        st.write("Details about Apple products.")
    elif page == 'gitlab':
        st.header("Gitlab")
        st.write("Gitlab integration and projects.")
    elif page == 'other':
        st.header("Other Products")
        st.write("Listing other miscellaneous products.")
    # Add more elif blocks for other pages like 'google', 'wechat', etc.

if __name__ == "__main__":
    main()
