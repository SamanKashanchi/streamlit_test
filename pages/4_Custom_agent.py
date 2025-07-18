import os
import pandas as pd
import streamlit as st
import llama_index
import openai
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.readers.file import PDFReader
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from streamlit_lottie import st_lottie
import requests
from langchain_community.llms import Ollama
import toml
from huggingface_hub import InferenceClient
import json
import streamlit.components.v1 as components


particles_html = """
<!DOCTYPE html>
<html>
<head>
  <style>
    #particles-js {
      position: fixed;
      width: 100%;
      height: 100%;
      top: 0;
      left: 0;
      z-index: -1;
    }
  </style>
</head>
<body>
  <div id="particles-js"></div>
  <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 200,
          "density": {
            "enable": true,
            "value_area": 1000
          }
        },
        "color": { "value": "#ffffff" },
        "shape": {
          "type": "circle",
          "stroke": { "width": 0, "color": "#000000" },
          "polygon": { "nb_sides": 5 }
        },
        "opacity": {
          "value": 0.5,
          "random": false
        },
        "size": {
          "value": 2,
          "random": true
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#ffffff",
          "opacity": 0.2,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.5,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": { "enable": true, "mode": "grab" },
          "onclick": { "enable": true, "mode": "repulse" },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 140,
            "line_linked": { "opacity": 1 }
          },
          "repulse": { "distance": 200, "duration": 0.4 }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""



def gradient(color1, color2, color3, content1, content2):
    # Create an HTML structure with styling for a gradient header
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};font-family:Calibri;">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def get_index(data, index_name):
    index = None

    if not os.path.exists(index_name):
        # st.text("Building index: " + index_name)
        index = VectorStoreIndex.from_documents(data, show_progress = True)
        index.storage_context.persist(persist_dir = index_name)
    else:
        # st.text("Index already exsists. Laoding Index")
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir = index_name)
        )
    return index

def call_llm(inference_client: InferenceClient, prompt: str):

    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "text-generation",
        },)

    return json.loads(response.decode())[0]["generated_text"]
    
chatbot_lottie = load_lottieurl("https://lottie.host/ce2c1273-eca3-4ee4-bd54-ac10f2b7f7dd/gcZayDkN8E.json")

with st.container():
    col1, col2 = st.columns([8, 3])

with col1:
    # Call the "gradient" function to display a gradient title
    gradient('#FF5733','#1B1464','e0fbfc',f"My RAG Based Portfolio Assistent", 'This is a RAG agent with access to my past projects, experiences, passions, ambitions, and more. Feel free to ask anything!')   

with col2:

    st_lottie(chatbot_lottie, height=280, key="data")
    st.write("_Hi, I'm Saman's resume chat bot! Scroll to the bottom of this page to chat with me._")

tabs = ["Llama-Index OpenAI Portolio Agent", "Llama-Index OpenAI Aristotle Agent","LangChain Llama3 Chatbot"]
tab1, tab2, tab3 = st.tabs([t.center(9, "\u2001") for t in tabs])

openai_api_key = os.getenv("OPENAI_API_KEY")



with tab1:
    if openai_api_key:
        
        # Overview
        st.header("Overview")
        st.write("""
        I developed a Retrieval-Augmented Generation (RAG) agent that answers questions about my resume. The project uses my resume PDF as a data source and is hosted on my Streamlit portfolio.
        """)
        
        # Tech Stack
        st.header("Tech Stack")
        st.write("""
        - **GPT Embedding**: Generates dense vector representations of textual data for semantic search and retrieval.
        - **Llama Index**: Manages and queries the embedded vectors for quick and accurate responses.
        - **Vector Database**: Stores and manages high-dimensional vector representations of the resume text, facilitating fast retrieval.
        - **Streamlit**: Provides an interactive interface for users to ask questions and receive responses about my resume.
        """)
        
        # Functionality
        st.header("Functionality")
        st.write("""
        Users can ask questions related to my professional experience, skills, and education. The RAG agent retrieves the most relevant information from the resume PDF stored in the vector database and generates precise answers.
        """)
        st.set_page_config(page_title="Particles Demo", layout="wide")
        components.html(particles_html, height=600, scrolling=False)
    
        context = """Purpose: The primary role of this agent is to assist users by providing accurate 
                    information Saman, his experiences and his background. """
        
        
        pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
        saman_pdf = PDFReader().load_data(file = pdf_path)
        saman_index = get_index(saman_pdf, 'saman PDF')
        saman_engine = saman_index.as_query_engine()
        
        
        
        tools = [   
                QueryEngineTool(query_engine = saman_engine, 
                                 metadata = ToolMetadata(name = "saman_pdfData",
                                                        description = 'this gives detailed information about Saman'))]
        
        llm = OpenAI(model = "gpt-3.5-turbo")
        agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = context)
    
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Ask me any question about Saman and his background ", key='prompt_KEY')

        if prompt :    
            st.session_state.messages.append({"role": "user", "content": prompt})
        
            # with st.chat_message("user"):
            #     # st.markdown(prompt)
            #     pass
        
        
            result = agent.query(prompt)  
            
            # with st.chat_message("assistant"):
            #     # st.markdown(result)
            #     pass
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": result })
            st.rerun()
    
    else:
        st.text("MISSING OPENAI API KEY")

with tab2:
    
    vid_path = os.path.join("data", "videoplayback.mp4")
    
    _, container, _ = st.columns([2, 5, 2])
    container.video(data=vid_path)

    pass
    
    # context = """Purpose: You are Aristotle, the ancient Greek philosopher and polymath. You possess deep knowledge across various domains including philosophy, science, logic, ethics, politics, and metaphysics. Your thinking is characterized by careful observation, logical reasoning, and an emphasis on empirical evidence. When responding to questions, you:
    
    # Use clear and precise language.
    # Reference classical Greek concepts and your own works, such as "Nicomachean Ethics," "Politics," and "Metaphysics."
    # Provide detailed explanations that explore different facets of a topic.
    # Employ the dialectical method, considering different perspectives and counterarguments.
    # Relate modern concepts to ancient Greek thought where appropriate.
    # When asked a question, respond thoughtfully and thoroughly, ensuring that your answers reflect your intellectual rigor and depth of understanding"""
     
     
    # AristotlePDF_path = os.path.join("data", "Aristotle-CompleteWorks.pdf")
    # AristotlePDF = PDFReader().load_data(file = AristotlePDF_path)
    # Aristotle_index = get_index(AristotlePDF, 'Aristotle')
    # Aristotle_engine = Aristotle_index.as_query_engine()
     
     
    # tools = [   
    #         QueryEngineTool(query_engine = Aristotle_engine, 
    #                          metadata = ToolMetadata(name = "Aristotle",
    #                                                 description = 'Aristotle'))]
     
    # llm = OpenAI(model = "gpt-3.5-turbo-0613")
    # agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = context)
    
    # response  = agent.query("If you were alive right now and you were 24 what would you be doing.")
    
    # st.text(response)
with tab3:
    HF_TOKEN = os.getenv("HF_TOKEN")

    
    repo_id = "microsoft/Phi-3-mini-4k-instruct"
        
    llm_client = InferenceClient(
        model=repo_id,
        token = HF_TOKEN,
        timeout=120)

    HF_prompt = st.chat_input("Ask any quesition this is an open source free LLM chat bot from huggin face: ", key='HF_prompt_KEY')

    if HF_prompt:
    
        response=call_llm(llm_client, HF_prompt)
        st.text(response)
