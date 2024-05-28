import streamlit as st
import pandas as pd

# Tiêu đề của ứng dụng
st.title("Hiển thị Bảng Dữ liệu từ Google Sheets")

# URL CSV từ Google Sheets
google_sheet_csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTn8rFdZh3D0fL9_k1VpGflP8OeJlZoEE5tA4ISUwx3u8SdsbJZt9ohSzkEJSI1pxy5Z1iVZjFN5QQZ/pub?output=csv"

try:
    # Đọc tệp CSV từ Google Sheets
    df = pd.read_csv(google_sheet_csv_url)

    # Hiển thị bảng dữ liệu
    st.write("Dữ liệu của bạn:")
    st.dataframe(df)

    # Hiển thị thống kê mô tả
    st.write("Thống kê mô tả:")
    st.dataframe(df.describe())

except Exception as e:
    st.error(f"Không thể tải dữ liệu từ URL. Lỗi: {e}")
