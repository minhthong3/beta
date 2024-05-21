import streamlit as st

st.title("Liên hệ")
st.header("Liên hệ")
st.write("Nội dung cho phần Liên hệ...")



# Đường link Canva cần nhúng
canva_link = "https://aaaadfe.my.canva.site/"

# Mã HTML để nhúng liên kết Canva
html_code = f'<iframe src="{canva_link}" width="100%" height="600px" frameborder="0" allowfullscreen></iframe>'

# Hiển thị HTML trong Streamlit
st.markdown(html_code, unsafe_allow_html=True)

