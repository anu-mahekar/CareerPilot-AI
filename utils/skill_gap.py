def calculate_skill_gap(skill_categories, career):


    # Convert dictionary skills into list

    user_skills = []

    for category, skills in skill_categories.items():
        user_skills.extend(skills)



    required_skills = {


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
            "python",
            "sql",
            "pandas",
            "power bi",
            "tableau",
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



    required = required_skills.get(
        career,
        []
    )


    missing = []


    for skill in required:

        if skill not in user_skills:

            missing.append(skill)


    return missing