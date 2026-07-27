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



# Select Role

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


"AI Engineer": [

"Python Advanced",
"Statistics for AI",
"Machine Learning Basics",
"Deep Learning",
"TensorFlow",
"PyTorch",
"NLP",
"Computer Vision",
"MLOps",
"Model Deployment"

],



"Machine Learning Engineer": [

"Python",
"Machine Learning",
"Scikit-Learn",
"Feature Engineering",
"Model Evaluation",
"Deep Learning",
"TensorFlow",
"PyTorch",
"MLOps"

],



"Data Scientist": [

"Python",
"SQL",
"Statistics",
"Pandas",
"Machine Learning",
"Data Visualization",
"Deep Learning",
"Experiment Design"

],



"Data Analyst": [

"Excel",
"SQL",
"Python",
"Pandas",
"Power BI",
"Tableau",
"Statistics",
"Business Analytics"

],



"Full Stack Developer": [

"HTML",
"CSS",
"JavaScript",
"React",
"REST APIs",
"Node.js",
"Database Design",
"Cloud Deployment"

]

}



skills = roadmaps[target_role]



# Store Progress

if "roadmap_progress" not in st.session_state:

    st.session_state["roadmap_progress"] = {}



if target_role not in st.session_state["roadmap_progress"]:

    st.session_state["roadmap_progress"][target_role] = []



completed = st.session_state["roadmap_progress"][target_role]



st.divider()


st.subheader(
    f"🚀 {target_role} Roadmap"
)



# Skill checklist

for skill in skills:

    checked = st.checkbox(
        skill,
        value=skill in completed
    )


    if checked:

        if skill not in completed:

            completed.append(skill)


    else:

        if skill in completed:

            completed.remove(skill)



# Calculate Progress

completed_count = len(completed)

total_skills = len(skills)


progress = completed_count / total_skills



st.divider()


st.subheader("📊 Your Progress")


st.progress(progress)


st.write(
    f"Completed: **{completed_count}/{total_skills} skills**"
)


st.write(
    f"Progress: **{int(progress*100)}%**"
)



# Status Message

if progress == 1:

    st.success(
        "🎉 Congratulations! You completed your career roadmap."
    )


elif progress >= 0.5:

    st.info(
        "🔥 Great progress! Keep building your skills."
    )


else:

    st.warning(
        "🚀 Start completing skills to become job-ready."
    )



st.divider()


# Project Ideas

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