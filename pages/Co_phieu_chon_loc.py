import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Thiết lập thông tin đăng nhập và quyền truy cập
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("image.danhmuc/datavnwealth-25a353ea3781.json", scope)
client = gspread.authorize(creds)

# Lấy dữ liệu từ Google Sheets
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/19TRaGNqO9darTuF5_2xCLEqoWOXZpUiTIIQMP1JeiTU/edit?usp=sharing")
sheet = spreadsheet.sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

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

# Áp dụng CSS tùy chỉnh
st.markdown(css, unsafe_allow_html=True)

# Hiển thị bảng dữ liệu với định dạng HTML
st.write("Dữ liệu của bạn:")
st.write(df.to_html(classes='dataframe'), unsafe_allow_html=True)

# Hiển thị thống kê mô tả với định dạng HTML
st.write("Thống kê mô tả:")
st.write(df.describe().to_html(classes='dataframe'), unsafe_allow_html=True)
