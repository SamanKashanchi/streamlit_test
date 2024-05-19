import os
import pandas as pd
from llama_index.llms import OpenAI

llm = OpenAI(model = "gpt-3.5-turbo-0613")

agent = ReActAgent.from_tools(tools, llm = llm, verbose = True, context = "SAY HELLO")

# from llama_index.query_engine import PandasQueryEngine
# # from prompts import context
# from llama_index.tools import QueryEngineTool, ToolMetadata
# from llama_index.agent import ReActAgent
# from llama_index.llms import OpenAI
# from pdf import saman_engine
