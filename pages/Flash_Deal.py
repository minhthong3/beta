import streamlit as st

def main():
    st.title("Nhúng Canva vào ứng dụng Streamlit")

    # Đoạn mã HTML từ Canva
    canva_html = '''
    <style>
        .full-width-content {
            width: 100%;
            max-width: 100%;
            padding: 0;
        }
    </style>

    <div class="full-width-content">
        <div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
            padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
            border-radius: 8px; will-change: transform;">
            <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
                src="https://www.canva.com/design/DAGF3tP2xAo/6WUfuT0272AxPgYsV9593w/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
            </iframe>
        </div>
        <a href="https://www.canva.com/design/DAGF3tP2xAo/6WUfuT0272AxPgYsV9593w/view?utm_content=DAGF3tP2xAo&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Design</a> by Minh Thông Nguyễn
    </div>
    '''

    # Hiển thị đoạn mã HTML bằng cách sử dụng st.markdown với option unsafe_allow_html=True
    st.markdown(canva_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
