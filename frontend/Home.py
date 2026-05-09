import streamlit as st 

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    label="Upload your resume (PDF or DOCX format)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    