import streamlit as st
# from moviepy.editor import VideoFileClip
import os

st.write('Hello world! How are yous. Its time to tawek over the world')


uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.video(uploaded_file)
