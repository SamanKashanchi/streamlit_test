import streamlit as st
from PIL import Image
from datetime import datetime


def show_certifications():
    st.title("Certifications 📊")

    # Display the PNG certificate
    st.subheader("TestDome Python Certificate")
    st.image("TestDomePython.PNG", use_column_width=True)

    # Display the PDF certificate using an iframe
    st.subheader("HackerRank Problem Solving Certificate")
    pdf_file_path = "HackerRankCertificate.pdf"
    st.image("hackerrank.png", use_column_width=True)

show_certifications()

