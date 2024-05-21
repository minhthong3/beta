import streamlit as st

st.title("Flash Deal")
st.header("Flash Deal")
st.write("Nội dung cho phần Flash Deal...")

import streamlit as st

def main():
    st.title("Nhúng Canva vào ứng dụng Streamlit")

    # Đường dẫn đến trang web Canva cụ thể
    canva_url = "https://www.canva.com/design/DAGF3tP2xAo/Js0hl4gPnM9QgnWkpPL2Ng/view?utm_content=DAGF3tP2xAo&utm_campaign=designshare&utm_medium=link&utm_source=editor"

    # Hiển thị trang web Canva bằng iframe
    st.write(f'<iframe src="{canva_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

