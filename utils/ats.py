def calculate_ats_score(resume_text):

    score = 0

    resume_text = resume_text.lower()

    # Important resume sections
    sections = [
        "education",
        "experience",
        "skills",
        "projects",
        "certifications"
    ]

    for section in sections:
        if section in resume_text:
            score += 10

    # Technical keywords
    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "data analysis",
        "tensorflow",
        "git",
        "github"
    ]

    keyword_count = 0

    for keyword in keywords:
        if keyword in resume_text:
            keyword_count += 1

    score += keyword_count * 5

    # Limit score
    if score > 100:
        score = 100

    return score