import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np

# st.set_page_config(page_title="PORTFOLIO")


# Load your profile picture
profile_pic = 'profile.jpeg'  

st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

st.write("Versatile and accomplished Data Scientist with a solid foundation in Computational Data Science and Mathematics, boasting a record of initiating and leading data-driven projects to successful completion. Proficient in leveraging advanced analytics, machine learning models, and data visualization techniques to drive strategic business decisions and operational efficiencies. Recognized for excellence in automation, demand forecasting, and research contributions..")



