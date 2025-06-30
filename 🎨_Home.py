import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import warnings

import numpy as np
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# from llama_index.llms import OpenAI

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

profile_pic = 'profile_pic_circle.png'  

# st.sidebar.image(profile_pic, caption='Saman Kashanchi', use_column_width=True)

def gradient(color1, color2, color3, content1, content2):
    # Create an HTML structure with styling for a gradient header
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};font-family:Calibri;">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)


def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
            "github": "https://asset.brandfetch.io/idZAyF9rlg/idd6TtF-kc.png",
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)
    return icons_html

# Load a Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# content2 = "From data to decisions: Unleashing the power of data science and predictive analytics to empower businesses"
# content2 = 'The only way to do great work is to love what you do." - Steve Jobs'
content2 = 'DATA SCIENTIST & MACHINE LEARNING ENGINEER'
resume_file = "Saman Kashanchi Resume 2024.pdf"
linkedin_url = "https://www.linkedin.com/in/saman-kashanchi/"



with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
 



with st.container():
    left_column, middle_column, right_column = st.columns((1,0.2,0.6))
    with left_column:
        
        gradient('#FF5733','#1B1464','e0fbfc',f"Saman Kashanchi", content2)
        
        st.markdown("<br><br>", unsafe_allow_html=True)

        # st.subheader("DATA SCIENTIST & MACHINE LEARNING ENGINEER")
        st.subheader('''Welcome to my online portfolio, where you'll discover not only overviews of my projects but also interactive pages allowing you to experience them firsthand.''')

        st.markdown("<br>", unsafe_allow_html=True)

        st.download_button( 
        label="📄 Download Resume",
        data= PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream")
       
        st.markdown(social_icons(32, 32, LinkedIn="https://www.linkedin.com/in/saman-kashanchi/", 
                                         GitHub="https://github.com/SamanKashanchi"),
                                         unsafe_allow_html=True)

    with middle_column:
       
        st.empty()
    with right_column:
        
        image = st.image(profile_pic, width=350)
        st.write("_\"The only way to do great work is to love what you do.\"_ - Steve Jobs")
        

st.write("---")

st.subheader("About Me")

# st.markdown('<hr style="border-top: 2px solid red;">', unsafe_allow_html=True)

# - **Mathematics and Physics:** My passion for these subjects drives my approach to problem-solving and my career in data science.  
# - **Tech:** Enthusiastic about the latest technologies and innovations.  

st.markdown("""
From a childhood in Tehran to international studies in England, and now as a Data Scientist in the U.S., my journey has been fueled by curiosity and a passion for solving complex, real-world problems. Currently based in Los Angeles, I have a deep expertise in statistics, mathematics, and computer science, with experience applying machine learning and data analysis to create impactful solutions.

What sets me apart is my ability to see the bigger picture—transforming data into actionable insights that drive decision-making. I take pride in being not only technically skilled but also a strong communicator who can bridge technical and non-technical teams to create aligned, effective strategies.
""")




with st.container():
    st.header('⚒️ Skills', divider='red')
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

repo = {
    "RAWG": "https://github.com/Kimchi21/RAWG.io_Game-Data-Analysis",
    "AutoSales": "https://github.com/Kimchi21/Data-Analysis_Portfolio/tree/main/Automobile%20Sales",
    "SSD": "https://github.com/Kimchi21/Solid-State-Drives_Analysis",
    "Laz_Shopee": "https://github.com/Kimchi21/Lazada-vs.-Shopee_Sentiment-Analysis",
    "Sperm": "https://github.com/Kimchi21/Sperm-Morphological-Quality-ImageSegmentation",
    "Raisin": "https://github.com/Kimchi21/Raisin-Grain-Prediction-Using-a-StackedEnsembleModel"
}

st.header("Projects", divider='red')
right, left = st.columns(2)
with right:
    st.markdown(
        f"""
        <style>
            .repo-button {{
                background-color: #0067c3;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .repo-button:hover {{
                background-color: #0b35b6;
            }}
            .project-container {{
                display: flex;
                justify-content: center;
            }}
            .project-box {{
                text-align: center;
                border: 1px solid #ccc;
                padding: 40px;
                border-radius: 20px;
                width: 550px;
                margin: 10px;
            }}
            .project-img {{
                width: 475px;
                height: 275px;
            }}
        </style>
        <div class="project-container">
        <div class="project-box">
             <h4>Aristotle RAG Agent</h4>
            <img src="https://classicalwisdom.com/wp-content/uploads/2020/11/original-atlantic.jpg" alt="RAWG" class="project-img">
            <p style='margin: 15px 0 0 0;'>I created a RAG-based chatbot trained on Aristotle's works, allowing users to ask questions and explore moral dilemmas. 
            It uses Google Cloud for embedding storage and inference, and includes an API integrated with Streamlit for a seamless user experience.</p>
            <br>
            <a href="{repo['RAWG']}" project>
                <button class="repo-button">
                    <strong>Link to Repository</strong>
                </button>
            </a>
        </div>
        <!-- Add similar structure for other projects -->
        </div>
        <script>
            var buttons = document.querySelectorAll('.repo-button');
            buttons.forEach(function(button) {{
                button.addEventListener('mouseover', function() {{
                    button.style.backgroundColor = '#0b35b6';
                }});
                button.addEventListener('mouseout', function() {{
                    button.style.backgroundColor = '#0067c3';
                }});
            }});
        </script>
        """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <style>
            .repo-button {{
                background-color: #0067c3;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .repo-button:hover {{
                background-color: #0b35b6;
            }}
            .project-container {{
                display: flex;
                justify-content: center;
            }}
            .project-box {{
                text-align: center;
                border: 1px solid #ccc;
                padding: 40px;
                border-radius: 20px;
                width: 550px;
                margin: 10px;
            }}
            .project-img {{
                width: 475px;
                height: 275px;
            }}
        </style>
        <div class="project-container">
        <div class="project-box">
             <h4>Home Cash Flow Analyzer</h4>
            <img src="https://th.bing.com/th/id/R.ec01397906a56b80de12dd6b8b3a8eca?rik=uN0ZBKnEOhYWVg&riu=http%3a%2f%2fstatic1.squarespace.com%2fstatic%2f65566accc2f6cd400c787935%2f65566bf399dfea2786ab3a1a%2f655f55b3e3203141d1e5ee91%2f1701126089883%2fshutterstock_2121976568.jpg%3fformat%3d1500w&ehk=KdquSEOkJsekHOFw5%2bglDSeKbAQgJbdfk0Z145rQ33Y%3d&risl=&pid=ImgRaw&r=0" alt="RAWG" class="project-img">
            <p style='margin: 15px 0 0 0;'>I developed a web-based application designed to analyze the cash flow of rental investments. The app utilizes web scraping techniques to gather and aggregate data from various online sources. By inputting a LinkedIn profile link, the application scrapes relevant information including crime statistics, median rental prices for the neighborhood, state property tax rates, and property insurance estimates.</p>
            <br>
            <a href="{repo['RAWG']}" project>
                <button class="repo-button">
                    <strong>Link to Repository</strong>
                </button>
            </a>
        </div>
        <!-- Add similar structure for other projects -->
        </div>
        <script>
            var buttons = document.querySelectorAll('.repo-button');
            buttons.forEach(function(button) {{
                button.addEventListener('mouseover', function() {{
                    button.style.backgroundColor = '#0b35b6';
                }});
                button.addEventListener('mouseout', function() {{
                    button.style.backgroundColor = '#0067c3';
                }});
            }});
        </script>
        """, unsafe_allow_html=True)

with left:
    st.markdown(
        f"""
        <style>
            .repo-button {{
                background-color: #0067c3;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .repo-button:hover {{
                background-color: #0b35b6;
            }}
            .project-container {{
                display: flex;
                justify-content: center;
            }}
            .project-box {{
                text-align: center;
                border: 1px solid #ccc;
                padding: 40px;
                border-radius: 20px;
                width: 550px;
                margin: 10px;
            }}
            .project-img {{
                width: 475px;
                height: 275px;
            }}
        </style>
        <div class="project-container">
        <div class="project-box">
             <h4>Trading Algo Backtester / Optimizer</h4>
            <img src="https://th.bing.com/th/id/OIP.2MCe49Eg66vWtgwgh5COfgHaD7?rs=1&pid=ImgDetMain" alt="Lazada vs. Shopee" class="project-img">
            <p style='margin: 15px 0 0 0;'>Over the course of two years, I developed and executed a series of algorithmic trading strategies across forex and stock markets. The project involved implementing and refining arbitrage strategies, leveraging statistical analysis, machine learning techniques, and time series modeling. Key activities included backtesting strategies using historical data, optimizing algorithms for live execution, and continuously evaluating performance to adapt to market conditions.</p>
            <br>
            <a href="{repo['Laz_Shopee']}" project>
                <button class="repo-button">
                    <strong>Link to Repository</strong>
                </button>
            </a>
        </div>
        <!-- Add similar structure for other projects -->
        </div>
        <script>
            var buttons = document.querySelectorAll('.repo-button');
            buttons.forEach(function(button) {{
                button.addEventListener('mouseover', function() {{
                    button.style.backgroundColor = '#0b35b6';
                }});
                button.addEventListener('mouseout', function() {{
                    button.style.backgroundColor = '#0067c3';
                }});
            }});
        </script>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <style>
            .repo-button {{
                background-color: #0067c3;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .repo-button:hover {{
                background-color: #0b35b6;
            }}
            .project-container {{
                display: flex;
                justify-content: center;
            }}
            .project-box {{
                text-align: center;
                border: 1px solid #ccc;
                padding: 40px;
                border-radius: 20px;
                width: 550px;
                margin: 10px;
            }}
            .project-img {{
                width: 475px;
                height: 275px;
            }}
        </style>
        <div class="project-container">
        <div class="project-box">
             <h4>Social Media Automation Suite</h4>
            <img src="https://store.outrightcrm.com/wp-content/uploads/2021/06/topimage.png" alt="Lazada vs. Shopee" class="project-img">
            <p style='margin: 15px 0 0 0;'>The Social Media Automation Suite is a versatile tool for efficient social media management. Utilizing web scrapers, GPT for caption and description generation, and integrated with the Telegram API, this suite allows for mass content scraping, user-specified editing (compilations, split screens, text overlays), post scheduling, and YouTube posting. It streamlines content creation and management across platforms, enhancing your social media strategy.</p>
            <br>
            <a href="{repo['Laz_Shopee']}" project>
                <button class="repo-button">
                    <strong>Link to Repository</strong>
                </button>
            </a>
        </div>
        <!-- Add similar structure for other projects -->
        </div>
        <script>
            var buttons = document.querySelectorAll('.repo-button');
            buttons.forEach(function(button) {{
                button.addEventListener('mouseover', function() {{
                    button.style.backgroundColor = '#0b35b6';
                }});
                button.addEventListener('mouseout', function() {{
                    button.style.backgroundColor = '#0067c3';
                }});
            }});
        </script>
        """,
        unsafe_allow_html=True
    )


