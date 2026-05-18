import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import streamlit as st
import plotly.express as px
import pandas as pd

from backend.services.parser import extract_text
from backend.services.skill_extractor import extract_skills
from backend.services.ats import calculate_ats_score
from backend.services.predict import predict_role
from backend.services.skill_match import skill_match_percentage


# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="centered"
)

# Title
st.title("AI Resume Analyzer")

# Upload Resume
uploaded_file = st.file_uploader(
    label="Upload your resume (PDF or DOCX format)",
    type=["pdf", "docx"]
)

# Process Resume
if uploaded_file is not None:

    # Create uploads folder
    os.makedirs("uploads", exist_ok=True)

    # Save uploaded file
    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # Extract text from resume
    text = extract_text(save_path)

    # Show extracted text
    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        value=text,
        height=300
    )

    # Extract skills
    skills = extract_skills(text)

    st.subheader("Extracted Skills")

    if skills:

        # Show skills
        st.write(", ".join(skills))

        # Skill Visualization
        df = pd.DataFrame({
            "Skills": skills
        })

        fig = px.bar(
            df,
            x="Skills",
            title="Detected Skills"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.warning("No skills found in the resume.")

    # Job Description Section
    st.subheader("Job Description")

    job_desc = st.text_area(
        "Paste the job description here",
        height=200
    )

    # ATS Analysis
    if job_desc:

        # ATS Score
        ats_score = calculate_ats_score(
            text,
            job_desc
        )

        st.subheader("ATS Match Score")

        st.progress(min(int(ats_score), 100))

        st.write(f"ATS Score: {ats_score}%")

        # Predict Job Role
        role = predict_role(skills)

        st.subheader("Predicted Job Role")

        st.success(role)

        # Skill Match
        jd_skills = [
        skill.strip().lower()
        for skill in job_desc.split(",")
        ]

        match_score = skill_match_percentage(
            skills,
            jd_skills
        )

        st.subheader("Skill Match")

        st.metric(
            label="Skill Match %",
            value=f"{match_score}%"
        )