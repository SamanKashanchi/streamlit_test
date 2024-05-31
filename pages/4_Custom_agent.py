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



# Ask user to enter OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API Key", type='password',help="https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key", key='API_KEY')

# Create a button for the user to submit their API key
if st.button('Submit'):
    # Set the OpenAI API key as an environment variable
    # Set the OpenAI API key directly
    openai.api_key = openai_api_key
    
    # Check if the API key is valid by making a simple API call
    os.environ["OPENAI_API_KEY"] = openai_api_key


def get_index(data, index_name):
    index = None

    if not os.path.exists(index_name):
        print("Building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress = True)
        index.storage_context.persist(persist_dir = index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir = index_name)
        )
    return index



context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information Saman, his experiences and his background. """


pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
saman_pdf = PDFReader().load_data(file = pdf_path)
saman_index = get_index(saman_pdf, 'saman')
saman_engine = saman_index.as_query_engine()


tools = [   
        QueryEngineTool(query_engine = saman_engine, 
                         metadata = ToolMetadata(name = "saman_pdfData",
                                                description = 'this gives detailed information about Saman'))]

llm = OpenAI(model = "gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = context)


prompt = st.text_input("Ask me any question about Saman and his background ", key='prompt_KEY')

if prompt != "":
    result = agent.query(prompt)
    with st.chat_message("assistant"):

        st.markdown(result)

