import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tempfile

# Cấu hình xác thực
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("image.danhmuc/datavnwealth-25a353ea3781.json", scope)
client = gspread.authorize(creds)

# URL của Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/1kkOjUihnNpcWn8jmNM7majctXlqU18fGvwlTOVi9efg/edit#gid=0"

# Đọc dữ liệu từ Google Sheets
def load_data():
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Chuyển dữ liệu thành CSV và lưu vào bộ nhớ tạm thời
def save_to_csv(df):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file.name

# Hiển thị dữ liệu với CSS
def display_with_css(csv_file_path):
    st.markdown(
        f"""
        <style>
        .dataframe {{
            border: 2px solid black;
            border-collapse: collapse;
            width: 100%;
        }}
        .dataframe th, .dataframe td {{
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }}
        .dataframe th {{
            background-color: #f2f2f2;
        }}
        </style>
        """, unsafe_allow_html=True
    )
    
    df = pd.read_csv(csv_file_path)
    st.write(df.to_html(classes='dataframe', index=False), unsafe_allow_html=True)

def main():
    st.title("Flash Deal - Mua Nhanh - Chốt lời lẹ")
    st.write(" Tín hiệu khuyến nghị của Flash Deal dựa trên Chiến lược Đầu tư Kỹ thuật")  
    st.write(" Tín hiệu khuyến nghị thời gian thực - Cập nhật 10 giây một lần")  
    
    data = load_data()
    
    csv_file_path = save_to_csv(data)
    
    display_with_css(csv_file_path)
    
    # Tự động làm mới trang sau mỗi 60 giây
    st_autorefresh(interval=10 * 1000)

if __name__ == "__main__":
    main()
