def analyze_role_match(user_skills, target_role):

    roles = {

        "AI Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "nlp",
            "computer vision",
            "generative ai"
        ],


        "Machine Learning Engineer": [
            "python",
            "machine learning",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "deep learning"
        ],


        "Data Scientist": [
            "python",
            "machine learning",
            "statistics",
            "deep learning",
            "sql",
            "nlp"
        ],


        "Data Analyst": [
            "sql",
            "excel",
            "power bi",
            "tableau",
            "python",
            "pandas",
            "statistics"
        ],


        "Full Stack Developer": [
            "html",
            "css",
            "javascript",
            "react",
            "node.js",
            "sql"
        ]

    }


    required_skills = roles.get(
        target_role,
        []
    )


    # Convert categorized skills dictionary into a list

    all_skills = []

    for category, skills in user_skills.items():
        all_skills.extend(skills)


    user_skills = set(all_skills)

    required_skills = set(required_skills)


    matched_skills = user_skills.intersection(
        required_skills
    )


    missing_skills = required_skills.difference(
        user_skills
    )


    score = int(
        (len(matched_skills) / len(required_skills)) * 100
    )


    return {
        "role": target_role,
        "score": score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }