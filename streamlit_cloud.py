import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile

st.write('Hello world! How are yous. Its time to tawek over the world')
s

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.video(uploaded_file)


    file_name = uploaded_file.name
    with open(file_name,"wb") as f:
        f.write(uploaded_file.getvalue())

    st.success(f"File {file_name} has been uploaded successfully")


    # Get user's desktop directory
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    # Move uploaded file to desktop
    desktop_file_path = os.path.join(desktop_dir, file_name)
    os.rename(file_name, desktop_file_path)

    st.info(f"File has been downloaded to your desktop.")
    