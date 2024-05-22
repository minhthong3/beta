import streamlit as st
import base64

# Đọc hình ảnh từ file và chuyển sang base64
def get_image_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Danh sách các thẻ với thông tin chi tiết
cards = [
    {
        "title": "Nâng hạng thị trường",
        "description": "Các DN đáp ứng tiêu chí nâng hạng thị trường theo FTSE và MSCI",
        "expected_return": "15%/năm",
        "risk": "Trung bình",
        "image_base64": get_image_base64("/mnt/data/image1.jpg")
    },
    {
        "title": "Đầu tư thuận xu thế",
        "description": "Các DN Ngân hàng, Chứng khoán, Thép hình thành xu hướng mạnh về...",
        "expected_return": "30%/năm",
        "risk": "Trung bình cao",
        "image_base64": get_image_base64("/mnt/data/image2.jpg")
    },
    {
        "title": "Cổ tức ổn định",
        "description": "Doanh nghiệp hoạt động kinh doanh ổn định, chi trả cổ tức cao và đều, thanh khoản tốt",
        "expected_return": "12%/năm",
        "risk": "Thấp",
        "image_base64": get_image_base64("/mnt/data/image3.jpg")
    },
    {
        "title": "Đầu tư giá trị",
        "description": "DN có sức khỏe tài chính lành mạnh, cổ tức cao, biến động giá thấp.",
        "expected_return": "18%/năm",
        "risk": "Thấp",
        "image_base64": get_image_base64("/mnt/data/image4.jpg")
    },
    {
        "title": "Lợi thế cạnh tranh",
        "description": "DN có tỷ suất lợi nhuận cao, sức khỏe tài chính lành mạnh",
        "expected_return": "20%/năm",
        "risk": "Trung bình thấp",
        "image_base64": get_image_base64("/mnt/data/image5.jpg")
    },
]

# Tạo các tab cho nội dung chi tiết
tabs = st.tabs([card['title'] for card in cards])

# Hiển thị thẻ và liên kết đến tab tương ứng
cols = st.columns(5)
for col, card, tab in zip(cols, cards, tabs):
    with col:
        if st.button(f"Xem chi tiết - {card['title']}"):
            st.session_state['selected_tab'] = card['title']
        st.markdown(f"""
        <div class="card">
            <img src="data:image/jpeg;base64,{card['image_base64']}" alt="{card['title']}">
            <h3>{card['title']}</h3>
            <p>{card['description']}</p>
            <p>Sinh lời kỳ vọng: <span class="highlight">{card['expected_return']}</span></p>
            <p>Rủi ro: <span class="highlight yellow">{card['risk']}</span></p>
        </div>
        """, unsafe_allow_html=True)

# Hiển thị nội dung chi tiết trong các tab
for tab, card in zip(tabs, cards):
    with tab:
        st.markdown(f"## {card['title']}")
        st.markdown(f"""
        <img src="data:image/jpeg;base64,{card['image_base64']}" alt="{card['title']}" style="width:100%">
        <p>{card['description']}</p>
        <p>Sinh lời kỳ vọng: <span class="highlight">{card['expected_return']}</span></p>
        <p>Rủi ro: <span class="highlight yellow">{card['risk']}</span></p>
        """)

# Chuyển đến tab đã chọn nếu có
if 'selected_tab' in st.session_state:
    selected_tab = st.session_state['selected_tab']
    selected_index = next(i for i, card in enumerate(cards) if card['title'] == selected_tab)
    st.experimental_set_query_params(tab=selected_index)
