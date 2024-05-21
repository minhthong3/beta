import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
@st.cache_data
def image_to_base64(img_path, resize_to=(300, 300), quality=85):
    img = Image.open(img_path)
    img = img.resize(resize_to)  # Resize image to reduce file size
    buffered = BytesIO()
    img.save(buffered, format="JPEG", quality=quality)  # Save as JPEG to reduce size
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
.card-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
}
.card {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
    width: 18%;
    flex-grow: 1;
    box-sizing: border-box;
}
.card img {
    width: 100%;
    border-radius: 10px;
}
.card h3 {
    font-size: 1.2em;
    margin: 10px 0;
}
.card p {
    font-size: 0.9em;
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

# Create container for cards
st.markdown('<div class="card-container">', unsafe_allow_html=True)

# Render the cards
for card in cards:
    st.markdown(f"""
    <div class="card">
        <img src="data:image/jpeg;base64,{card['image_base64']}" alt="{card['title']}">
        <h3>{card['title']}</h3>
        <p>{card['description']}</p>
        <p>Sinh lời kỳ vọng: <span class="highlight">{card['expected_return']}</span></p>
        <p>Rủi ro: <span class="highlight yellow">{card['risk']}</span></p>
        <button>Xem chi tiết</button>
    </div>
    """, unsafe_allow_html=True)

# Close container for cards
st.markdown('</div>', unsafe_allow_html=True)


import streamlit as st

# HTML code to embed
html_code = '''
<div style="position: relative; width: 100%; height: 0; padding-top: 141.4286%; padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden; border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0; margin: 0;"
    src="https://www.canva.com/design/DAGF3gLOxfY/r7jI3obh1jMio2XWo5OOHw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https://www.canva.com/design/DAGF3gLOxfY/r7jI3obh1jMio2XWo5OOHw/view?utm_content=DAGF3gLOxfY&utm_campaign=designshare&utm_medium=embeds&utm_source=link" target="_blank" rel="noopener">Green White Illustrative Biology photosynthetic organisms Poster</a> by Minh Thông Nguyễn
'''

# Display the HTML in Streamlit
st.markdown(html_code, unsafe_allow_html=True)

