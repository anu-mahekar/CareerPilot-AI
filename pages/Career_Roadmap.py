import streamlit as st


st.title("🛣 Career Roadmap")

st.write(
    "Get a personalized learning roadmap and track your progress."
)


# Check resume upload

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.info(
        "Go to Resume Analyzer → Upload PDF → Come back here."
    )

    st.stop()



resume_skills = [
    skill.lower()
    for category in st.session_state["user_skills"].values()
    for skill in category
]



# Role Selection

target_role = st.selectbox(
    "🎯 Select your career goal",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Full Stack Developer"
    ]
)



# Roadmap Data

roadmaps = {


"AI Engineer": {

"Beginner": [
"Python Advanced",
"Statistics for AI",
"Machine Learning Basics"
],

"Intermediate": [
"Deep Learning",
"TensorFlow",
"PyTorch",
"NLP",
"Computer Vision"
],

"Advanced": [
"MLOps",
"Model Deployment",
"Cloud AI Services"
]

},



"Machine Learning Engineer": {

"Beginner": [
"Python",
"Machine Learning",
"Scikit-Learn"
],

"Intermediate": [
"Feature Engineering",
"Model Evaluation",
"Deep Learning",
"TensorFlow"
],

"Advanced": [
"PyTorch",
"MLOps",
"Model Deployment"
]

},



"Data Scientist": {

"Beginner": [
"Python",
"SQL",
"Statistics"
],

"Intermediate": [
"Pandas",
"Machine Learning",
"Data Visualization"
],

"Advanced": [
"Deep Learning",
"Experiment Design",
"Model Deployment"
]

},



"Data Analyst": {

"Beginner": [
"Excel",
"SQL",
"Python"
],

"Intermediate": [
"Pandas",
"Power BI",
"Tableau"
],

"Advanced": [
"Statistics",
"Business Analytics",
"Data Storytelling"
]

},



"Full Stack Developer": {

"Beginner": [
"HTML",
"CSS",
"JavaScript"
],

"Intermediate": [
"React",
"REST APIs",
"Node.js"
],

"Advanced": [
"Database Design",
"Cloud Deployment",
"System Design"
]

}

}



selected_roadmap = roadmaps[target_role]



# Progress Storage

if "roadmap_progress" not in st.session_state:

    st.session_state["roadmap_progress"] = {}



if target_role not in st.session_state["roadmap_progress"]:

    st.session_state["roadmap_progress"][target_role] = []



completed = st.session_state["roadmap_progress"][target_role]



# Auto detect resume skills

for level, skills in selected_roadmap.items():

    for skill in skills:

        if skill.lower() in resume_skills:

            if skill not in completed:

                completed.append(skill)



st.divider()


st.subheader(
    f"🚀 {target_role} Roadmap"
)



all_skills = []



# Display roadmap

for level, skills in selected_roadmap.items():

    st.subheader(
        f"📚 {level}"
    )


    for skill in skills:

        all_skills.append(skill)


        checked = st.checkbox(
            skill,
            value=skill in completed,
            key=f"{target_role}_{skill}"
        )


        if checked:

            if skill not in completed:
                completed.append(skill)

        else:

            if skill in completed:
                completed.remove(skill)



# Progress Calculation


completed_count = len(completed)

total_skills = len(all_skills)


progress = completed_count / total_skills



st.divider()


st.subheader("📊 Your Progress")


st.progress(progress)



st.write(
    f"Completed Skills: **{completed_count}/{total_skills}**"
)


st.write(
    f"Progress: **{int(progress*100)}%**"
)



# Career Readiness


if progress == 1:

    st.success(
        "🎉 You are fully prepared for this career path!"
    )


elif progress >= 0.7:

    st.success(
        "🔥 Excellent progress! Start building advanced projects."
    )


elif progress >= 0.4:

    st.info(
        "🚀 Good foundation. Continue improving your skills."
    )


else:

    st.warning(
        "📚 Start learning the fundamentals first."
    )



# Projects


st.divider()


st.subheader("💡 Recommended Projects")



projects = {


"AI Engineer": [
"AI Chatbot using NLP",
"Image Classification System",
"Recommendation System"
],


"Machine Learning Engineer": [
"House Price Prediction",
"Fraud Detection System",
"Customer Churn Prediction"
],


"Data Scientist": [
"Sales Forecasting",
"Sentiment Analysis",
"Customer Segmentation"
],


"Data Analyst": [
"Sales Dashboard",
"Business Analytics Report",
"Customer Analysis"
],


"Full Stack Developer": [
"E-Commerce Website",
"Portfolio Website",
"Blog Application"
]

}



for project in projects[target_role]:

    st.write(
        "🚀",
        project
    )