import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_option_menu import option_menu
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(layout="wide")  # Đặt cấu hình trang một lần ở đầu chương trình

selected2 = option_menu(None, ["FlashDeal", "Hướng dẫn"], 
    icons=['house', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

def load_data():
    # Cấu hình xác thực
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("image.danhmuc/datavnwealth-25a353ea3781.json", scope)
    client = gspread.authorize(creds)

    # URL của Google Sheets
    sheet_url = "https://docs.google.com/spreadsheets/d/1kkOjUihnNpcWn8jmNM7majctXlqU18fGvwlTOVi9efg/edit#gid=0"
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

def display_with_css(df):
    st.markdown(
        f"""
        <style>
        table {{
            width: 95%;
            border-collapse: collapse;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }}
        th {{
            background-color: orange;
            color: white;
            text-align: center;
            border: 1px solid white;
        }}
        td {{
            background-color: white;
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        .tin_hieu[data-value="MUA"] {{
            color: green;
        }}
        .tin_hieu[data-value="BÁN"] {{
            color: red;
        }}
        .gia_hien_tai {{
            color: black;
        }}
        .percent[data-value^="-"] {{
            color: red;
        }}
        .percent[data-value="0.0"], .percent[data-value="0"], .percent[data-value="0.00"] {{
            color: orange;
        }}
        .percent[data-value]:not([data-value^="-"]):not([data-value="0"]):not([data-value="0.0"]):not([data-value="0.00"]) {{
            color: green;
        }}
        </style>
        """, unsafe_allow_html=True
    )

    def format_value(val, class_name):
        if pd.isna(val):
            return f'<td class="{class_name}" data-value=""></td>'
        return f'<td class="{class_name}" data-value="{val}">{val}</td>'

    def format_row(row):
        return [
            f'<td>{row["Mã"]}</td>',
            format_value(row["Tín hiệu"], "tin_hieu"),
            f'<td class="gia_hien_tai" data-percent-value="{row["+/- %"]}">{row["Giá hiện tại"]}</td>',
            f'<td class="percent" data-value="{row["+/- %"]}">{row["+/- %"]}</td>'
        ]

    formatted_rows = [format_row(row) for _, row in df.iterrows()]
    html = "<table class='dataframe'>"
    html += "<thead><tr><th>Mã</th><th>Tín hiệu</th><th>Giá hiện tại</th><th>+/- %</th></tr></thead>"
    html += "<tbody>"
    for row in formatted_rows:
        html += "<tr>" + "".join(row) + "</tr>"
    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)


if selected2 == "FlashDeal":
    st.title("Flash Deal - Mua Nhanh - Chốt lời lẹ")
    st.write("Tín hiệu khuyến nghị của Flash Deal dựa trên Chiến lược Đầu tư Kỹ thuật")  
    st.write("Tín hiệu khuyến nghị thời gian thực - Dữ liệu được cập nhật 10 giây một lần từ 9h15 đến 15h00")  

    data = load_data()
    
    display_with_css(data)
    
    # Tự động làm mới trang sau mỗi 10 giây
    st_autorefresh(interval=10 * 1000)

elif selected2 == "Hướng dẫn":
    st.write("settings is my bettings")
