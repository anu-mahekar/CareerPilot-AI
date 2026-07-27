import streamlit as st


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


        progress = 0


        if roadmap:

            for role, completed in roadmap.items():

                progress = len(completed)



        st.metric(
            "🛣 Skills Completed",
            progress
        )



    st.divider()



    # Skills Summary


    st.subheader(
        "🧠 Your Skill Profile"
    )


    if all_skills:

        st.write(
            f"You have **{len(all_skills)} detected skills**"
        )


        display_skills = all_skills[:15]


        for skill in display_skills:

            st.write(
                "✅",
                skill.title()
            )


        if len(all_skills) > 15:

            st.info(
                f"+ {len(all_skills)-15} more skills"
            )



    st.divider()



    # Quick Actions


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