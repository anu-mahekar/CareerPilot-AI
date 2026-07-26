import streamlit as st

from utils.role_analyzer import analyze_role_match


st.title("🎯 Target Role Analyzer")


st.write(
    "Analyze your resume skills against your desired career role."
)


# Check if resume skills exist

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.info(
        "Go to Resume Analyzer → Upload PDF → Wait until skills are detected → Come back here."
    )

    st.stop()



skills = st.session_state["user_skills"]



target_role = st.selectbox(
    "Select your target role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Full Stack Developer"
    ]
)



if st.button("Analyze Role"):


    result = analyze_role_match(
        skills,
        target_role
    )


    st.subheader("📊 Role Match Result")


    st.write(
        f"Target Role: **{result['role']}**"
    )


    st.progress(
        result["score"] / 100
    )


    st.write(
        f"Match Score: **{result['score']}%**"
    )


    # Readiness message

    if result["score"] >= 80:

        st.success(
            "Excellent match! You are highly prepared for this role."
        )


    elif result["score"] >= 60:

        st.info(
            "Good foundation! Improve the missing skills to become job-ready."
        )


    else:

        st.warning(
            "You need to build more skills for this role."
        )



    st.subheader("✅ Matching Skills")


    if result["matched_skills"]:

        for skill in result["matched_skills"]:

            st.write(
                "✅",
                skill.title()
            )

    else:

        st.write(
            "No matching skills found"
        )



    st.subheader("❌ Skills To Improve")


    if result["missing_skills"]:

        for skill in result["missing_skills"]:

            st.write(
                "❌",
                skill.title()
            )

    else:

        st.success(
            "You have all required skills!"
        )