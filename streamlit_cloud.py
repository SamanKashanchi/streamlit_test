import streamlit as st

st.write('Hello world! How are yous. Its time to tawek over the world')



def trim_video(input_file, duration=59):

    try:
        clip = VideoFileClip(input_file)
    except:
        st.text("FAILD AT READING THE VIDEO FROM TRIMING")

    if clip.duration > 59:
        st.text(clip.duration)
        st.text("Original duration.")
        st.text("MAKING TRIMED VID")
        st.text(input_file)
        st.text("^^^the fucken input file")
        New_input_file = input_file[:-4] + "_" + '.mp4'
        clip = clip.subclip(0, duration)
        clip.write_videofile(New_input_file, codec="libx264", audio_codec="aac")
        clip.close()
        os.remove(input_file)
    else:
        pass
uploaded_file = st.file_uploader("Choose a file")

 