
import streamlit as st



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


# Load your profile picture
profile_pic = 'profile_pic.jpeg'  

# st.sidebar.image(profile_pic, caption='Your Name', use_column_width=True)
st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)


with st.container():
    # Divide the container into two columns, with widths 8 and 3
    col1, col2 = st.columns([8, 3])

with col1:
    # Call the "gradient" function to display a gradient title
    gradient('#FF5733','#1B1464','e0fbfc',f"Research", 'Algorithmic trading is the practice of executing trades using computer programs grounded in strategies that typically rely on statistical methods for decision-making.')    
# Inside the second column (col2):
st.subheader('Research')

reserch_pic = 'research.jpg'  

st.image(reserch_pic, caption='Reserch Board', use_column_width=True)
