import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile

st.write('Hello world! How are yous. Its time to tawek over the world')

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    st.video(uploaded_file)
    

    file_content = uploaded_file.getvalue()
    file_name = uploaded_file.name
      
   


    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(file_content)


    # # Get user's desktop directory
    # desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    # # Move uploaded file to desktop
    # desktop_file_path = os.path.join(desktop_dir, file_name)

    # st.text(desktop_file_path)

    # os.rename(file_name, desktop_file_path)

    # st.info(f"File has been downloaded to your desktop.")
    