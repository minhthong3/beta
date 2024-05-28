import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Cấu hình xác thực
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)

# URL của Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/your_google_sheet_id_here"

# Đọc dữ liệu từ Google Sheets
@st.cache_data
def load_data():
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Hiển thị dữ liệu
def main():
    st.title("Google Sheets Data in Streamlit")
    
    st.write("Dữ liệu từ Google Sheets:")
    
    data = load_data()
    
    st.write(data)

if __name__ == "__main__":
    main()
