import os

# Define the directory structure
project_directory = "G:\\My Drive\\VNW.WEBAPP\\beta"  # Thay thế bằng đường dẫn thực tế đến thư mục dự án của bạn
pages_directory = os.path.join(project_directory, "pages")
page_files = [
    ("Thi_truong.py", "Thị trường"),
    ("Co_phieu_chon_loc.py", "Cổ phiếu chọn lọc"),
    ("Dau_tu_Danh_muc.py", "Đầu tư Danh mục"),
    ("Flash_Deal.py", "Flash Deal"),
    ("Huong_dan_su_dung.py", "Hướng dẫn sử dụng"),
    ("Lien_he.py", "Liên hệ")
]

# Create the directory structure
os.makedirs(pages_directory, exist_ok=True)

# Content for each page file
page_content_template = """\
import streamlit as st

st.title("{title}")
st.header("{title}")
st.write("Nội dung cho phần {title}...")
"""

# Write each page file
for page_file, title in page_files:
    page_content = page_content_template.format(title=title)
    page_path = os.path.join(pages_directory, page_file)
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(page_content)
        print(f"Tạo thành công tệp: {page_path}")

print(f"Cấu trúc thư mục và các tệp đã được tạo trong {pages_directory}")

