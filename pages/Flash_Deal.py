import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

# Xử lý sự kiện sắp xếp
def handle_sort(column):
    if st.session_state['sort_column'] == column:
        st.session_state['sort_ascending'] = not st.session_state['sort_ascending']
    else:
        st.session_state['sort_column'] = column
        st.session_state['sort_ascending'] = True

# Hiển thị dữ liệu với CSS và tính năng sort
def display_with_css_and_sort(df):
    sort_column = st.session_state.get('sort_column', None)
    sort_ascending = st.session_state.get('sort_ascending', True)
    
    if sort_column:
        df = df.sort_values(by=sort_column, ascending=sort_ascending)

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
        th {{
            background-color: orange;  /* Nền màu cam cho tiêu đề */
            color: white;  /* Chữ màu trắng */
            text-align: center;  /* Văn bản căn giữa */
            border: 1px solid white;  /* Đường viền màu trắng */
            cursor: pointer;
        }}
        td {{
            background-color: white;  /* Nền màu trắng */
            border: 1px solid #ddd;  /* Đường viền màu xám nhạt */
            padding: 8px;
            text-align: left;
        }}
        .tin_hieu {{
            color: black;
        }}
        .tin_hieu[data-value="MUA"] {{
            color: green;  /* Màu xanh lá cây cho "MUA" */
        }}
        .tin_hieu[data-value="BÁN"] {{
            color: red;  /* Màu đỏ cho "BÁN" */
        }}
        .gia_hien_tai {{
            color: black;
        }}
        .gia_hien_tai[data-percent-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .gia_hien_tai[data-percent-value="0.0"],
        .gia_hien_tai[data-percent-value="0"],
        .gia_hien_tai[data-percent-value="0.00"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .gia_hien_tai[data-percent-value]:not([data-percent-value^="-"]):not([data-percent-value="0"]):not([data-percent-value="0.0"]):not([data-percent-value="0.00"]) {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        .percent {{
            color: black;
        }}
        .percent[data-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .percent[data-value="0.0"],
        .percent[data-value="0"],
        .percent[data-value="0.00"] {{
            color: yellow;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .percent[data-value]:not([data-value^="-"]):not([data-value="0"]):not([data-value="0.0"]):not([data-value="0.00"]) {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        </style>
        """, unsafe_allow_html=True
    )

    def format_value(val, class_name):
        if pd.isna(val):
            return f'<td class="{class_name}" data-value=""></td>'
        return f'<td class="{class_name}" data-value="{val}">{val}</td>'

    def format_row(row):
        percent_value = row["+/- %"]
        gia_hien_tai_color_class = ""
        if percent_value > 0:
            gia_hien_tai_color_class = "gia_hien_tai"
        elif percent_value < 0:
            gia_hien_tai_color_class = "gia_hien_tai"
        else:
            gia_hien_tai_color_class = "gia_hien_tai"
        
        return [
            f'<td>{row["Mã"]}</td>',
            format_value(row["Tín hiệu"], "tin_hieu"),
            f'<td class="{gia_hien_tai_color_class}" data-percent-value="{percent_value}">{row["Giá hiện tại"]}</td>',
            f'<td class="percent" data-value="{percent_value}">{percent_value}</td>'
        ]

    formatted_rows = [format_row(row) for _, row in df.iterrows()]
    html = "<table class='dataframe'>"
    html += "<thead><tr>"
    for col in df.columns:
        html += f'<th onclick="window.location.href=\'#{col}\'">{col}</th>'
    html += "</tr></thead>"
    html += "<tbody>"
    for row in formatted_rows:
        html += "<tr>" + "".join(row) + "</tr>"
    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)

# Đặt các giá trị mặc định cho session_state nếu chưa có
if 'sort_column' not in st.session_state:
    st.session_state['sort_column'] = None
if 'sort_ascending' not in st.session_state:
    st.session_state['sort_ascending'] = True

# Gọi hàm handle_sort khi nhấn vào tiêu đề cột
if st.button('Mã'):
    handle_sort('Mã')
if st.button('Tín hiệu'):
    handle_sort('Tín hiệu')
if st.button('Giá hiện tại'):
    handle_sort('Giá hiện tại')
if st.button('+/- %'):
    handle_sort('+/- %')

def main():
    # Cấu hình trang web với chế độ wide mode
    st.set_page_config(layout="wide")
    
    st.title("Flash Deal - Mua Nhanh - Chốt lời lẹ")
    st.write("Tín hiệu khuyến nghị của Flash Deal dựa trên Chiến lược Đầu tư Kỹ thuật")  
    st.write("Tín hiệu khuyến nghị thời gian thực - Cập nhật 10 giây một lần")  
    st.write("Từ 9h15 đến 15h00 dữ liệu được cập nhật liên tục trong phiên giao dịch.")
    
    data = load_data()
    
    display_with_css_and_sort(data)
    
    # Tự động làm mới trang sau mỗi 10 giây
    st_autorefresh(interval=10 * 1000)

if __name__ == "__main__":
    main()
