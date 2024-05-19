import os
import pandas as pd
import streamlit as st
st.text("HI")
try:
    import llama_index
    st.write("llama_index is installed.")
    st.write("Modules in llama_index:")
    st.write(dir(llama_index))

    try:
        from llama_index import query_engine
        st.write("\nModules in llama_index.query_engine:")
        st.write(dir(query_engine))
    except ImportError as e:
        st.write("\nError importing query_engine:", e)

    try:
        from llama_index import readers
        st.write("\nModules in llama_index.readers:")
        st.write(dir(readers))
    except ImportError as e:
        st.write("\nError importing readers:", e)

    # Repeat for other submodules you are interested in
except ImportError as e:
    st.write("llama_index is not installed:", e)

