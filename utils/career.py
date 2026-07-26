def recommend_careers(skill_categories):

    # Convert categorized skills into a single list
    skills = []

    for category, skill_list in skill_categories.items():
        skills.extend(skill_list)


    careers = {

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
        ],


        "Software Developer": [
            "java",
            "python",
            "c++",
            "data structures",
            "algorithms",
            "git"
        ],


        "Cloud Engineer": [
            "aws",
            "azure",
            "docker",
            "kubernetes",
            "linux"
        ],


        "Business Analyst": [
            "sql",
            "excel",
            "power bi",
            "tableau",
            "statistics"
        ],


        "Data Engineer": [
            "python",
            "sql",
            "spark",
           "hadoop",
            "aws",
            "docker"
        ]

    }


    results = []


    for career, required_skills in careers.items():

        matched = set(skills).intersection(required_skills)


        # Skill matching score
        score = int(
            (len(matched) / len(required_skills)) * 100
        )


        # AI/ML skill bonus
        ai_bonus = 0


        if career in [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ]:

            ai_skills = [
                "machine learning",
                "deep learning",
                "nlp",
                "opencv",
                "generative ai",
                "scikit-learn"
            ]


            ai_matches = len(
                set(skills).intersection(ai_skills)
            )


            ai_bonus = ai_matches * 2



        # Career relevance bonus
        career_bonus = 0


        if career == "AI Engineer":
            career_bonus = 10

        elif career == "Machine Learning Engineer":
            career_bonus = 10

        elif career == "Data Scientist":
            career_bonus = 0

        elif career == "Data Analyst":
            career_bonus = 3



        # Reduce unrelated roles
        penalty = 0


        if career == "Full Stack Developer":

            if "machine learning" in skills:
                penalty = 10


        if career == "Business Analyst":

            if "machine learning" in skills:
                penalty = 5



        # AI/ML profile detection bonus
        profile_bonus = 0


        if (
            "machine learning" in skills
            and "python" in skills
        ):

            if career == "AI Engineer":
                profile_bonus = 15


            elif career == "Machine Learning Engineer":
                profile_bonus = 15


            elif career == "Data Scientist":
                profile_bonus = 3



        final_score = (
            score
            + ai_bonus
            + career_bonus
            + profile_bonus
            - penalty
        )


        if final_score > 100:
            final_score = 100


        if final_score < 0:
            final_score = 0



        results.append(
            {
                "career": career,
                "score": final_score,
                "matched_skills": list(matched)
            }
        )



    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return results[:5]