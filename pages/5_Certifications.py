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
        ,
        {
            "title": "AWS Certified Solutions Architect",
            "date": "August 2023",
            "image_file": "AWSCertification.PNG",  # Local file path
            "organization": "Amazon Web Services",
            "details_link": "https://aws.amazon.com/certification/certified-solutions-architect-associate/"
        }
    ]

    # Show number of results
    st.write(f"Showing {len(certifications)} certification:")

    # Display certificate details
    for cert in certifications:
        c1, c2 = st.columns([1, 3.5])
        with c1:
            st.image(cert["image_file"], use_column_width=True, width=500)  # Adjust width to 300px
        with c2:
            st.markdown(f"""
                ### {cert['title']}
                - **Date:** {cert['date']}
                - **Organization:** {cert['organization']}
            """)
            st.markdown(f"[View Certificate]({cert['details_link']})")


if __name__ == "__main__":
    show_certifications()
