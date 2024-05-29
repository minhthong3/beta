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
        table {{
            width: 80%;
            border-collapse: collapse;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }}
        .dataframe th {{
            background-color: orange;  /* Nền màu cam cho tiêu đề */
            color: white;  /* Chữ màu trắng */
            text-align: center;  /* Văn bản căn giữa */
            border: 1px solid white;  /* Đường viền màu trắng */
        }}
        .dataframe td {{
            background-color: white;  /* Nền màu trắng */
            border: 1px solid #ddd;  /* Đường viền màu xám nhạt */
            padding: 8px;
            text-align: left;
        }}
        .dataframe td.tin_hieu {{
            color: black;
        }}
        .dataframe td.tin_hieu[data-value="MUA"] {{
            color: green;  /* Màu xanh lá cây cho "MUA" */
        }}
        .dataframe td.tin_hieu[data-value="BÁN"] {{
            color: red;  /* Màu đỏ cho "BÁN" */
        }}
        .dataframe td.gia_hien_tai {{
            color: black;
        }}
        .dataframe td.gia_hien_tai[data-percent-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .dataframe td.gia_hien_tai[data-percent-value="0"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .dataframe td.gia_hien_tai[data-percent-value^="0"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .dataframe td.gia_hien_tai[data-percent-value] {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        .dataframe td.percent {{
            color: black;
        }}
        .dataframe td.percent[data-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .dataframe td.percent[data-value="0"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .dataframe td.percent[data-value^="0"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .dataframe td.percent[data-value] {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        </style>
        """, unsafe_allow_html=True
    )
    
    df = pd.read_csv(csv_file_path)
    # Thay thế NaN bằng chuỗi trắng trong cột "Tín hiệu"
    if 'Tín hiệu' in df.columns:
        df['Tín hiệu'] = df['Tín hiệu'].fillna('')
    # Tạo HTML cho các cột
    df['+/- %'] = df['+/- %'].apply(lambda x: f'<td class="percent" data-value="{x}">{x}</td>')
    df['Tín hiệu'] = df['Tín hiệu'].apply(lambda x: f'<td class="tin_hieu" data-value="{x}">{x}</td>')
    df['Giá hiện tại'] = df.apply(lambda row: f'<td class="gia_hien_tai" data-percent-value="{row["+/- %"]}">{row["Giá hiện tại"]}</td>', axis=1)
    
    st.write(df.to_html(classes='dataframe', index=False, escape=False), unsafe_allow_html=True)

def main():
    # Cấu hình trang web với chế độ wide mode
    st.set_page_config(layout="wide")
    
    st.title("Flash Deal - Mua Nhanh - Chốt lời lẹ")
    st.write("Tín hiệu khuyến nghị của Flash Deal dựa trên Chiến lược Đầu tư Kỹ thuật")  
    st.write("Tín hiệu khuyến nghị thời gian thực - Cập nhật 10 giây một lần")  
    st.write("Từ 9h15 đến 15h00 dữ liệu được cập nhật liên tục trong phiên giao dịch.")
    
    data = load_data()
    
    csv_file_path = save_to_csv(data)
    
    display_with_css(csv_file_path)
    
    # Tự động làm mới trang sau mỗi 10 giây
    st_autorefresh(interval=10 * 1000)

if __name__ == "__main__":
    main()
