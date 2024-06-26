
import streamlit as st
import requests
from streamlit_lottie import st_lottie


def gradient(color1, color2, color3, content1, content2):
    # Create an HTML structure with styling for a gradient header
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};font-family:Calibri;">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)

# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Load your profile picture
profile_pic = 'profile_pic.jpeg'  
research_lottie = load_lottieurl("https://lottie.host/e8315d73-10a2-49cb-ace5-6583616ce5bd/KGlhVphyDL.json")

# st.sidebar.image(profile_pic, caption='Your Name', use_column_width=True)
st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)


# with st.container():
#     # Divide the container into two columns, with widths 8 and 3
#     col1, col2 = st.columns([8, 3])

# with col1:
#     # Call the "gradient" function to display a gradient title
gradient('#FF5733','#1B1464','e0fbfc',f"Chapman Machine Learning Research", 'Custom generative models tailored for the Optical Engineering department, specializing in the design of nanoscale surfaces.')   
# with col2:

#     st_lottie(research_lottie, height=280, key="data")
# Inside the second column (col2):
st.subheader('Research')

reserch_pic = 'research.jpg'  

st.image(reserch_pic, caption='Reserch Board', use_column_width=True)
