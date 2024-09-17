import streamlit as st
import streamlit.components.v1 as components

certificate_url = "https://www.testdome.com/certificates/fa5728523f994b2ea040e0d5cf8870f6"
components.iframe(certificate_url, height=600)
st.markdown("[View my certificate](https://www.testdome.com/certificates/fa5728523f994b2ea040e0d5cf8870f6)")
