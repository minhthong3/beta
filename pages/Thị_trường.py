import streamlit as st
from streamlit_navigation_bar import st_navbar

# Set initial configuration for the Streamlit app
st.set_page_config(page_title="GoodStock Analysis", initial_sidebar_state="collapsed")

# Define the pages and custom styles for the navigation bar
pages = ["Home", "Documentation", "Examples", "Community", "About"]
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
        "width": "100%",
    },
    "div": {
        "width": "100%",
        "margin": "auto"
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.5 rem",  # Tăng khoảng cách ngang giữa các mục
        "padding": "0.4375rem 0.625rem",
        "display": "inline-block",
        "white-space": "nowrap",
        "font-size": "14px"
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)"
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)"
    },
}

# Implement navigation bar and get the currently selected page
selected_page = st_navbar(pages, styles=styles)

# Define the content for each page and display it
def home():
    st.title("Home")
    st.write("Welcome to the home page!")

def documentation():
    st.title("Documentation")
    st.write("Here you can find all the documentation.")
    # Thiết lập tiêu đề cho ứng dụng
st.title(" vnwPortfolio ")
st. write('VNWEALTH mang đến sản phẩm Danh mục đầu tư mẫu với 5 danh mục được nghiên cứu theo chiến lược của các huyền thoại đầu tư như Warren Buffett hay Philip Fisher, để sẵn sàng cùng bạn chạm được cột mốc cao nhất trong hành trình này.')
st. write('Danh mục cổ phiếu là một tập hợp các cổ phiếu được lựa chọn từ nhiều ngành và lĩnh vực khác nhau. Mục đích của việc xây dựng danh mục này là đa dạng hóa đầu tư, giảm thiểu rủi ro và tối đa hóa lợi nhuận dài hạn')
# CSS để làm cho nội dung chính rộng toàn màn hình
css_code = """
<style>
    .main > div {
        max-width: 100%;
        padding-left: 5%;
        padding-right: 5%;
    }
</style>
"""

# Mã HTML để nhúng
html_code = '''

<div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.2em; margin-bottom: 0.5em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGF7v8behA&#x2F;aeUkg5aplUgG4XKANvKrSw&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGF7v8behA&#x2F;aeUkg5aplUgG4XKANvKrSw&#x2F;view?utm_content=DAGF7v8behA&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">
'''

# Áp dụng CSS tùy chỉnh
st.markdown(css_code, unsafe_allow_html=True)

# Hiển thị HTML trong Streamlit
st.markdown(html_code, unsafe_allow_html=True)



# Thiết lập tiêu đề cho ứng dụng
st.title("XEM CHI TIẾT")
st.write('Được cập nhật mỗi tháng, cập nhật gần nhất 02/05/2024')
# Sử dụng st.tabs để tạo các tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Đầu tư giá trị", "Đầu tư tăng trưởng", "Cổ tức bền vững", "Đầu tư phòng thủ", "Cơ hội đổi đời"])

# Nội dung cho tab 1
with tab1:
    st.header("Đầu tư giá trị")
    st.write("Đây là nội dung của Tab 1.")
    # Mã HTML để nhúng
    html_code = '''
    <div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
     padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
     border-radius: 8px; will-change: transform;">
      <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
        src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGGbeRekAE&#x2F;O1EpPEZ1Of7YCziHtJCm-g&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
          </iframe>
    </div>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGGbeRekAE&#x2F;O1EpPEZ1Of7YCziHtJCm-g&#x2F;view?utm_content=DAGGbeRekAE&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">
    '''

# Nội dung cho tab 2
with tab2:
    st.header("Đầu tư tăng trưởng")
    st.write("Đây là nội dung của Tab 2.")

# Nội dung cho tab 3
with tab3:
    st.header("Cổ tức bền vững")
    st.write("Đây là nội dung của Tab 3.")

# Nội dung cho tab 4
with tab4:
    st.header("Đầu tư phòng thủ")
    st.write("Đây là nội dung của Tab 4.")

# Nội dung cho tab 5
with tab5:
    st.header("Cơ hội đổi đời")
    st.write("Đây là nội dung của Tab 5.")

def examples():
    st.title("Examples")
    st.write("Check out these cool examples.")

def community():
    st.title("Community")
    st.write("Join our vibrant community!")

def about():
    st.title("About")
    st.write("Learn more about our project.")

if selected_page == "Home":
    home()
elif selected_page == "Documentation":
    documentation()
elif selected_page == "Examples":
    examples()
elif selected_page == "Community":
    community()
elif selected_page == "About":
    about()

# Sidebar content
with st.sidebar:
    st.write("Sidebar")
