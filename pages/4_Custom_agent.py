import os
import pandas as pd
import streamlit as st
st.text("HI")
import streamlit as st

st.text(llama_index.__version__)



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

