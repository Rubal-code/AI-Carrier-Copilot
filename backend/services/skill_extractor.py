skills_db = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "fastapi",
    "streamlit",
    "react",
    "docker"
]
def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)
    return found_skills