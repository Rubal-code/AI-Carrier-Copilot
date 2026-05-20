def classify_resume(skills):

    skills = [s.lower().strip() for s in skills]

    # -----------------------------
    # AI / ML / Data Science
    # -----------------------------
    if (
        "python" in skills and
        (
            "machine learning" in skills or
            "deep learning" in skills or
            "tensorflow" in skills or
            "pytorch" in skills
        )
    ):
        return "AI / Machine Learning Engineer"

    elif (
        "python" in skills and
        (
            "pandas" in skills or
            "numpy" in skills or
            "data analysis" in skills or
            "sql" in skills
        )
    ):
        return "Data Scientist"

    elif (
        "power bi" in skills or
        "tableau" in skills or
        "excel" in skills
    ):
        return "Data Analyst"

    # -----------------------------
    # Web Development
    # -----------------------------
    elif (
        "javascript" in skills and
        (
            "react" in skills or
            "html" in skills or
            "css" in skills
        )
    ):
        return "Frontend Developer"

    elif (
        "node.js" in skills or
        "express.js" in skills or
        "mongodb" in skills
    ):
        return "MERN Stack Developer"

    elif (
        "java" in skills and
        (
            "spring" in skills or
            "spring boot" in skills or
            "hibernate" in skills
        )
    ):
        return "Backend Java Developer"

    elif (
        "php" in skills or
        "laravel" in skills
    ):
        return "PHP Developer"

    elif (
        "django" in skills or
        "flask" in skills or
        "fastapi" in skills
    ):
        return "Python Backend Developer"

    # -----------------------------
    # Mobile Development
    # -----------------------------
    elif (
        "flutter" in skills or
        "dart" in skills
    ):
        return "Flutter Developer"

    elif (
        "android" in skills or
        "kotlin" in skills
    ):
        return "Android Developer"

    elif (
        "swift" in skills or
        "ios" in skills
    ):
        return "iOS Developer"

    # -----------------------------
    # Cloud / DevOps
    # -----------------------------
    elif (
        "aws" in skills or
        "azure" in skills or
        "gcp" in skills
    ):
        return "Cloud Engineer"

    elif (
        "docker" in skills or
        "kubernetes" in skills or
        "jenkins" in skills
    ):
        return "DevOps Engineer"

    # -----------------------------
    # Cybersecurity
    # -----------------------------
    elif (
        "network security" in skills or
        "penetration testing" in skills or
        "ethical hacking" in skills
    ):
        return "Cybersecurity Analyst"

    # -----------------------------
    # UI/UX
    # -----------------------------
    elif (
        "figma" in skills or
        "adobe xd" in skills or
        "ui ux" in skills
    ):
        return "UI/UX Designer"

    # -----------------------------
    # Software Testing
    # -----------------------------
    elif (
        "selenium" in skills or
        "manual testing" in skills or
        "automation testing" in skills
    ):
        return "QA / Test Engineer"

    # -----------------------------
    # Blockchain
    # -----------------------------
    elif (
        "solidity" in skills or
        "web3" in skills or
        "ethereum" in skills
    ):
        return "Blockchain Developer"

    # -----------------------------
    # Game Development
    # -----------------------------
    elif (
        "unity" in skills or
        "unreal engine" in skills
    ):
        return "Game Developer"

    # -----------------------------
    # Embedded / IoT
    # -----------------------------
    elif (
        "arduino" in skills or
        "raspberry pi" in skills or
        "iot" in skills
    ):
        return "IoT Engineer"

    # -----------------------------
    # Non-Tech Roles
    # -----------------------------
    elif (
        "communication" in skills and
        "leadership" in skills
    ):
        return "HR / Management Professional"

    elif (
        "sales" in skills or
        "marketing" in skills or
        "digital marketing" in skills
    ):
        return "Marketing Specialist"

    elif (
        "accounting" in skills or
        "finance" in skills or
        "tally" in skills
    ):
        return "Finance / Accounts Professional"

    elif (
        "content writing" in skills or
        "copywriting" in skills
    ):
        return "Content Writer"

    elif (
        "trading" in skills or
        "stock market" in skills
    ):
        return "Trading Analyst"

    elif (
        "project management" in skills or
        "scrum" in skills
    ):
        return "Project Manager"

    # -----------------------------
    # Default
    # -----------------------------
    else:
        return "General Professional"