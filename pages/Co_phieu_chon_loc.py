import streamlit as st
import pandas as pd

# CSS tùy chỉnh cho bảng
css = """
<style>
    .dataframe {
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }
    .dataframe th, .dataframe td {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    .dataframe tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .dataframe th {
        background-color: #4CAF50;
        color: white;
    }
</style>
"""

# Tiêu đề của ứng dụng
st.title("Hiển thị Bảng Dữ liệu từ Google Sheets")

# URL CSV từ Google Sheets
google_sheet_csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vStRBFjNcpDt-h9MWyZ6DQT_Oq9nv4hCI7tlxS56Pv5vNhq3i45tVvewqxE3sL30F7QfZNwacIxBEJk/pub?gid=0&single=true&output=csv"

try:
    # Đọc tệp CSV từ Google Sheets
    df = pd.read_csv(google_sheet_csv_url)

    # Áp dụng CSS tùy chỉnh
    st.markdown(css, unsafe_allow_html=True)
    
    # Hiển thị bảng dữ liệu với định dạng HTML
    st.write("Dữ liệu của bạn:")
    st.write(df.to_html(classes='dataframe'), unsafe_allow_html=True)

    # Hiển thị thống kê mô tả với định dạng HTML
    st.write("Thống kê mô tả:")
    st.write(df.describe().to_html(classes='dataframe'), unsafe_allow_html=True)

except Exception as e:
    st.error(f"Không thể tải dữ liệu từ URL. Lỗi: {e}")
