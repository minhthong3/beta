import streamlit as st

# Sidebar title
st.sidebar.title("VNWEALTH")

# Sidebar menu with custom icons
menu_items = {
    "Thông tin thị trường": "📈",
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

# Link to the respective pages
if selected_item == "Thông tin thị trường":
    st.experimental_rerun("Thong_tin_thi_truong")
elif selected_item == "Cổ phiếu chọn lọc":
    st.experimental_rerun("Co_phieu_chon_loc")
elif selected_item == "Đầu tư Danh mục":
    st.experimental_rerun("Dau_tu_Danh_muc")
elif selected_item == "Flash Deal":
    st.experimental_rerun("Flash_Deal")
elif selected_item == "Hướng dẫn sử dụng":
    st.experimental_rerun("Huong_dan_su_dung")
elif selected_item == "Liên hệ":
    st.experimental_rerun("Lien_he")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
