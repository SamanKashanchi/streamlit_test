import streamlit as st
from PIL import Image
from datetime import datetime
st.text("YOOOZ")
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
            "iframe_link": "https://www.hackerrank.com/certificates/iframe/e26e93338e02",
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
            if "details_link" in cert:
                st.markdown(f"[View Certificate]({cert['details_link']})")
            if "iframe_link" in cert:
                # Embed the iframe
                st.components.v1.iframe(cert["iframe_link"], height=500, scrolling=True)

if __name__ == "__main__":
    show_certifications()
