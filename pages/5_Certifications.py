import streamlit as st
from PIL import Image
from datetime import datetime


def show_certifications():
    st.title("Certifications 📊")

    # Display the PNG certificate
    st.subheader("TestDome Python Certificate")
    st.image("TestDomePython.PNG", width=400)

    # Display the PDF certificate using an iframe
    st.subheader("HackerRank Problem Solving Certificate")
    pdf_file_path = "HackerRankCertificate.pdf"
    st.image("hackerrank.png", width=400)

show_certifications()

