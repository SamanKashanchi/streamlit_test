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


# Load your profile picture
profile_pic = 'profile.jpeg'  

st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

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

mango_lottie = load_lottieurl("mangodb.jason")

content2 = "From data to decisions: Unleashing the power of data science and predictive analytics to empower businesses"

# Call the "gradient" function to display a gradient title
gradient('#FF5733','#1B1464','e0fbfc',f"Saman Kashanchi", content2)
st.write("---")  # Add an empty line



st.write('Versatile and accomplished Data Scientist with a solid foundation in Computational Data Science and Mathematics, boasting a record of initiating and leading data-driven projects to successful completion. Proficient in leveraging advanced analytics, machine learning models, and data visualization techniques to drive strategic business decisions and operational efficiencies. Recognized for excellence in automation, demand forecasting, and research contributions')
st.subheader('Skills')
st_lottie(python_lottie, height=90,width=90, key="python", speed=2.5)
st_lottie(sql_lottie, height=90,width=90, key="sql", speed=2.5)
st_lottie(docker_lottie, height=90,width=90, key="docker", speed=2.5)
st_lottie()