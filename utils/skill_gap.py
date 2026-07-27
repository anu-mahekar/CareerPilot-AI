def calculate_skill_gap(skill_categories, career):

    # Convert categorized skills into one list
    user_skills = []

    for category, skills in skill_categories.items():
        user_skills.extend(skills)


    # Normalize skills
    user_skills = [
        skill.lower()
        for skill in user_skills
    ]


    career_skills = {

        "AI Engineer": {

            "Deep Learning": {
                "skill": "deep learning",
                "why": "Required for building advanced AI models and neural networks.",
                "learn": [
                    "Neural Networks",
                    "CNN",
                    "Backpropagation"
                ]
            },

            "TensorFlow": {
                "skill": "tensorflow",
                "why": "Used for training and deploying machine learning models.",
                "learn": [
                    "TensorFlow basics",
                    "Model training",
                    "Model deployment"
                ]
            },

            "PyTorch": {
                "skill": "pytorch",
                "why": "Popular framework for deep learning research and applications.",
                "learn": [
                    "Tensors",
                    "Neural Network Implementation"
                ]
            },

            "Computer Vision": {
                "skill": "computer vision",
                "why": "Needed for image and video based AI applications.",
                "learn": [
                    "Image Processing",
                    "OpenCV",
                    "Object Detection"
                ]
            }
        },


        "Machine Learning Engineer": {

            "Deep Learning": {
                "skill": "deep learning",
                "why": "Used for advanced machine learning solutions.",
                "learn": [
                    "Neural Networks",
                    "CNN",
                    "RNN"
                ]
            },

            "TensorFlow": {
                "skill": "tensorflow",
                "why": "Used for ML model development.",
                "learn": [
                    "TensorFlow APIs",
                    "Model Deployment"
                ]
            },

            "PyTorch": {
                "skill": "pytorch",
                "why": "Used for deep learning implementation.",
                "learn": [
                    "Tensors",
                    "Model Training"
                ]
            }
        },


        "Data Scientist": {

            "Statistics": {
                "skill": "statistics",
                "why": "Important for analysis and model evaluation.",
                "learn": [
                    "Probability",
                    "Hypothesis Testing",
                    "Regression Analysis"
                ]
            },

            "Deep Learning": {
                "skill": "deep learning",
                "why": "Helps build advanced predictive models.",
                "learn": [
                    "Neural Networks",
                    "CNN",
                    "Model Optimization"
                ]
            }
        },


        "Data Analyst": {

            "Statistics": {
                "skill": "statistics",
                "why": "Required for extracting insights from data.",
                "learn": [
                    "Probability",
                    "Data Distribution",
                    "Hypothesis Testing"
                ]
            },

            "Excel": {
                "skill": "excel",
                "why": "Used for reporting and analysis.",
                "learn": [
                    "Advanced Excel",
                    "Pivot Tables",
                    "Charts"
                ]
            }
        },


        "Full Stack Developer": {

            "Node.js": {
                "skill": "node.js",
                "why": "Required for backend development using JavaScript.",
                "learn": [
                    "Express.js",
                    "REST APIs",
                    "Backend Development"
                ]
            }
        }
    }


    required_skills = career_skills.get(
        career,
        {}
    )


    missing_skills = []


    for name, details in required_skills.items():

        if details["skill"] not in user_skills:

            missing_skills.append(
                {
                    "name": name,
                    "why": details["why"],
                    "learn": details["learn"]
                }
            )


    return missing_skills