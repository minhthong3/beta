import streamlit as st
import base64



# Display page links in the main content
if selected_item == "Thông tin thị trường":
    st.page_link("pages/Thong_tin_thi_truong", label="Thông tin thị trường", icon="📈")
elif selected_item == "Cổ phiếu chọn lọc":
    st.page_link("pages/Co_phieu_chon_loc", label="Cổ phiếu chọn lọc", icon="⭐")
elif selected_item == "Đầu tư Danh mục":
    st.page_link("pages/Dau_tu_Danh_muc", label="Đầu tư Danh mục", icon="📊")
elif selected_item == "Flash Deal":
    st.page_link("pages/Flash_Deal", label="Flash Deal", icon="⚡")
elif selected_item == "Hướng dẫn sử dụng":
    st.page_link("pages/Huong_dan_su_dung", label="Hướng dẫn sử dụng", icon="📘")
elif selected_item == "Liên hệ":
    st.page_link("pages/Lien_he", label="Liên hệ", icon="📞")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
