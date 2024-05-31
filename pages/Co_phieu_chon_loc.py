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
    from streamlit_option_menu import option_menu
    
    # Cho phép sử dụng CSS trong Streamlit
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # Gọi hàm với đường dẫn chính xác, chú ý đến khoảng trắng trong tên thư mục
    local_css("css library/style.css")

    
    # Tạo thanh menu tab
    selected = option_menu
    (
    menu_title=None,  # Không tiêu đề cho menu
    options=["Home", "GoodStock Analysis"],  # Tên các tab
    icons=["house", "graph-up-arrow"],  # Icons cho từng tab
    menu_icon="cast",  # Icon cho menu
    default_index=1,  # Mặc định chọn tab "GoodStock Analysis"
    orientation="horizontal"
    )
    
    if selected == "GoodStock Analysis":
        # Nội dung cho tab "GoodStock Analysis"
        st.markdown("""
        <div class="content">
            <h1>GoodStock - Cổ phiếu tiềm năng</h1>
            <h2>Phương pháp – Triết lý đầu tư</h2>
            <p>GoodStock cung cấp dự báo và khuyến nghị đối với các cổ phiếu bị định giá thấp so với giá trị thực của chúng.
            GoodStock sử dụng phân tích cơ bản để đánh giá tình hình tài chính, hiệu suất kinh doanh, và triển vọng của công ty có xét đến yếu tố vĩ mô ảnh hưởng đến ngành, doanh nghiệp, đồng thời áp dụng các phương pháp định giá để xác định giá trị thực của cổ phiếu so với giá thị trường.</p>
            
            <h2>Nhà đầu tư phù hợp với Cổ phiếu tiềm năng</h2>
            <ul>
                <li>Không có nhiều thời gian để theo dõi thị trường</li>
                <li>Tập trung tiềm năng tăng trưởng dài hạn của công ty, tìm kiếm lợi nhuận bền vững và tránh rủi ro không cần thiết</li>
                <li>Chiến lược giao giao dịch trung-dài hạn (từ 1-2 năm)</li>
                <li>Không chuyên hoặc mới tham gia thị trường</li>
            </ul>
            
            <h2>Hệ thống khuyến nghị của GoodStock</h2>
            <p>Khuyến nghị được đưa ra dựa trên mức tăng/giảm của giá cổ phiếu để đạt đến giá mục tiêu, được xác định bằng công thức (giá mục tiêu - giá hiện tại)/giá hiện tại</p>
            <ul>
                <li>MUA: lợi nhuận (bao gồm cổ tức) trong 12 tháng tới dự báo sẽ trên 20%</li>
                <li>KHẢ QUAN: lợi nhuận (bao gồm cổ tức) trong 12 tháng tới dự báo sẽ dương từ 10%-20%</li>
                <li>PHÙ HỢP THỊ TRƯỜNG: lợi nhuận (bao gồm cổ tức) trong 12 tháng tới dự báo sẽ dao động trong khoảng âm 10% và dương 10%</li>
                <li>KÉM KHÁ QUAN: lợi nhuận (bao gồm cổ tức) trong 12 tháng tới dự báo sẽ âm từ 10%-20%</li>
                <li>BÁN: lợi nhuận (bao gồm cổ tức) trong 12 tháng tới dự báo sẽ âm trên 20%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

