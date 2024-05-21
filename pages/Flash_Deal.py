import streamlit as st

def main():
    st.title("Nhúng đoạn mã từ Canva vào ứng dụng Streamlit")

    # Đoạn mã HTML và CSS từ Canva
    canva_code = '''
    <style>
        .full-screen-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 9999;
        }

        .canva-iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>

    <div class="full-screen-container">
        <iframe class="canva-iframe" src="https://www.canva.com/design/DAGF3tP2xAo/6WUfuT0272AxPgYsV9593w/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
        </iframe>
    </div>
    '''

    # Hiển thị đoạn mã bằng cách sử dụng st.components.html
    st.components.v1.html(canva_code)

if __name__ == "__main__":
    main()
