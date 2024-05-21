import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
def image_to_base64(img_path):
    img = Image.open(img_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Load and convert images to base64
image_1_base64 = image_to_base64("image.danhmuc/image_1.png")
image_2_base64 = image_to_base64("image.danhmuc/image_2.png")
image_3_base64 = image_to_base64("image.danhmuc/image_3.png")
image_4_base64 = image_to_base64("image.danhmuc/image_4.png")
image_5_base64 = image_to_base64("image.danhmuc/image_5.png")

# Custom CSS to style the cards
st.markdown("""
<style>
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    box-sizing: border-box;
    margin-bottom: 20px;
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
button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
</style>
""", unsafe_allow_html=True)

# Card data
cards = [
    {
        "title": "Nâng hạng thị trường",
        "image_base64": image_1_base64,
        "description": "Các DN đáp ứng tiêu chí nâng hạng thị trường theo FTSE và MSCI",
        "expected_return": "15%/năm",
        "risk": "Trung bình"
    },
    {
        "title": "Đầu tư thuận xu thế",
        "image_base64": image_2_base64,
        "description": "Các DN Ngân hàng, Chứng khoán, Thép hình thành xu hướng mạnh về...",
        "expected_return": "30%/năm",
        "risk": "Trung bình cao"
    },
    {
        "title": "Cổ tức ổn định",
        "image_base64": image_3_base64,
        "description": "Doanh nghiệp hoạt động kinh doanh ổn định, chi trả cổ tức cao và đều",
        "expected_return": "12%/năm",
        "risk": "Thấp"
    },
    {
        "title": "Đầu tư giá trị",
        "image_base64": image_4_base64,
        "description": "DN có sức khỏe tài chính lành mạnh, cổ tức cao, biến động giá thấp",
        "expected_return": "18%/năm",
        "risk": "Thấp"
    },
    {
        "title": "Lợi thế cạnh tranh",
        "image_base64": image_5_base64,
        "description": "DN có tỷ suất lợi nhuận cao, sức khỏe tài chính lành mạnh",
        "expected_return": "20%/năm",
        "risk": "Trung bình thấp"
    }
]

# Create columns and render the cards
cols = st.columns(len(cards), gap="small")

for col, card in zip(cols, cards):
    with col:
        st.markdown(f"""
        <div class="card">
            <img src="data:image/png;base64,{card['image_base64']}" alt="{card['title']}">
            <h3>{card['title']}</h3>
            <p>{card['description']}</p>
            <p>Sinh lời kỳ vọng: <span class="highlight">{card['expected_return']}</span></p>
            <p>Rủi ro: <span class="highlight yellow">{card['risk']}</span></p>
            <button>Xem chi tiết</button>
        </div>
        """, unsafe_allow_html=True)
