import streamlit as st

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

# Main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")

# Link to the respective pages using st.switch_page
if selected_item == "Thị trường":
    st.markdown("[📈 Thị trường](pages/Thị_trường.py)")
    if st.button("Chuyển đến Thị trường"):
        st.switch_page("pages/Thị_trường.py")
elif selected_item == "Cổ phiếu chọn lọc":
    st.markdown("[⭐ Cổ phiếu chọn lọc](pages/Co_phieu_chon_loc.py)")
    if st.button("Chuyển đến Cổ phiếu chọn lọc"):
        st.switch_page("pages/Co_phieu_chon_loc.py")
elif selected_item == "Đầu tư Danh mục":
    st.markdown("[📊 Đầu tư Danh mục](pages/Dau_tu_Danh_muc.py)")
    if st.button("Chuyển đến Đầu tư Danh mục"):
        st.switch_page("pages/Dau_tu_Danh_muc.py")
elif selected_item == "Flash Deal":
    st.markdown("[⚡ Flash Deal](pages/Flash_Deal.py)")
    if st.button("Chuyển đến Flash Deal"):
        st.switch_page("pages/Flash_Deal.py")
elif selected_item == "Hướng dẫn sử dụng":
    st.markdown("[📘 Hướng dẫn sử dụng](pages/Huong_dan_su_dung.py)")
    if st.button("Chuyển đến Hướng dẫn sử dụng"):
        st.switch_page("pages/Huong_dan_su_dung.py")
elif selected_item == "Liên hệ":
    st.markdown("[📞 Liên hệ](pages/Lien_he.py)")
    if st.button("Chuyển đến Liên hệ"):
        st.switch_page("pages/Lien_he.py")
