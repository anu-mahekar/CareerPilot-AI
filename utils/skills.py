def extract_skills(resume_text):

    skill_categories = {

        "Programming Languages": [
            "python",
            "java",
            "c",
            "c++",
            "javascript",
            "typescript",
            "r",
            "scala",
            "go"
        ],


        "AI / Machine Learning": [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "scikit-learn",
            "nlp",
            "computer vision",
            "opencv",
            "generative ai",
            "llm",
            "rag"
        ],


        "Data Analytics": [
            "sql",
            "mysql",
            "mongodb",
            "pandas",
            "numpy",
            "statistics",
            "excel",
            "power bi",
            "tableau"
        ],


        "Web Development": [
            "html",
            "css",
            "react",
            "node.js",
            "flask",
            "django",
            "fastapi",
            "rest api"
        ],


        "Cloud & DevOps": [
            "azure",
            "aws",
            "google cloud",
            "docker",
            "kubernetes",
            "linux",
            "git",
            "github"
        ],


        "Engineering Tools": [
            "matlab",
            "autocad",
            "solidworks",
            "arduino",
            "esp32",
            "iot"
        ]

    }


    resume_text = resume_text.lower()

    detected_skills = {}


    for category, skills in skill_categories.items():

        found_skills = []

        for skill in skills:

            if skill in resume_text:
                found_skills.append(skill)

        detected_skills[category] = found_skills


    return detected_skills