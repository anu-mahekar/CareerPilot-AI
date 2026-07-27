import streamlit as st

from utils.skill_gap import calculate_skill_gap


st.title("🎯 Skill Gap Analysis")


st.write(
    "Find missing skills for your dream job role."
)


# Check if resume skills exist
if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.info(
        "Go to Resume Analyzer → Upload PDF → Come back here."
    )

    st.stop()



skills = st.session_state["user_skills"]



roles = [
    "AI Engineer",
    "Machine Learning Engineer",
    "Data Scientist",
    "Data Analyst",
    "Full Stack Developer"
]


selected_role = st.selectbox(
    "Select your target role",
    roles
)



if st.button("Analyze Skill Gap"):


    missing_skills = calculate_skill_gap(
        skills,
        selected_role
    )


    st.subheader(
        f"📊 Target Role: {selected_role}"
    )


    if missing_skills:


        st.write(
            "### ❌ Skills To Improve"
        )


        for skill in missing_skills:


            st.write(
                f"## ❌ {skill['name']}"
            )


            st.write(
                "**Why it matters:**",
                skill["why"]
            )


            st.write(
                "**Learning Topics:**"
            )


            for topic in skill["learn"]:

                st.write(
                    "✅",
                    topic
                )


            st.divider()


    else:

        st.success(
            "🎉 You have all required skills for this role!"
        )