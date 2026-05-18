def skill_match_percentage(
    resume_skills,
    jd_skills
):

    matched = set(
        resume_skills
    ).intersection(
        set(jd_skills)
    )

    percentage = (
        len(matched)
        /
        len(jd_skills)
    ) * 100

    return round(percentage, 2)