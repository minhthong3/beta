
# Page Bachground Image
# Function to get the base64 encoding of the binary file
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set a PNG image as the page background
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# Set the background image
set_png_as_page_bg('images/27324.jpg')


import streamlit as st
import base64

# Function to get the base64 encoding of the binary file
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set a PNG image as the page background
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

# Set the background image
set_png_as_page_bg('images/27324.jpg')


# TẠO SIDEBAR
# Sidebar title
st.sidebar.title("VNWEALTH")

# Sidebar menu with custom icons
menu_items = {
    "Thông tin thị trường": "📈",
    "Cổ phiếu chọn lọc": "⭐",
    "Đầu tư Danh mục": "📊",
    "Flash Deal": "⚡",
    "Hướng dẫn sử dụng": "📘",
    "Liên hệ": "📞"
}

selected_item = st.sidebar.radio(
    "",
    list(menu_items.keys()),
    format_func=lambda x: f"{menu_items[x]} {x}"
)

# TẠO PAGE
# Display page links in the main content
if selected_item == "Thông tin thị trường":
    st.page_link("Thong_tin_thi_truong", label="Thông tin thị trường", icon="📈")
elif selected_item == "Cổ phiếu chọn lọc":
    st.page_link("Co_phieu_chon_loc", label="Cổ phiếu chọn lọc", icon="⭐")
elif selected_item == "Đầu tư Danh mục":
    st.page_link("Dau_tu_Danh_muc", label="Đầu tư Danh mục", icon="📊")
elif selected_item == "Flash Deal":
    st.page_link("Flash_Deal", label="Flash Deal", icon="⚡")
elif selected_item == "Hướng dẫn sử dụng":
    st.page_link("Huong_dan_su_dung", label="Hướng dẫn sử dụng", icon="📘")
elif selected_item == "Liên hệ":
    st.page_link("Lien_he", label="Liên hệ", icon="📞")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")

#----------
# pages/Thong_tin_thi_truong.py
import streamlit as st

st.title("Thông tin thị trường")
st.header("Thông tin thị trường")
st.write("Nội dung cho phần Thông tin thị trường...")

#pages/Co_phieu_chon_loc.py
import streamlit as st

st.title("Cổ phiếu chọn lọc")
st.header("Cổ phiếu chọn lọc")
st.write("Nội dung cho phần Cổ phiếu chọn lọc...")

#pages/Dau_tu_Danh_muc.py
import streamlit as st

st.title("Đầu tư Danh mục")
st.header("Đầu tư Danh mục")
st.write("Nội dung cho phần Đầu tư Danh mục...")

# pages/Flash_Deal.py
import streamlit as st

st.title("Flash Deal")
st.header("Flash Deal")
st.write("Nội dung cho phần Flash Deal...")

#----------
# HÀM TẠO PROJECT DIRECTORY

import os
# Define the directory structure
project_directory = "your_project_directory"  # Thay thế bằng đường dẫn thực tế đến thư mục dự án của bạn
pages_directory = os.path.join(project_directory, "pages")
# Tạo các pages
page_files = ["Thong_tin_thi_truong.py", "Co_phieu_chon_loc.py", "Dau_tu_Danh_muc.py", "Flash_Deal.py", "Huong_dan_su_dung.py", "Lien_he.py"]

# Create the directory structure
os.makedirs(pages_directory, exist_ok=True)

#----------
# Content for each page file
page_content_template = """\
import streamlit as st

st.title("{title}")
st.header("{title}")
st.write("Nội dung cho phần {title}...")
"""