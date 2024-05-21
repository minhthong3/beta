import streamlit as st

st.title("Đầu tư Danh mục")
st.header("Đầu tư Danh mục")
st.write("Nội dung cho phần Đầu tư Danh mục...")

import streamlit as st
from PIL import Image

# Load images
image_1 = Image.open("image.danhmuc/image_1.png").crop((0, 0, 512, 512)) # Chess piece
image_2 = Image.open("image.danhmuc/image_2.png").crop((512, 0, 1024, 512)) # Surfer
image_3 = Image.open("image.danhmuc/image_3.png").crop((1024, 0, 1536, 512)) # Coins
image_4 = Image.open("image.danhmuc/image_4.png").crop((0, 512, 512, 1024)) # Tree
image_5 = Image.open("image.danhmuc/image_5.png").crop((512, 512, 1024, 1024)) # Boxing gloves

# Custom CSS to style the cards
st.markdown("""
<style>
.card-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
    width: 18%;
    text-align: center;
    margin-bottom: 20px;
    color: white;
}
.card img {
    width: 100%;
    border-radius: 10px;
}
.card h3 {
    font-size: 1.5em;
    margin: 10px 0;
}
.card p {
    font-size: 1em;
    margin: 5px 0;
}
.card .highlight {
    color: #00FF00; /* Green */
}
.card .highlight.yellow {
    color: #FFFF00; /* Yellow */
}
</style>
""", unsafe_allow_html=True)

# Card data
cards = [
    {
        "title": "Nâng hạng thị trường",
        "image": image_1,
        "description": "Các DN đáp ứng tiêu chí nâng hạng thị trường theo FTSE và MSCI",
        "expected_return": "15%/năm",
        "risk": "Trung bình"
    },
    {
        "title": "Đầu tư thuận xu thế",
        "image": image_2,
        "description": "Các DN Ngân hàng, Chứng khoán, Thép hình thành xu hướng mạnh về...",
        "expected_return": "30%/năm",
        "risk": "Trung bình cao"
    },
    {
        "title": "Cổ tức ổn định",
        "image": image_3,
        "description": "Doanh nghiệp hoạt động kinh doanh ổn định, chi trả cổ tức cao và đều",
        "expected_return": "12%/năm",
        "risk": "Thấp"
    },
    {
        "title": "Đầu tư giá trị",
        "image": image_4,
        "description": "DN có sức khỏe tài chính lành mạnh, cổ tức cao, biến động giá thấp",
        "expected_return": "18%/năm",
        "risk": "Thấp"
    },
    {
        "title": "Lợi thế cạnh tranh",
        "image": image_5,
        "description": "DN có tỷ suất lợi nhuận cao, sức khỏe tài chính lành mạnh",
        "expected_return": "20%/năm",
        "risk": "Trung bình thấp"
    }
]

# Render the cards
st.markdown('<div class="card-container">', unsafe_allow_html=True)
for card in cards:
    st.markdown(f"""
    <div class="card">
        <img src="{card['image']}" alt="{card['title']}">
        <h3>{card['title']}</h3>
        <p>{card['description']}</p>
        <p>Sinh lời kỳ vọng: <span class="highlight">{card['expected_return']}</span></p>
        <p>Rủi ro: <span class="highlight yellow">{card['risk']}</span></p>
        <button>Xem chi tiết</button>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
