import streamlit as st
from streamlit_option_menu import option_menu



selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings','Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2
