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

# Tiêu đề của ứng dụng
st.title("Hiển thị Bảng Dữ liệu từ Google Sheets")

# Hiển thị bảng dữ liệu
st.write("Dữ liệu của bạn:")
st.dataframe(df)

# Hiển thị thống kê mô tả
st.write("Thống kê mô tả:")
st.dataframe(df.describe())
