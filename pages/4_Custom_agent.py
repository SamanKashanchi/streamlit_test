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
        st.text("Building index: " + index_name)
        index = VectorStoreIndex.from_documents(data, show_progress = True)
        index.storage_context.persist(persist_dir = index_name)
    else:
        st.text("Index already exsists. Laoding Index")
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir = index_name)
        )
    return index


chatbot_lottie = load_lottieurl("https://lottie.host/ce2c1273-eca3-4ee4-bd54-ac10f2b7f7dd/gcZayDkN8E.json")

with st.container():
    col1, col2 = st.columns([8, 3])

with col1:
    # Call the "gradient" function to display a gradient title
    gradient('#FF5733','#1B1464','e0fbfc',f"My RAG Based Portfolio Assistent", 'This is a RAG agent with access to my past projects, experiences, passions, ambitions, and more. Feel free to ask anything!')   

with col2:

    st_lottie(chatbot_lottie, height=280, key="data")


tabs = ["Llama-Index OpenAI Portolio Agent", "LangChain Llama3 Chatbot"]
tab1, tab2 = st.tabs([t.center(9, "\u2001") for t in tabs])


secrets = toml.load('secrets.toml')
openai_api_key = secrets['secrets']['OPENAI_API_KEY']
st.text(f"Loaded API Key: {openai_api_key}")
    
# context = """Purpose: The primary role of this agent is to assist users by providing accurate 
#             information Saman, his experiences and his background. """


# pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
# saman_pdf = PDFReader().load_data(file = pdf_path)
# saman_index = get_index(saman_pdf, 'saman PDF')
# saman_engine = saman_index.as_query_engine()

    

# tools = [   
#         QueryEngineTool(query_engine = saman_engine, 
#                          metadata = ToolMetadata(name = "saman_pdfData",
#                                                 description = 'this gives detailed information about Saman'))]

# llm = OpenAI(model = "gpt-3.5-turbo-0613")
# agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = context)




# # if prompt:
# #     result = agent.query(prompt)
# #     with st.chat_message("assistant"):

# #         st.markdown(result)

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
        
# prompt = st.chat_input("Ask me any question about Saman and his background ", key='prompt_KEY')


# if prompt :    
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     with st.chat_message("user"):
#         st.markdown(prompt)


#     result = agent.query(prompt)  
    
#     with st.chat_message("assistant"):
#         st.markdown(result)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": result })

# with tab2:
    
#     llm = Ollama(
#         model="llama3"
#     )  # assuming you have Ollama installed and have llama3 model pulled with `ollama pull llama3 `
    
    
#     st.text((llm.invoke("Tell me a joke")))

