import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile
import base64
import uuid

st.write('Hello world! How are yous. Its time to tawek over the world')

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])



def get_binary_file_downloader_html(file_path, file_label, button_text="Download"):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    button_uuid = str(uuid.uuid4()).replace("-", "")
    button_id = f"button_{button_uuid}"
    button_html = f'<button id="{button_id}" type="button">{button_text}</button>'
    js_download = (
        f'var ele = document.getElementById("{button_id}");ele.download = "{file_label}";'
        f'var blob = new Blob(["{b64}"], {{type: "video/mp4"}});'
        f'ele.href = window.URL.createObjectURL(blob);'
    )
    js_click = f'var ele = document.getElementById("{button_id}");ele.click();'
    return f'<script>{js_download}{js_click}</script>'


if uploaded_file is not None:
    st.video(uploaded_file)


    file_content = uploaded_file.getvalue()
    file_name = uploaded_file.name
      
   


    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(file_content)

        st.markdown(get_binary_file_downloader_html(temp_file.name, file_name, button_text="Click to Download"), unsafe_allow_html=True)




    # # Get user's desktop directory
    # desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    # # Move uploaded file to desktop
    # desktop_file_path = os.path.join(desktop_dir, file_name)

    # st.text(desktop_file_path)

    # os.rename(file_name, desktop_file_path)

    # st.info(f"File has been downloaded to your desktop.")
    