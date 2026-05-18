def skill_match_percentage(resume_skills, jd_skills):

    # Convert to lowercase sets
    resume_set = set(
        skill.lower().strip()
        for skill in resume_skills
    )

    jd_set = set(
        skill.lower().strip()
        for skill in jd_skills
    )

    # Avoid division by zero
    if len(jd_set) == 0:
        return 0

    # Find matching skills
    matched_skills = resume_set.intersection(jd_set)

    # Calculate percentage
    percentage = (
        len(matched_skills) / len(jd_set)
    ) * 100

    return round(percentage, 2)