import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st 

from backend.services.parser import extract_text

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    label="Upload your resume (PDF or DOCX format)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    save_path = os.path.join("uploads", uploaded_file.name)
    
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")

    text=extract_text(save_path)
    st.text_area("Extracted Text", value=text, height=300)
    