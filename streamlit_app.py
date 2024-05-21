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

# Link to the respective pages using st.switch_page
if selected_item == "Thị trường":
    st.markdown(f"[📈 Thị trường](pages/Thị_trường.py)")
    st.experimental_rerun()  # Dừng chạy tại đây và chuyển sang trang mới
elif selected_item == "Cổ phiếu chọn lọc":
    st.markdown(f"[⭐ Cổ phiếu chọn lọc](pages/Co_phieu_chon_loc.py)")
    st.experimental_rerun()
elif selected_item == "Đầu tư Danh mục":
    st.markdown(f"[📊 Đầu tư Danh mục](pages/Dau_tu_Danh_muc.py)")
    st.experimental_rerun()
elif selected_item == "Flash Deal":
    st.markdown(f"[⚡ Flash Deal](pages/Flash_Deal.py)")
    st.experimental_rerun()
elif selected_item == "Hướng dẫn sử dụng":
    st.markdown(f"[📘 Hướng dẫn sử dụng](pages/Huong_dan_su_dung.py)")
    st.experimental_rerun()
elif selected_item == "Liên hệ":
    st.markdown(f"[📞 Liên hệ](pages/Lien_he.py)")
    st.experimental_rerun()

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
