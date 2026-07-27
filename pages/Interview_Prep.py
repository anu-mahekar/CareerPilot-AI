import streamlit as st
from utils.interview_ai import evaluate_answer


st.title("🎤 Interview Preparation")

st.write(
    "Prepare for interviews with role-based technical and HR questions."
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
    "🎯 Select your interview role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Full Stack Developer"
    ]
)



# Difficulty Level

difficulty = st.selectbox(
    "📊 Select difficulty level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)



# Question Database

questions = {

"AI Engineer": {

"Beginner": [
"What is Artificial Intelligence?",
"What is Machine Learning?",
"Difference between AI and ML?",
"What is supervised learning?"
],

"Intermediate": [
"Explain neural networks.",
"What is NLP?",
"Explain CNN architecture.",
"What is model training?"
],

"Advanced": [
"Explain Transformer architecture.",
"How does Generative AI work?",
"How do you deploy AI models?",
"Explain MLOps workflow."
]

},


"Machine Learning Engineer": {

"Beginner": [
"What is Machine Learning?",
"Difference between supervised and unsupervised learning?",
"What is overfitting?",
"What is train-test split?"
],

"Intermediate": [
"Explain Random Forest algorithm.",
"What is feature engineering?",
"What is cross validation?",
"Explain model evaluation metrics."
],

"Advanced": [
"Explain hyperparameter tuning.",
"How do you optimize ML models?",
"Explain ML deployment pipeline.",
"What is MLOps?"
]

},


"Data Scientist": {

"Beginner": [
"What is data science?",
"Difference between AI and Data Science?",
"What is data preprocessing?",
"What is EDA?"
],

"Intermediate": [
"Explain feature selection.",
"What is hypothesis testing?",
"Explain regression algorithms.",
"What are clustering techniques?"
],

"Advanced": [
"Explain A/B testing.",
"How do you handle large datasets?",
"Explain recommendation systems.",
"Explain predictive modelling."
]

},


"Data Analyst": {

"Beginner": [
"What is SQL?",
"What is data visualization?",
"Difference between Excel and Power BI?",
"What is data cleaning?"
],

"Intermediate": [
"Explain SQL joins.",
"What are dashboards?",
"Explain Power BI relationships.",
"What is KPI?"
],

"Advanced": [
"Explain business intelligence.",
"How do you find insights from data?",
"Explain statistical analysis.",
"How do you automate reports?"
]

},


"Full Stack Developer": {

"Beginner": [
"What is HTML?",
"What is CSS?",
"What is JavaScript?",
"What is frontend development?"
],

"Intermediate": [
"Explain React components.",
"What are REST APIs?",
"Explain database design.",
"What is backend development?"
],

"Advanced": [
"Explain authentication.",
"How do you deploy web applications?",
"What is system design?",
"Explain scalability."
]

}

}



selected_questions = questions[target_role][difficulty]



# Display Questions

st.divider()

st.subheader(
    f"🔥 {difficulty} Questions for {target_role}"
)



answered_questions = 0



for index, question in enumerate(
    selected_questions,
    start=1
):

    st.write(
        f"**{index}. {question}**"
    )


    answer = st.text_area(
        "Your Answer",
        key=f"answer_{target_role}_{difficulty}_{index}"
    )


    if answer.strip():

        answered_questions += 1


        if st.button(
            f"Evaluate Answer {index}",
            key=f"evaluate_{target_role}_{difficulty}_{index}"
        ):

            result = evaluate_answer(
                question,
                answer
            )


            st.success(
                f"📊 Answer Score: {result['score']}/10"
            )


            st.info(
                f"💡 Feedback: {result['feedback']}"
            )



# ---------------- Interview Progress ----------------


total_questions = len(selected_questions)



if total_questions > 0:

    interview_progress = int(
        (answered_questions / total_questions) * 100
    )

else:

    interview_progress = 0



# Save progress

st.session_state["interview_progress"] = interview_progress



st.divider()

st.subheader(
    "📊 Interview Progress"
)



st.progress(
    interview_progress / 100
)



st.write(
    f"Completed: **{answered_questions}/{total_questions} questions**"
)


st.write(
    f"Progress: **{interview_progress}%**"
)



# HR Section

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



# Interview Tips

st.divider()

st.subheader(
    "💡 Interview Tips"
)



tips = [

"Explain your projects clearly.",

"Understand the basics before advanced topics.",

"Practice SQL and coding problems regularly.",

"Use real examples while answering.",

"Prepare your resume thoroughly."

]



for tip in tips:

    st.write(
        "🚀",
        tip
    )