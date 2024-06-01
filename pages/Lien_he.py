import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh


# Cấu hình trang web với chế độ wide mode
st.set_page_config(layout="wide")

st.title("Flash Deal") 
st.title("Mua Nhanh - Chốt lời lẹ")
st.write("Tín hiệu khuyến nghị thời gian thực - Dữ liệu được cập nhật 10 giây một lần từ 9h15 đến 15h00")  


selected2 = option_menu(None, ["FlashDeal", "Hướng dẫn"], 
    icons=['house', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


# Hàm để tải dữ liệu từ Google Sheets
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

# Hàm để hiển thị bảng với CSS tùy chỉnh
def display_with_css(df):
    # Đọc nội dung file CSS
    with open("css.style/flashdeal.css") as f:
        css = f.read()
    
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Định dạng giá trị của ô dữ liệu trong bảng HTML
    def format_value(val, class_name):
        if pd.isna(val):
            return f'<td class="{class_name}" data-value=""></td>'
        return f'<td class="{class_name}" data-value="{val}">{val}</td>'

    # Định dạng một hàng dữ liệu từ DataFrame thành thẻ HTML <td>
    def format_row(row):
        return [
            f'<td class="font_ticker">{row["Mã"]}</td>',
            format_value(row["Tín hiệu"], "tin_hieu"),
            f'<td class="gia_hien_tai" data-percent-value="{row["+/- %"]}">{row["Giá hiện tại"]}</td>',
            f'<td class="percent" data-value="{row["+/- %"]}">{row["+/- %"]}</td>'
        ]

    # Tạo HTML cho bảng từ DataFrame
    formatted_rows = [format_row(row) for _, row in df.iterrows()]
    html = "<table class='dataframe'>"
    html += "<thead><tr><th>Mã</th><th>Tín hiệu</th><th>Giá hiện tại</th><th>+/- %</th></tr></thead>"
    html += "<tbody>"
    for row in formatted_rows:
        html += "<tr>" + "".join(row) + "</tr>"
    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)

# Kiểm tra nếu 'FlashDeal' được chọn
if selected2 == "FlashDeal":
    data = load_data()
    display_with_css(data)

    # Tự động làm mới trang sau mỗi 10 giây
    st_autorefresh(interval=10 * 1000)

elif selected2 == "Hướng dẫn":
    st.write("settings is my bettings")
    

