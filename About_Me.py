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

st.markdown(
    "<div style='display: flex; flex-direction: column;'>"
    
    "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 100%;'>"
    "<p style='margin: 10px 0; font-size: 20px;'><strong>Languages</strong></p>"
    "<div style='display: flex; flex-wrap: wrap; justify-content: space-around;'>"
    "<div style='margin: 5px; flex-basis: 25%; display: flex; justify-content: space-around;'>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' alt='python' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>Python</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn-icons-png.flaticon.com/128/4248/4248443.png' alt='sql' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>SQL</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg' alt='c' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>C</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg' alt='html' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>HTML</p>"
    "</div>"
    "</div>"
    "</div>"
    "</div>"
    
    "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 100%; margin-top: 20px;'>"
    "<p style='margin: 10px 0; font-size: 20px;'><strong>Libraries & Frameworks</strong></p>"
    "<div style='display: flex; flex-wrap: wrap; justify-content: space-around;'>"
    "<div style='margin: 5px; flex-basis: 25%; display: flex; justify-content: space-around;'>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg' alt='pandas' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>Pandas</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg' alt='numpy' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>NumPy</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://icon.icepanel.io/Technology/svg/Matplotlib.svg' alt='matplot' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>matplotlib</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://user-images.githubusercontent.com/315810/92161415-9e357100-edfe-11ea-917d-f9e33fd60741.png' alt='seaborn' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>seaborn</p>"
    "</div>"
    "</div>"
    "</div>"
    "</div>"
    
    "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 100%; margin-top: 20px;'>"
    "<p style='margin: 10px 0; font-size: 20px;'><strong>Development Tools & Applications</strong></p>"
    "<div style='display: flex; flex-wrap: wrap; justify-content: space-around;'>"
    "<div style='margin: 5px; flex-basis: 25%; display: flex; justify-content: space-around;'>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg' alt='mysql' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>MySQL</p>"
    "</div>"
    "<div style='display: flex; flex-direction: column;'>"
    "<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg' alt='postgresql' style='width: 50px; height: 50px;'>"
    "<p style='margin: 5px 0;'>PostgreSQL</p>"
    "</div>"
    "</div>"
    "</div>"
    "</div>"
    
    "</div>", unsafe_allow_html=True
)




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
