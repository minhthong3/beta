import streamlit as st
import sys
import codecs

# Sidebar title
st.sidebar.title("VNWEALTH")

# Sidebar menu with custom icons
menu_items = {
    "Thị trường": "📈",
    "Cổ phiếu chọn lọc": "⭐",
    "Đầu tư Danh mục": "📊",
    "Flash Deal": "⚡",
    "Hướng dẫn sử dụng": "📘",
    "Liên hệ": "📞"
}

selected_item = st.sidebar.radio(
    "",
    list(menu_items.keys()),
    format_func=lambda x: f"{menu_items[x]} {x}"
)

# Link to the respective pages using st.page_link
if selected_item == "Thị trường":
    st.page_link("pages/Thị_trường.py", label="Thị trường", "📈")
elif selected_item == "Cổ phiếu chọn lọc":
    st.page_link("pages/Co_phieu_chon_loc.py", label="Cổ phiếu chọn lọc", icon="⭐")
elif selected_item == "Đầu tư Danh mục":
    st.page_link("pages/Dau_tu_Danh_muc.py", label="Đầu tư Danh mục", icon="📊")
elif selected_item == "Flash Deal":
    st.page_link("pages/Flash_Deal.py", label="Flash Deal", icon="⚡")
elif selected_item == "Hướng dẫn sử dụng":
    st.page_link("pages/Huong_dan_su_dung.py", label="Hướng dẫn sử dụng", icon="📘")
elif selected_item == "Liên hệ":
    st.page_link("pages/Lien_he.py", label="Liên hệ", icon="📞")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
