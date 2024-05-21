import streamlit as st

st.title("Hướng dẫn sử dụng")
st.header("Hướng dẫn sử dụng")
st.write("Nội dung cho phần Hướng dẫn sử dụng...")


# Đường link Canva cần nhúng
canva_link = "https://www.canva.com/design/DAGF3tP2xAo/6WUfuT0272AxPgYsV9593w/view"

# Mã HTML để nhúng liên kết Canva
html_code = f'<iframe src="{canva_link}" width="100%" height="600px" frameborder="0" allowfullscreen></iframe>'

# Hiển thị HTML trong Streamlit
st.markdown(html_code, unsafe_allow_html=True)
