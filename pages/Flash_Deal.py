import streamlit as st

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
'''

# Áp dụng CSS tùy chỉnh
st.markdown(css_code, unsafe_allow_html=True)

# Hiển thị HTML trong Streamlit
st.markdown(html_code, unsafe_allow_html=True)
