
import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Happy Valentine's Day",
    page_icon="❤️",
    layout="centered"
)

# Use absolute path to ensure robustness
current_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(current_dir, 'background.png.jpeg')

# Function to encode local image to base64
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# Attempt to load local background
local_bg_b64 = get_base64_of_bin_file(background_path)

if local_bg_b64:
    background_css = f'''
    background-image: url("data:image/png;base64,{local_bg_b64}");
    '''
else:
    # If file missing, show clear error
    st.error(f"⚠️ **Background Image Not Found!**")
    st.warning(f"Please save your image as `background.png.jpeg` in: `{current_dir}`")
    background_css = 'background-color: #ffe4e1;' # Fallback color

# YOUR MESSAGE
YOUR_PARAGRAPH = """
My babygurlll , happy valentines day i still miss and feel your hug your touch your close presence and that serene experience of being with you it was really heavenly with you my babygurll iloveyou the mostt and i still want to ask you that , will you be my valentine ??🥺🧿

Because you are the most beautiful soul and the most prettiest, cutest and the most coolest babygurll i can ever imagine of( bhumi be like - esahi hai humara laadle 😌)

Happy Valentine’s Day my love , iloveyou the most and i adore you the most and I’m blessed to have you my love🥺🫂🧿❤️
"""

# Custom CSS
st.markdown(f"""
<style>
    /* Background Image */
    .stApp {{
        {background_css}
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* Overlay Card - DARK GLASS for White Text */
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.4); 
        padding: 3rem 2.5rem;
        border-radius: 25px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        margin-top: 30px;
        max-width: 750px;
        text-align: center;
    }}

    /* Header Styling */
    h1 {{
        font-family: 'Great Vibes', cursive;
        color: #ffffff; /* White Text */
        font-weight: 400;
        font-size: 3.5rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        line-height: 1.2;
    }}
    
    /* Paragraph Text Styling */
    .valentine-text {{
        font-family: 'Georgia', serif;
        font-size: 1.3rem; 
        line-height: 1.8;
        color: #ffffff; /* White Text */
        margin-bottom: 30px;
        white-space: pre-wrap;
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8); /* Shadow for readability */
        font-weight: 500;
    }}
    
    /* Decorative Elements */
    .heart-decoration {{
        font-size: 2.5rem;
        color: #d81b60;
        margin-top: 20px;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.1); }}
        100% {{ transform: scale(1); }}
    }}

    /* Hide standard elements */
    header, footer {{visibility: hidden;}}
    
    /* YES Button Styling */
    .stButton > button {{
        background-color: #d81b60;
        color: white !important;
        border: none;
        border-radius: 50px;
        padding: 1rem 3rem;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(216, 27, 96, 0.4);
        transition: all 0.3s ease;
        margin-top: 1rem;
    }}
    
    .stButton > button:hover {{
        background-color: #ad1457;
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(216, 27, 96, 0.6);
    }}
    
</style>

<!-- Import Google Font for Header -->
<link href="https://fonts.googleapis.com/css2?family=Great Vibes&display=swap" rel="stylesheet">

""", unsafe_allow_html=True)

# Content
st.markdown("<h1>Happy Valentine's Day My Love ❤️</h1>", unsafe_allow_html=True)

st.markdown(f"""
<div class="valentine-text">
{YOUR_PARAGRAPH}
</div>
""", unsafe_allow_html=True)


# Interactive YES Button
if st.button("YES, I will be your Valentine! 💍"):
    st.balloons()
    st.snow()
    st.markdown("""
    <div style="
        font-size: 2rem; 
        color: #ffffff; 
        font-weight: bold; 
        margin-top: 20px; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        animation: fadeIn 2s;
    ">
    Yay! Forever & Always! ❤️❤️❤️
    </div>
    """, unsafe_allow_html=True)
