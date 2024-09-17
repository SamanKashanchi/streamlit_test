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
            "image_file": "TestDomePython.png",  # Local file path
            "organization": "TestDome",
            "details_link": "https://www.testdome.com/certificates/fa5728523f994b2ea040e0d5cf8870f6"
        }
    ]

    # Show number of results
    st.write(f"Showing {len(certifications)} certification:")

    # Display certificate details
    for cert in certifications:
        c1, c2 = st.columns([1, 3.5])
        with c1:
            st.image(cert["image_file"], use_column_width=True, width=300)  # Adjust width to 300px
        with c2:
            st.markdown(f"""
                ### {cert['title']}
                - **Date:** {cert['date']}
                - **Organization:** {cert['organization']}
            """)
            st.markdown(f"[View Certificate]({cert['details_link']})")


if __name__ == "__main__":
    show_certifications()
