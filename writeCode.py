import os

# Define the directory structure
project_directory = "G:\\My Drive\\VNW.WEBAPP\\beta"  # Thay thế bằng đường dẫn thực tế đến thư mục dự án của bạn
pages_directory = os.path.join(project_directory, "pages")
page_files = ["Thong_tin_thi_truong.py", "Co_phieu_chon_loc.py", "Dau_tu_Danh_muc.py", "Flash_Deal.py", "Huong_dan_su_dung.py", "Lien_he.py"]

# Create the directory structure
os.makedirs(pages_directory, exist_ok=True)

# Content for each page file
page_content_template = """\
import streamlit as st

"""

# Write each page file
for page_file in page_files:
    title = page_file.replace("_", " ").replace(".py", "")
    page_content = page_content_template.format(title=title)
    page_path = os.path.join(pages_directory, page_file)
    with open(page_path, "w") as f:
        f.write(page_content)
        print(f"Tạo thành công tệp: {page_path}")

print(f"Cấu trúc thư mục và các tệp đã được tạo trong {pages_directory}")
