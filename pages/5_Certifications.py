import streamlit as st
from PIL import Image
from datetime import datetime

def show_certifications():
    st.title("Certifications 📊")

    # Certificate details
    certifications = [
        {
            "title": "TestDome Python Certificate",
            "date": "September 2024",
            "image_file": "TestDomePython.PNG",  # Local file path
            "organization": "TestDome",
            "details_link": "https://www.testdome.com/certificates/fa5728523f994b2ea040e0d5cf8870f6"
        },
        {
            "title": "HackerRank Problem Solving Certificate",
            "date": "August 2023",
            "pdf_file": "HackerRankCertificate.pdf",  # Local PDF file path
            "organization": "HackerRank"
        }
    ]

    # Show number of results
    st.write(f"Showing {len(certifications)} certifications:")

    # Display certificate details
    for cert in certifications:
        c1, c2 = st.columns([1, 3.5])
        if "image_file" in cert:
            with c1:
                st.image(cert["image_file"], use_column_width=True, width=500)  # Adjust width to 500px
        with c2:
            st.markdown(f"""
                ### {cert['title']}
                - **Date:** {cert['date']}
                - **Organization:** {cert['organization']}
            """)
            st.image(cert["pdf_file"], use_column_width=True, width=500)  # Adjust width to 500px


# Option to upload a PDF for the HackerRank certificate
uploaded_file = st.file_uploader("Upload the HackerRank certificate as a PDF", type="pdf")
if uploaded_file is not None:
    with open("HackerRankCertificate.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("File uploaded successfully!")

st.text("YOOOZYYYY")
show_certifications()

