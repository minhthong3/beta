import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Tiêu đề của ứng dụng
st.title("GoodStock")

# URL CSV từ Google Sheets
google_sheet_csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vStRBFjNcpDt-h9MWyZ6DQT_Oq9nv4hCI7tlxS56Pv5vNhq3i45tVvewqxE3sL30F7QfZNwacIxBEJk/pub?gid=0&single=true&output=csv"

# Tạo các tab
tab1, tab2 = st.tabs(["Khuyến nghị", "Hướng dẫn"])

with tab1:
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
        .highlight-mua {
            background-color: lightgreen !important;
        }
        .highlight-ban {
            background-color: red !important;
            color: white !important;
        }
        .highlight-phuhop {
            background-color: lightgreen !important;
        }
    </style>
    """

    try:
        # Đọc tệp CSV từ Google Sheets
        df = pd.read_csv(google_sheet_csv_url)

        # Thêm lớp CSS tùy chỉnh cho các ô có giá trị đặc biệt trong cột "Khuyến nghị"
        def apply_highlight(val):
            if val == 'MUA':
                return 'background-color: lightgreen'
            elif val == 'BÁN':
                return 'background-color: red; color: white'
            elif val == 'PHÙ HỢP THỊ TRƯỜNG':
                return 'background-color: lightgreen'
            else:
                return ''

        # Áp dụng lớp CSS tùy chỉnh
        df_styled = df.style.applymap(apply_highlight, subset=['Khuyến nghị'])

        # Áp dụng CSS tùy chỉnh
        st.markdown(css, unsafe_allow_html=True)
        
        # Hiển thị bảng dữ liệu với định dạng HTML và lớp CSS tùy chỉnh
        st.write("DANH MỤC ĐƯỢC ĐỊNH GIÁ:")
        st.write(df_styled.to_html(escape=False), unsafe_allow_html=True)

        # Tự động làm mới trang sau mỗi 15 giây
        st_autorefresh(interval=15 * 1000)

    except Exception as e:
        st.error(f"Không thể tải dữ liệu từ URL. Lỗi: {e}")

with tab2:
    from streamlit_navigation_bar import navigation_bar
    
    # Tạo các trang cho mỗi phần của thanh điều hướng
    def home():
        st.title("Home")
        st.write("Welcome to the home page!")
    
    def documentation():
        st.title("Documentation")
        st.write("Here you can find all the documentation.")
    
    def examples():
        st.title("Examples")
        st.write("Check out these cool examples.")
    
    def community():
        st.title("Community")
        st.write("Join our vibrant community!")
    
    def about():
        st.title("About")
        st.write("Learn more about our project.")
    
    # Thiết lập thanh điều hướng
    selected = navigation_bar(
        menu_title="Main Navigation",
        options=["Home", "Documentation", "Examples", "Community", "About"],
        icons=["house", "book", "app-indicator", "people", "info-circle"],
        menu_icon="cast",
        orientation="horizontal"
    )
    
    # Logic để hiển thị nội dung dựa trên lựa chọn của người dùng
    if selected == "Home":
        home()
    elif selected == "Documentation":
        documentation()
    elif selected == "Examples":
        examples()
    elif selected == "Community":
        community()
    elif selected == "About":
        about()
