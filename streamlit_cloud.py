import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile
import base64
import uuid

st.write('Hello world! How are yous. Its time to tawek over the world')

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])


   
def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'data:video/mp4;base64,{b64}'
    return f'<a href="{href}" download="{file_label}">Download Chunk</a>'


def split_video_into_chunks(video_path, chunk_duration=20):
    clip = VideoFileClip(video_path)
    total_duration = clip.duration
    chunks = []
    for i in range(0, int(total_duration), chunk_duration):
        start_time = i
        end_time = min(i + chunk_duration, total_duration)
        chunk = clip.subclip(start_time, end_time)
        chunks.append(chunk)
    return chunks


if uploaded_file is not None:
    st.video(uploaded_file)

    if st.button("Split Video into Chunks"):


        file_content = uploaded_file.getvalue()
          

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(file_content)
            file_name = uploaded_file.name
            temp_file_path = temp_file.name

            # st.markdown(get_binary_file_downloader_html(temp_file.name, file_name), unsafe_allow_html=True)


            # Split the video into chunks
            video_chunks = split_video_into_chunks(temp_file_path)

            # Provide download links for each chunk
            for i, chunk in enumerate(video_chunks):
                chunk_file_path = f"{temp_file_path}_chunk_{i}.mp4"
                chunk.write_videofile(chunk_file_path, codec="libx264", fps=24, audio_codec="aac")
                st.markdown(get_binary_file_downloader_html(chunk_file_path, f"{file_name}_chunk_{i}.mp4"), unsafe_allow_html=True)



    # # Get user's desktop directory
    # desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    # # Move uploaded file to desktop
    # desktop_file_path = os.path.join(desktop_dir, file_name)

    # st.text(desktop_file_path)

    # os.rename(file_name, desktop_file_path)

    # st.info(f"File has been downloaded to your desktop.")
    