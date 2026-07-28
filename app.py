import streamlit as st
import os

from utils.readiness import calculate_readiness
from database.db_operations import (
    get_user_skills,
    get_user_details,
    get_role_match,
    get_roadmap_progress,
    get_interview_progress
)

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- LOAD USER AFTER REFRESH ----------------

if "user_id" not in st.session_state:

    if os.path.exists("database/current_user.txt"):

        with open("database/current_user.txt", "r") as f:

            user_id = f.read().strip()

            if user_id:
                st.session_state["user_id"] = int(user_id)

# ---------------- LOAD DATABASE DATA ----------------

if "user_id" in st.session_state:

    user_id = st.session_state["user_id"]

    # Load Skills
    saved_skills = get_user_skills(user_id)

    if saved_skills:
        st.session_state["user_skills"] = saved_skills

    # Load User Details
    user_details = get_user_details(user_id)

    if user_details:
    

        st.session_state["ats_score"] = float(
            user_details["ats_score"]
        )

    # Load Role Match
    role_data = get_role_match(user_id)

    if role_data:
        st.session_state["selected_role"] = role_data["role"]
        st.session_state["role_match_score"] = role_data["score"]

    # Load Roadmap Progress
    role = st.session_state.get("selected_role", "AI Engineer")

    completed = get_roadmap_progress(user_id, role)

    roadmap_totals = {
        "AI Engineer": 11,
        "Machine Learning Engineer": 10,
        "Data Scientist": 9,
        "Data Analyst": 9,
        "Full Stack Developer": 9
    }

    total = roadmap_totals.get(role, 10)

    st.session_state["roadmap_percentage"] = int(
        (len(completed) / total) * 100
    )

    # Load Interview Progress
    st.session_state["interview_progress"] = get_interview_progress(user_id)


# ---------------- HERO SECTION ----------------

st.title("🚀 CareerPilot AI")

st.subheader(
    "Your Personal AI Career Mentor"
)

st.write(
    """
Analyze your resume, discover career paths,
identify skill gaps, build learning roadmaps,
and prepare for interviews using AI.
"""
)

st.divider()

# ---------------- DASHBOARD ----------------

if "user_skills" in st.session_state:

    st.success("🎉 Resume analyzed successfully!")

    skills = st.session_state["user_skills"]

    all_skills = []

    for category, skill_list in skills.items():
        for skill in skill_list:
            all_skills.append(skill)

    st.subheader("📊 Career Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        ats_score = float(
            st.session_state.get(
                "ats_score",
                0
            )
        )

        st.metric(
            "📄 ATS Score",
            f"{ats_score}%"
        )

    with col2:

        role = st.session_state.get(
            "selected_role",
            "AI Engineer"
        )

        st.metric(
            "🎯 Target Role",
            role
        )

    with col3:

        st.metric(
            "🧠 Skills Detected",
            len(all_skills)
        )

    with col4:

        readiness = calculate_readiness(

            st.session_state.get(
                "ats_score",
                0
            ),

            st.session_state.get(
                "role_match_score",
                0
            ),

            st.session_state.get(
                "roadmap_percentage",
                0
            ),

            st.session_state.get(
                "interview_progress",
                0
            )
        )

        st.metric(
            "🚀 Career Readiness",
            f"{readiness}%"
        )

    st.divider()

    # ---------------- SKILLS ----------------

    st.subheader("🧠 Your Skill Profile")

    for category, skill_list in skills.items():

        with st.expander(category):

            for skill in skill_list:

                st.write(
                    "✅",
                    skill.title()
                )

else:

    st.info(
        """
👋 Welcome to CareerPilot AI!

Start your journey:

1️⃣ Upload your resume

2️⃣ Analyze your skills

3️⃣ Find matching careers

4️⃣ Build your roadmap

5️⃣ Prepare for interviews
"""
    )

st.divider()

# ---------------- FEATURES ----------------

st.subheader("✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        """
📄 Resume Analyzer

• ATS Score

• Skill Extraction

• Resume Insights
"""
    )

with col2:

    st.info(
        """
🎯 Career Intelligence

• Role Matching

• Skill Gap Detection

• Career Roadmap
"""
    )

with col3:

    st.info(
        """
🎤 Interview Preparation

• Technical Questions

• HR Questions

• AI Feedback
"""
    )

st.divider()

st.markdown(
    "🚀 Build your future with AI-powered career guidance"
)

