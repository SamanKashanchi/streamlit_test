import os
import pandas as pd
import streamlit as st
import llama_index
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.readers.file import PDFReader
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage

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

openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key


if not openai_api_key:
    st.text("No OPENAI_API_KEY found in environment variables")

pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
saman_pdf = PDFReader().load_data(file = pdf_path)
saman_index = get_index(saman_pdf, 'saman')
