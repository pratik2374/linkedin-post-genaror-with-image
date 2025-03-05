import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from image import generate_post_with_image

# Page Configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📢",
    layout="wide"
)

# --- Styling ---
st.markdown(
    """
    <style>
        .subtext {
            font-size: 18px !important;
            text-align: left;
            color: #5A5A5A;
            margin-bottom: 80px;
        }
        .stButton>button {
            background-color: #3366CC !important;
            color: white !important;
            font-size: 16px;
            padding: 10px 15px;
            border-radius: 5px;
        }
        .result-box {
            font-size: 18px;
            color: #333333;
            background: #F8F8F8;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Main Title ---
st.markdown("<h1>📢 LinkedIn Post Generator</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Generate professional LinkedIn posts instantly</div>", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.header("🎯 Customize Your Post")

fs = FewShotPosts()
tags = fs.get_tags()

selected_tag = st.sidebar.selectbox("📝 Choose a Topic", options=tags)
selected_length = st.sidebar.selectbox("📄 Select Length", options=["Short", "Medium", "Long"])
selected_language = st.sidebar.selectbox("🌍 Select Language", options=["English", "Hinglish"])
need_image = st.sidebar.checkbox("🖼️ Need Image?")

# Generate Button
if st.sidebar.button("🚀 Generate Post"):
    with st.spinner("Generating your post... ⏳"):
        post = generate_post(selected_length, selected_language, selected_tag)

    # Display the Generated Post
    st.markdown(
        f"""
        <div class="result-box">
            <h4 style="color: #3366CC;">📜 Your Generated Post:</h4>
            <p>{post}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if need_image :
        image = generate_post_with_image(post=post,tag = selected_tag)

        if image:
            st.markdown(
            """
            <style>
                .image-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                .image-container img {
                    border-radius: 10px;
                    max-height: 400px;
                    width: auto;
                    object-fit: contain;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the image inside a div container
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image, caption="Generated Image", use_container_width=False)
        st.markdown("</div>", unsafe_allow_html=True)

