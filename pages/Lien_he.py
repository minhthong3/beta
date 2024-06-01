import streamlit as st
from streamlit_option_menu import option_menu



selected2 = option_menu(None, ["Home", "Upload"], 
    icons=['house', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2
# Thiết lập tiêu đề cho ứng dụng
st.title(" vnwPortfolio ")
st. write('VNWEALTH mang đến sản phẩm Danh mục đầu tư mẫu với 5 danh mục được nghiên cứu theo chiến lược của các huyền thoại đầu tư như Warren Buffett hay Philip Fisher, để sẵn sàng cùng bạn chạm được cột mốc cao nhất trong hành trình này.')
st. write('Danh mục cổ phiếu là một tập hợp các cổ phiếu được lựa chọn từ nhiều ngành và lĩnh vực khác nhau. Mục đích của việc xây dựng danh mục này là đa dạng hóa đầu tư, giảm thiểu rủi ro và tối đa hóa lợi nhuận dài hạn')

if selected2 == "Home":
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
else:
    st.write("settings is my bettings")


