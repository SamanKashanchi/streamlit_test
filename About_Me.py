import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np

st.set_page_config(page_title="PORTFOLIO")


# Load your profile picture
profile_pic = 'profile.jpeg'  


st.sidebar.markdown(f"![Saman Kashanchi]({profile_pic})")


