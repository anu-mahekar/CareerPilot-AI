import streamlit as st
import os

from database.db_operations import (
    save_roadmap_progress,
    get_roadmap_progress
)


st.title("🛣 Career Roadmap")

st.write(
    "Get a personalized learning roadmap and track your progress."
)


# ---------------- LOAD USER ----------------

if "user_id" not in st.session_state:

    if os.path.exists("database/current_user.txt"):

        with open("database/current_user.txt","r") as f:

            user_id = f.read().strip()

            if user_id:
                st.session_state["user_id"] = int(user_id)



# ---------------- CHECK RESUME ----------------

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.info(
        "Go to Resume Analyzer → Upload PDF → Come back here."
    )

    st.stop()



if "user_id" not in st.session_state:

    st.warning(
        "User information not found. Upload resume again."
    )

    st.stop()



user_id = st.session_state["user_id"]



# ---------------- RESUME SKILLS ----------------

resume_skills = [

    skill.lower()

    for category, skills in st.session_state["user_skills"].items()

    for skill in skills

]



# ---------------- ROLE SELECTION ----------------

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



# ---------------- ROADMAP DATABASE ----------------

roadmaps = {


"AI Engineer": {

"Beginner":[

"Python Advanced",

"Statistics for AI",

"Machine Learning Basics"

],

"Intermediate":[

"Deep Learning",

"TensorFlow",

"PyTorch",

"NLP",

"Computer Vision"

],

"Advanced":[

"MLOps",

"Model Deployment",

"Cloud AI Services"

]

},



"Machine Learning Engineer": {

"Beginner":[

"Python",

"Machine Learning",

"Scikit-Learn"

],

"Intermediate":[

"Feature Engineering",

"Model Evaluation",

"Deep Learning",

"TensorFlow"

],

"Advanced":[

"PyTorch",

"MLOps",

"Model Deployment"

]

},



"Data Scientist": {

"Beginner":[

"Python",

"SQL",

"Statistics"

],

"Intermediate":[

"Pandas",

"Machine Learning",

"Data Visualization"

],

"Advanced":[

"Deep Learning",

"Experiment Design",

"Model Deployment"

]

},



"Data Analyst": {

"Beginner":[

"Excel",

"SQL",

"Python"

],

"Intermediate":[

"Pandas",

"Power BI",

"Tableau"

],

"Advanced":[

"Statistics",

"Business Analytics",

"Data Storytelling"

]

},



"Full Stack Developer": {

"Beginner":[

"HTML",

"CSS",

"JavaScript"

],

"Intermediate":[

"React",

"REST APIs",

"Node.js"

],

"Advanced":[

"Database Design",

"Cloud Deployment",

"System Design"

]

}

}



selected_roadmap = roadmaps[target_role]



# ---------------- LOAD COMPLETED SKILLS ----------------

completed = get_roadmap_progress(

    user_id,

    target_role

)



if completed is None:

    completed = []



# ---------------- AUTO DETECT SKILLS ----------------

for level, skills in selected_roadmap.items():


    for skill in skills:


        if skill.lower() in resume_skills:


            if skill not in completed:

                completed.append(skill)

                save_roadmap_progress(

                    user_id,

                    target_role,

                    skill

                )



# ---------------- ROADMAP DISPLAY ----------------


st.divider()

st.subheader(
    f"🚀 {target_role} Learning Path"
)



all_skills = []



for level, skills in selected_roadmap.items():


    with st.expander(
        f"📚 {level}",
        expanded=True
    ):


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


                    save_roadmap_progress(

                        user_id,

                        target_role,

                        skill

                    )


            else:


                if skill in completed:

                    completed.remove(skill)



# ---------------- PROGRESS ----------------


completed_count = len(completed)

total_skills = len(all_skills)



if total_skills:

    progress = completed_count / total_skills

else:

    progress = 0



percentage = int(progress * 100)



st.divider()


st.subheader(
    "📊 Learning Progress"
)


st.progress(progress)



st.metric(

    "Skills Completed",

    f"{completed_count}/{total_skills}"

)


st.metric(

    "Roadmap Completion",

    f"{percentage}%"

)



# Save for dashboard

st.session_state["roadmap_percentage"] = percentage



# ---------------- STATUS ----------------


if percentage == 100:


    st.success(
        "🎉 You are fully prepared for this career path!"
    )


elif percentage >= 70:


    st.success(
        "🔥 Excellent progress! Start building advanced projects."
    )


elif percentage >= 40:


    st.info(
        "🚀 Good foundation. Continue improving your skills."
    )


else:


    st.warning(
        "📚 Start learning the fundamentals first."
    )



# ---------------- PROJECTS ----------------


st.divider()


st.subheader(
    "💡 Recommended Projects"
)



projects = {


"AI Engineer":[

"AI Chatbot using NLP",

"Image Classification System",

"Recommendation System"

],


"Machine Learning Engineer":[

"House Price Prediction",

"Fraud Detection System",

"Customer Churn Prediction"

],


"Data Scientist":[

"Sales Forecasting",

"Sentiment Analysis",

"Customer Segmentation"

],


"Data Analyst":[

"Sales Dashboard",

"Business Analytics Report",

"Customer Analysis"

],


"Full Stack Developer":[

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