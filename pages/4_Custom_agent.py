import os
import pandas as pd
import streamlit as st
import llama_index
from llama_index.llms.openai import OpenAI
from llama_index.agent import ReActAgent


import subprocess
st.text("HI")

st.text(llama_index)

# Define the pip command you want to run
pip_command = ["pip", "show", "llama_index"]

# Run the pip command
result = subprocess.run(pip_command, capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the output of the pip command
    st.text(result.stdout)
else:
    # Print an error message if the command failed
    st.text(result.stderr)


try:
    import llama_index
    st.write("llama_index is installed.")
    st.write("Modules in llama_index:")
    st.write(dir(llama_index))

    try:
        from llama_index import llms
        st.write("\nModules in llama_index.llms:")
        st.write(dir(llms))
    except ImportError as e:
        st.write("\nError importing llms:", e)

    try:
        from llama_index import readers
        st.write("\nModules in llama_index.readers:")
        st.write(dir(readers))
    except ImportError as e:
        st.write("\nError importing readers:", e)

    # Check individual submodules in llms and readers
    try:
        st.write("\nSubmodules in llama_index.llms:")
        for submodule in dir(llms):
            st.write(f"llms.{submodule}: {getattr(llms, submodule)}")
    except Exception as e:
        st.write("\nError listing submodules in llms:", e)

    try:
        st.write("\nSubmodules in llama_index.readers:")
        for submodule in dir(readers):
            st.write(f"readers.{submodule}: {getattr(readers, submodule)}")
    except Exception as e:
        st.write("\nError listing submodules in readers:", e)

except ImportError as e:
    st.write("llama_index is not installed:", e)

