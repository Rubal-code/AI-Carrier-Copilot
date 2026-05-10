import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st 
from backend.services.parser import extract_text
from backend.services.skill_extractor import extract_skills
from backend.services.ats import calculate_ats_score
from backend.services.predict import predict_role

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

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

    skills = extract_skills(text)
    st.subheader("Extracted Skills")
    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills found in the resume.")
    
    # job description section
    st.subheader("Job Description")
    job_desc = st.text_area("Paste the job description here", height=200)
    if job_desc:

        ats_score = calculate_ats_score(text, job_desc)

        st.subheader("ATS Match Score")

        st.progress(int(ats_score))

        st.write(f"ATS Score: {ats_score}%")

        role=predict_role(skills)
        st.subheader("Predicted Job Role")
        st.success(role)