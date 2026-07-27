import streamlit as st
from utils.readiness import calculate_readiness


# Page configuration

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)


# Title

st.title("🚀 CareerPilot AI")

st.subheader(
    "Your Personal AI Career Mentor"
)


st.write(
"""
CareerPilot AI analyzes your resume, recommends career paths,
identifies skill gaps, creates learning roadmaps, and prepares you
for interviews.
"""
)


st.divider()



# Dashboard Check

if "user_skills" in st.session_state:


    st.success(
        "🎉 Resume analyzed successfully!"
    )


    skills = st.session_state["user_skills"]



    # Flatten skills

    all_skills = []


    for category, skill_list in skills.items():

        for skill in skill_list:

            all_skills.append(skill)



    # ---------------- Dashboard Cards ----------------


    col1, col2, col3 = st.columns(3)



    with col1:

        ats_score = st.session_state.get(
            "ats_score",
            80
        )


        st.metric(
            "📄 ATS Score",
            f"{ats_score}/100"
        )



    with col2:

        recommended_role = st.session_state.get(
            "recommended_role",
            "AI Engineer"
        )


        st.metric(
            "🎯 Recommended Role",
            recommended_role
        )



    with col3:

        roadmap = st.session_state.get(
            "roadmap_progress",
            {}
        )


        completed_skills = 0


        for role, completed in roadmap.items():

            completed_skills += len(completed)



        st.metric(
            "🛣 Skills Completed",
            completed_skills
        )



    # ---------------- Career Readiness ----------------


    st.divider()


    st.subheader(
        "🎯 Career Readiness Score"
    )



    # ATS Score

    ats_score = st.session_state.get(
        "ats_score",
        80
    )



    # Role Match Score

    role_match_score = st.session_state.get(
        "role_match_score",
        0
    )



    # Roadmap Progress

    roadmap_percentage = st.session_state.get(
        "roadmap_percentage",
        0
    )



    # Interview Progress

    interview_progress = st.session_state.get(
        "interview_progress",
        0
    )



    # Calculate Score

    readiness_score = calculate_readiness(
        ats_score,
        role_match_score,
        roadmap_percentage,
        interview_progress
    )



    st.metric(
        "🚀 Overall Career Readiness",
        f"{readiness_score}%"
    )



    if readiness_score >= 80:

        st.success(
            "🔥 Excellent! Your profile is highly job-ready."
        )


    elif readiness_score >= 60:

        st.info(
            "🚀 Good progress! Continue improving your skills."
        )


    else:

        st.warning(
            "📚 Keep learning and building projects."
        )



    # ---------------- Readiness Breakdown ----------------


    st.divider()


    st.subheader(
        "📊 Readiness Breakdown"
    )


    col1, col2 = st.columns(2)



    with col1:

        st.metric(
            "📄 Resume Strength",
            f"{ats_score}%"
        )


        st.metric(
            "🎯 Role Match",
            f"{role_match_score}%"
        )



    with col2:

        st.metric(
            "🛣 Roadmap Progress",
            f"{roadmap_percentage}%"
        )


        st.metric(
            "🎤 Interview Preparation",
            f"{interview_progress}%"
        )



    st.divider()



    # ---------------- Skills Summary ----------------


    st.subheader(
        "🧠 Your Skill Profile"
    )



    st.write(
        f"You have **{len(all_skills)} detected skills**"
    )



    for skill in all_skills[:15]:

        st.write(
            "✅",
            skill.title()
        )



    if len(all_skills) > 15:

        st.info(
            f"+ {len(all_skills)-15} more skills"
        )



    st.divider()



    # ---------------- Quick Actions ----------------


    st.subheader(
        "🚀 Continue Your Career Journey"
    )



    col1, col2, col3 = st.columns(3)



    with col1:

        st.info(
"""
📚 Skill Gap Analysis

Find missing skills and
improve your profile.
"""
        )



    with col2:

        st.info(
"""
🛣 Career Roadmap

Track your learning
progress.
"""
        )



    with col3:

        st.info(
"""
🎤 Interview Prep

Practice role-based
questions.
"""
        )



else:


    st.info(
"""
👋 Welcome to CareerPilot AI!

Start your journey:

1. Upload your resume
2. Analyze your skills
3. Discover suitable careers
4. Build your roadmap
5. Prepare for interviews
"""
    )



st.divider()



# Features

st.subheader(
    "✨ Platform Features"
)



features = [

"📄 Resume Analysis & ATS Scoring",

"🎯 AI Career Recommendations",

"📚 Skill Gap Detection",

"🛣 Personalized Learning Roadmap",

"🎤 Interview Preparation",

"✍ Cover Letter Generation",

"📥 Career Report PDF"

]



for feature in features:

    st.write(
        "✅",
        feature
    )