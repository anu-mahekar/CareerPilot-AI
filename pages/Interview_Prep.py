import streamlit as st
import os

from utils.interview_ai import evaluate_answer
from database.db_operations import (
    save_interview_result,
    get_interview_progress
)


st.title("🎤 Interview Preparation")

st.write(
    "Prepare for interviews with role-based technical and HR questions."
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



# ---------------- ROLE ----------------


target_role = st.selectbox(

    "🎯 Select your interview role",

    [

        "AI Engineer",

        "Machine Learning Engineer",

        "Data Scientist",

        "Data Analyst",

        "Full Stack Developer"

    ]

)



difficulty = st.selectbox(

    "📊 Select difficulty level",

    [

        "Beginner",

        "Intermediate",

        "Advanced"

    ]

)



# ---------------- QUESTIONS ----------------


questions = {


"AI Engineer": {

"Beginner":[

"What is Artificial Intelligence?",

"What is Machine Learning?",

"Difference between AI and ML?",

"What is supervised learning?"

],

"Intermediate":[

"Explain neural networks.",

"What is NLP?",

"Explain CNN architecture.",

"What is model training?"

],

"Advanced":[

"Explain Transformer architecture.",

"How does Generative AI work?",

"How do you deploy AI models?",

"Explain MLOps workflow."

]

},



"Machine Learning Engineer": {


"Beginner":[

"What is Machine Learning?",

"Difference between supervised and unsupervised learning?",

"What is overfitting?",

"What is train-test split?"

],


"Intermediate":[

"Explain Random Forest algorithm.",

"What is feature engineering?",

"What is cross validation?",

"Explain model evaluation metrics."

],


"Advanced":[

"Explain hyperparameter tuning.",

"How do you optimize ML models?",

"Explain ML deployment pipeline.",

"What is MLOps?"

]

},



"Data Scientist": {


"Beginner":[

"What is data science?",

"Difference between AI and Data Science?",

"What is data preprocessing?",

"What is EDA?"

],


"Intermediate":[

"Explain feature selection.",

"What is hypothesis testing?",

"Explain regression algorithms.",

"What are clustering techniques?"

],


"Advanced":[

"Explain A/B testing.",

"How do you handle large datasets?",

"Explain recommendation systems.",

"Explain predictive modelling."

]

},



"Data Analyst": {


"Beginner":[

"What is SQL?",

"What is data visualization?",

"Difference between Excel and Power BI?",

"What is data cleaning?"

],


"Intermediate":[

"Explain SQL joins.",

"What are dashboards?",

"Explain Power BI relationships.",

"What is KPI?"

],


"Advanced":[

"Explain business intelligence.",

"How do you find insights from data?",

"Explain statistical analysis.",

"How do you automate reports?"

]

},



"Full Stack Developer": {


"Beginner":[

"What is HTML?",

"What is CSS?",

"What is JavaScript?",

"What is frontend development?"

],


"Intermediate":[

"Explain React components.",

"What are REST APIs?",

"Explain database design.",

"What is backend development?"

],


"Advanced":[

"Explain authentication.",

"How do you deploy web applications?",

"What is system design?",

"Explain scalability."

]

}

}



selected_questions = questions[target_role][difficulty]



# ---------------- SESSION TRACKING ----------------


if "evaluated_answers" not in st.session_state:

    st.session_state["evaluated_answers"] = {}



st.divider()


st.subheader(
    f"🔥 {difficulty} Questions - {target_role}"
)



for index, question in enumerate(
    selected_questions,
    start=1
):


    st.write(
        f"### {index}. {question}"
    )


    answer = st.text_area(

        "Your Answer",

        key=f"{target_role}_{difficulty}_{index}"

    )



    if st.button(

        f"Evaluate Answer {index}",

        key=f"button_{index}"

    ):


        if answer.strip():


            result = evaluate_answer(

                question,

                answer

            )



            st.session_state["evaluated_answers"][index] = True



            st.success(

                f"📊 Score: {result['score']}/10"

            )


            st.info(

                f"💡 Feedback: {result['feedback']}"

            )



            if result["covered"]:

                st.success(

                    "✅ Covered: " +

                    ", ".join(result["covered"])

                )



            if result["missing"]:

                st.warning(

                    "❌ Missing: " +

                    ", ".join(result["missing"])

                )



            if "user_id" in st.session_state:


                save_interview_result(

                    st.session_state["user_id"],

                    result["score"],

                    result["feedback"]

                )



        else:


            st.warning(

                "Please enter your answer."

            )



# ---------------- PROGRESS ----------------


total_questions = len(selected_questions)


completed = len(
    st.session_state["evaluated_answers"]
)



progress = int(

    (completed / total_questions) * 100

)



st.session_state["interview_progress"] = progress



st.divider()


st.subheader(
    "📊 Interview Progress"
)



st.progress(

    progress / 100

)



st.metric(

    "Completed",

    f"{completed}/{total_questions}"

)



st.metric(

    "Progress",

    f"{progress}%"

)



# ---------------- HR ----------------


st.divider()


st.subheader(
    "💼 HR Interview Questions"
)



hr_questions = [

"Tell me about yourself.",

"Why should we hire you?",

"Explain your projects.",

"What are your strengths and weaknesses?",

"Where do you see yourself in 5 years?"

]



for q in hr_questions:

    st.write(

        "✅",

        q

    )



# ---------------- TIPS ----------------


st.divider()


st.subheader(
    "💡 Interview Tips"
)



tips = [

"Explain your projects clearly.",

"Understand fundamentals before advanced topics.",

"Practice SQL and coding problems.",

"Use real examples while answering.",

"Prepare your resume thoroughly."

]



for tip in tips:

    st.write(

        "🚀",

        tip

    )