import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar title
st.sidebar.title("VNWEALTH")

# Define menu items with icons
menu_items = [
    {"label": "Thị trường", "icon": "📈", "file": "pages/Thị_trường.py"},
    {"label": "Cổ phiếu chọn lọc", "icon": "⭐", "file": "pages/Co_phieu_chon_loc.py"},
    {"label": "Đầu tư Danh mục", "icon": "📊", "file": "pages/Dau_tu_Danh_muc.py"},
    {"label": "Flash Deal", "icon": "⚡", "file": "pages/Flash_Deal.py"},
    {"label": "Hướng dẫn sử dụng", "icon": "📘", "file": "pages/Huong_dan_su_dung.py"},
    {"label": "Liên hệ", "icon": "📞", "file": "pages/Lien_he.py"}
]

# Sidebar menu with icons
selected_item = option_menu(
    menu_title="",  # required
    options=[item["label"] for item in menu_items],  # required
    icons=[item["icon"] for item in menu_items],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
    styles={
        "container": {"padding": "5px", "background-color": "#f8f9fa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "2px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# Link to the respective pages using st.page_link
for item in menu_items:
    if selected_item == item["label"]:
        st.page_link(page=item["file"], label=item["label"], icon=item["icon"])

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
