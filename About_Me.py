import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="PORTFOLIO", layout='wide')
st.markdown(
    """
    <style>
    {% include 'styles.css' %}
    </style>
    """,
    unsafe_allow_html=True
)


# Load your profile picture
profile_pic = 'profile_pic.jpeg'  

st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

# Add a header for Projects
st.sidebar.markdown('## Projects')

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

python_lottie = load_lottieurl("https://lottie.host/9127127e-e4e5-494b-85a2-0aa303879534/KNejozHiWc.json")

sql_lottie = load_lottieurl('https://lottie.host/365ff170-3177-4554-be41-065a379a505e/gMAp1Y5Hk9.json')

docker_lottie = load_lottieurl("https://lottie.host/9ccbd771-096b-4cfc-9e7c-bec8a7afbaf2/Kl4y97DOt4.json")

content2 = "From data to decisions: Unleashing the power of data science and predictive analytics to empower businesses"

# Call the "gradient" function to display a gradient title
gradient('#FF5733','#1B1464','e0fbfc',f"Saman Kashanchi", content2)
st.write("---")  # Add an empty line



st.write('Versatile and accomplished Data Scientist with a solid foundation in Computational Data Science and Mathematics, boasting a record of initiating and leading data-driven projects to successful completion. Proficient in leveraging advanced analytics, machine learning models, and data visualization techniques to drive strategic business decisions and operational efficiencies. Recognized for excellence in automation, demand forecasting, and research contributions')
st.write('/"The only way to do great work is to love what you do./" - Steve Jobs')

resume_file = "Saman Kashanchi Resume 2024.pdf"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
st.download_button( 
    label="📄 Download Resume",
    data= PDFbyte,
    file_name=resume_file,
    mime="application/octet-stream"
)

linkedin_url = "https://www.linkedin.com/in/saman-kashanchi/"

st.markdown(f"[LinkedIn Profile]({linkedin_url})", unsafe_allow_html=True)


with st.container():
    st.subheader('⚒️ Skills')
    st.write("---")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=90,width=90, key="python", speed=2.5)
        st_lottie(sql_lottie, height=90,width=90, key="sql", speed=2.5)
    with col2:
        st_lottie(docker_lottie, height=90,width=90, key="docker", speed=2.5)
        st.markdown('<img width="60" height="60" src="https://icon.icepanel.io/Technology/svg/Matplotlib.svg" alt="power-bi"/>', unsafe_allow_html=True)
        st.markdown("matplotlib")


    with col3:
        st.markdown('<img width="60" height="60" src="https://img.icons8.com/color/48/amazon-web-services.png" alt="amazon-web-services"/>', unsafe_allow_html=True)
        st.markdown('<div style="height: 55px;"></div>', unsafe_allow_html=True)  # Add vertical space

        st.markdown('<img width="60" height="60" src="https://img.icons8.com/color/48/power-bi.png" alt="power-bi"/>', unsafe_allow_html=True)
        
    with col4:
        st.markdown('<img width="60" height="60" src="https://cdn-lfs.huggingface.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/942cad1ccda905ac5a659dfd2d78b344fccfb84a8a3ac3721e08f488205638a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D%22hf-logo.svg%22%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1715635938&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcxNTYzNTkzOH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5odWdnaW5nZmFjZS5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzk0MmNhZDFjY2RhOTA1YWM1YTY1OWRmZDJkNzhiMzQ0ZmNjZmI4NGE4YTNhYzM3MjFlMDhmNDg4MjA1NjM4YTA%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=BK24DvmXtJPBdfBW%7ECjRRcfUgpPkNnkM3eElZq7yz3yw4cJOVkGNibLg3wbUQCltxGhj6X03uhj1cjQeBXorPrwOkiPfAgOeMnw3wdZXLdJmCI0RCfs7QPgwcac8K7eMy3R3aEY3O3Xhbp9%7ELtgyybjy3QdKJ18eRe9l9MGSWXrgo-lbN4PgSWViPYtgdKZC5KUr5uwAyqPzEcTifEYinSkvCmzDZ3n%7Eb-SmljtT8jfV--YLw9P23awsmU1zn7l8ATJfphe7im9rDp2SOFfawkC-mg9nbMwKhUaa2OVenoBt9-ylK4b02eBJQQjnLBi8JFddfMFtCzWG1%7Eqrpv-AtQ__&Key-Pair-Id=KVTP0A1DKRTAX" alt="power-bi"/>', unsafe_allow_html=True)
        st.markdown("HuggingFace")
