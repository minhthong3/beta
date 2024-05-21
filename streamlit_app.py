import streamlit as st
import base64

# Link to the respective pages
if selected_item == "Thông tin thị trường":
    st.switch_page("Thong_tin_thi_truong")
elif selected_item == "Cổ phiếu chọn lọc":
    st.switch_page("Co_phieu_chon_loc")
elif selected_item == "Đầu tư Danh mục":
    st.switch_page("Dau_tu_Danh_muc")
elif selected_item == "Flash Deal":
    st.switch_page("Flash_Deal")
elif selected_item == "Hướng dẫn sử dụng":
    st.switch_page("Huong_dan_su_dung")
elif selected_item == "Liên hệ":
    st.switch_page("Lien_he")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
