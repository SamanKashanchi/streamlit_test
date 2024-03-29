import streamlit as st
from moviepy.editor import VideoFileClip
import os

st.write('Hello world! How are yous. Its time to tawek over the world')


# uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

# if uploaded_file is not None:
#     st.video(uploaded_file)

def split_video_into_minutes(video_path):
    # Load the video clip
    clip = VideoFileClip(video_path)
    duration = clip.duration
    # Split the video into minute-long segments
    minute_segments = []
    for i in range(0, int(duration // 20)):
        start_time = i * 20
        end_time = min((i + 1) * 20, duration)
        segment = clip.subclip(start_time, end_time)
        minute_segments.append(segment)
    return minute_segments

def main():
    st.title("Video Uploader and Splitter App")
    
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    
    if uploaded_file is not None:
        st.video(uploaded_file)
        if st.button("Split Video and Save to Desktop"):
            # Create a temporary directory to store the video segments
            temp_dir = st._get_report_ctx().session_id
            os.makedirs(temp_dir, exist_ok=True)
            video_path = os.path.join(temp_dir, uploaded_file.name)
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Split the video into minute-long segments
            segments = split_video_into_minutes(video_path)
            
            # Save each segment to the user's desktop
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            for i, segment in enumerate(segments):
                segment_name = f"{os.path.splitext(uploaded_file.name)[0]}_{i}.mp4"
                segment_path = os.path.join(desktop_path, segment_name)
                segment.write_videofile(segment_path)
            
            st.success("Video split and saved to desktop successfully!")
            
if __name__ == "__main__":
    main()
