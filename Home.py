import streamlit as st
import  yfinance as yf
import pandas as pd
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import warnings

from scipy.stats import shapiro
import statsmodels.api as sm
import numpy as np
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="PORTFOLIO", layout ='wide')
st.markdown(
    """
    <style>
    {% include 'styles.css' %}
    </style>
    """,
    unsafe_allow_html=True
)


# Load your profile picture
profile_pic = 'profile_pic.jpeg'  

st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

# Add a header for Projects
st.sidebar.markdown('## Projects')

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

python_lottie = load_lottieurl("https://lottie.host/9127127e-e4e5-494b-85a2-0aa303879534/KNejozHiWc.json")

sql_lottie = load_lottieurl('https://lottie.host/365ff170-3177-4554-be41-065a379a505e/gMAp1Y5Hk9.json')

docker_lottie = load_lottieurl("https://lottie.host/9ccbd771-096b-4cfc-9e7c-bec8a7afbaf2/Kl4y97DOt4.json")

# content2 = "From data to decisions: Unleashing the power of data science and predictive analytics to empower businesses"
content2 = '"The only way to do great work is to love what you do." - Steve Jobs'

# Call the "gradient" function to display a gradient title



with st.container():
    # Divide the container into two columns, with widths 8 and 3
    col1, col2 = st.columns([8, 3])

with col1:
    # Call the "gradient" function to display a gradient title
    gradient('#FF5733','#1B1464','e0fbfc',f"Saman Kashanchi", content2)
    
# Inside the second column (col2):
with col2:
    # Display a Lottie animation using the st_lottie function
    pass

st.write("---")  # Add an empty line



st.write('''Hey there,

I'm Saman Kashanchi, a data science enthusiast based in Los Angeles, CA, and I'm glad you found your way to my online portfolio.

With a background in Computational Data Science and Mathematics, I've been fortunate to work on a variety of real-world projects that have shaped my journey in this field. From optimizing supply chains to forecasting demand, I've had the opportunity to tackle some fascinating challenges head-on.

One of my recent professional projects involved developing a custom supply chain simulation at Jetro Restaurant Depot, utilizing reinforcement learning to optimize product ordering and reduce stockouts across the western region. Additionally, I led the development of a comprehensive invoice auditor system across multiple facilities, resulting in significant cost savings through error identification and process improvements.

Outside of my professional work, I'm always tinkering with personal projects that explore new ideas and technologies. For instance, I've developed a social media automation tool that manages over 30 channels with 2000+ subscribers, streamlining content creation and engagement across platforms.

I've also delved into the world of algorithmic trading, exploring arbitrage techniques in the foreign exchange markets. It's an ever-evolving landscape that combines my love for data with the excitement of financial markets.

Currently, I'm immersed in a personal project focused on database AI agents. These agents can visualize data, provide real-time insights, and automate workflows, offering a glimpse into the future of data-driven decision-making.

With a Master of Science in Computational Data Science and a Bachelor of Science in Computer Science from Chapman University, along with certificates in Applied Statistical Analysis and Bloomberg Certified, I'm equipped with the skills and knowledge to tackle complex challenges in the data science realm.

Thanks for taking the time to visit my portfolio. I invite you to explore further and learn more about my professional experiences, personal projects, skills, and expertise.''')
st.write()

resume_file = "Saman Kashanchi Resume 2024.pdf"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    
st.download_button( 
    label="📄 Download Resume",
    data= PDFbyte,
    file_name=resume_file,
    mime="application/octet-stream"
)

linkedin_url = "https://www.linkedin.com/in/saman-kashanchi/"

st.markdown(f"[LinkedIn Profile]({linkedin_url})", unsafe_allow_html=True)


with st.container():
    st.subheader('⚒️ Skills')
    st.write("---")
    col1, col2, col3= st.columns([1, 1, 1])
    with col1:

        st.markdown(
            "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
            "<p style='margin: 10px 0; font-size: 20px;'><strong>Languages</strong></p>"
            "<br>"
            "<div style='display: flex; justify-content: space-around;'>"
            
            "<div>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src= 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' alt='python' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>Python</p>"
            
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg' alt='c' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>C</p>"
            
            "</div>"
            "<div>"
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://cdn-icons-png.flaticon.com/128/4248/4248443.png' alt='sql' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>SQL</p>"

            
            f"<div style='display: flex; justify-content: center;'>"
            f"<img src='https://img.icons8.com/fluency/48/rstudio.png' alt='rstudio' style='width: 50px; height: 50px;'>"
            "</div>"
            "<p style='margin: 10px 0;'>R</p>"
            "</div>"
            "</div>"
            "</div>",
            unsafe_allow_html=True)

        st.markdown(
                "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
                "<p style='margin: 10px 0; font-size: 20px;'><strong>Modules</strong></p>"
                "<br>"
                "<div style='display: flex; justify-content: space-around;'>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg' alt='pandas' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Pandas</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg' alt='numpy' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Numpy</p>"
                "</div>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/iddpy6AFkF/idR-DMRMQW.svg' alt='SQLal' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>SQLAlchemy</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idUKrxFKe8/idwnJgWu7B.svg' alt='Jupyter' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Jupyter</p>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True)
        # st_lottie(python_lottie, height=90,width=90, key="python", speed=2.5)
        # st_lottie(sql_lottie, height=90,width=90, key="sql", speed=2.5)
    with col2:

        st.markdown(
                "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
                "<p style='margin: 10px 0; font-size: 20px;'><strong>DataBase Tools</strong></p>"
                "<br>"
                "<div style='display: flex; justify-content: space-around;'>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://img.icons8.com/color/48/amazon-web-services.png' alt='amazon-web-services' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>AWS</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://img.icons8.com/nolan/64/mongo-db.png' alt='mongo-db' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>MangoDB</p>"
                "</div>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idBdG8DdKe/idSEhEKy8_.svg' alt='MySQL' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Microsoft SQL Server</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://img.icons8.com/color/48/hadoop-distributed-file-system.png' alt='hadoop-distributed-file-system' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Apache Hadoop</p>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True
            )

        st.markdown(
                "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
                "<p style='margin: 10px 0; font-size: 20px;'><strong>Visualization Tools</strong></p>"
                "<br>"
                "<div style='display: flex; justify-content: space-around;'>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idiyFucwEQ/idMfeYD37H.svg' alt='streamlit' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>StreamLit</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idVCtIagXj/idHweJIV_u.svg' alt='PowerBI' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>PowerBI</p>"
                "</div>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idwPNp71Xw/id642wtAgP.jpeg' alt='Plotly' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Plotly</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idbyoKq4tZ/idvwpDn6Co.png' alt='mtplotlib' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Matplotlib</p>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True)

    
        # st_lottie(docker_lottie, height=90,width=90, key="docker", speed=2.5)
        # st.markdown('<img width="60" height="60" src="https://cwiki.apache.org/confluence/download/attachments/145723561/airflow_transparent.png" alt="power-bi"/>', unsafe_allow_html=True)
        # st.markdown("Apache AirFlow")


    with col3:



        st.markdown(
                "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
                "<p style='margin: 10px 0; font-size: 20px;'><strong>ML Tools</strong></p>"
                "<br>"
                "<div style='display: flex; justify-content: space-around;'>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/id6a4s3gXI/idncpUsO_z.jpeg' alt='LammaIidex' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>LlamaIndex</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idGqKHD5xE/idyUOkmwIu.svg' alt='huggingface' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>HuggingFace</p>"
                "</div>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg' alt='tensorflow' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>TensorFlow</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://icon.icepanel.io/Technology/svg/scikit-learn.svg' alt='Sklearn' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Scikit-learn</p>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True)


        st.markdown(
                "<div style='text-align: center; border: 1px solid #ccc; padding: 15px; border-radius: 20px; width: 375px; margin: 10px;'>"
                "<p style='margin: 10px 0; font-size: 20px;'><strong>Workflow Automation</strong></p>"
                "<br>"
                "<div style='display: flex; justify-content: space-around;'>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/id3uyOwT-S/idgLpsQVbx.jpeg' alt='Selenium' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Selenium</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg' alt='docker' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Docker</p>"
                "</div>"
                "<div>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://asset.brandfetch.io/idw382nG0m/idUCpm3axR.svg' alt='GitLab' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>GitLab</p>"
                f"<div style='display: flex; justify-content: center;'>"
                f"<img src='https://cwiki.apache.org/confluence/download/attachments/145723561/airflow_transparent.png?api=v2' alt='Apache AirFlow' style='width: 50px; height: 50px;'>"
                "</div>"
                "<p style='margin: 10px 0;'>Apache AirFlow</p>"
                "</div>"
                "</div>"
                "</div>",
                unsafe_allow_html=True)
             
        # st.markdown('<img width="60" height="60" src="https://img.icons8.com/color/48/amazon-web-services.png" alt="amazon-web-services"/>', unsafe_allow_html=True)
        # st.markdown('<div style="height: 55px;"></div>', unsafe_allow_html=True)  # Add vertical space

        # st.markdown('<img width="60" height="60" src="https://static-00.iconduck.com/assets.00/power-bi-icon-1536x2048-0xah5g2o.png" alt="power-bi"/>', unsafe_allow_html=True)
        # st.markdown("PowerBI")

        # st.markdown("</div>")

        # st.markdown('<img width="60" height="60" src="https://cdn-lfs.huggingface.co/repos/96/a2/96a2c8468c1546e660ac2609e49404b8588fcf5a748761fa72c154b2836b4c83/942cad1ccda905ac5a659dfd2d78b344fccfb84a8a3ac3721e08f488205638a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27hf-logo.svg%3B+filename%3D%22hf-logo.svg%22%3B&response-content-type=image%2Fsvg%2Bxml&Expires=1715636965&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcxNTYzNjk2NX19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy5odWdnaW5nZmFjZS5jby9yZXBvcy85Ni9hMi85NmEyYzg0NjhjMTU0NmU2NjBhYzI2MDllNDk0MDRiODU4OGZjZjVhNzQ4NzYxZmE3MmMxNTRiMjgzNmI0YzgzLzk0MmNhZDFjY2RhOTA1YWM1YTY1OWRmZDJkNzhiMzQ0ZmNjZmI4NGE4YTNhYzM3MjFlMDhmNDg4MjA1NjM4YTA%7EcmVzcG9uc2UtY29udGVudC1kaXNwb3NpdGlvbj0qJnJlc3BvbnNlLWNvbnRlbnQtdHlwZT0qIn1dfQ__&Signature=ZEl4ID--nH2qxecX5ADD71STYrL%7ENnF5CZ4qi3KvDQE1WpzHNRl3M9i0NBmAaKvfZx23gHODkNFLTp9wIcV7X-yvQWWN2NoZVyLDRfQPs42H6F4zbN1O6doXZUL8RQtP4We2YxuvxjCMCNcs8Ui3Glvn-9MN7RdIDV1WPVtHoKb6rHpauGHTFN7QK3uaNP4m0rZhOv5FjkkrIjhqQ3clbY0XU85aYRzUSPa3Yr9PyXji68%7Edv7SapXwZU9vk3GQOMaM5lHICY3aFRx8xaRfuPoVxyJ6VaWPDfLI-qXISYFKMsqGqDaxGW4EMwPlTIWn8gQArKSWUbpLIk9PkWyq%7EEg__&Key-Pair-Id=KVTP0A1DKRTAX"/>', unsafe_allow_html=True)
        # st.markdown("HuggingFace")
        
        # st.markdown('<img width="60" height="60" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="power-bi"/>', unsafe_allow_html=True)
        # st.markdown("scikit-learn")

