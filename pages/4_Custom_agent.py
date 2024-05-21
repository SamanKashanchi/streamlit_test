import os
import pandas as pd
import streamlit as st
import llama_index
from llama_index.llms.openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.readers.file import PDFReader
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage



# pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
# saman_pdf = PDFReader().load_data(file = pdf_path)
