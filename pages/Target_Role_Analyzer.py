import streamlit as st
import os

from utils.role_analyzer import analyze_role_match
from database.db_operations import save_role_match


st.title("🎯 Target Role Analyzer")

st.write(
    "Analyze your resume skills against your desired career role."
)


# ---------------- LOAD USER ----------------

if "user_id" not in st.session_state:

    if os.path.exists("database/current_user.txt"):

        with open("database/current_user.txt", "r") as f:

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



skills = st.session_state["user_skills"]



# ---------------- CHECK USER ----------------

if "user_id" not in st.session_state:

    st.warning(
        "User information not found. Please upload resume again."
    )

    st.stop()



user_id = st.session_state["user_id"]



# ---------------- ROLE SELECTION ----------------

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



# ---------------- ANALYZE ROLE ----------------

if st.button("🚀 Analyze Role"):


    result = analyze_role_match(
        skills,
        target_role
    )


    # Save session values

    st.session_state["target_role_result"] = result

    st.session_state["selected_role"] = target_role

    st.session_state["role_match_score"] = result["score"]



    # Save role score in database

    save_role_match(
        user_id,
        target_role,
        result["score"]
    )



    st.divider()



    # ---------------- RESULT ----------------

    st.subheader(
        "📊 Role Match Result"
    )


    st.write(
        f"Target Role: **{result['role']}**"
    )


    st.progress(
        result["score"] / 100
    )


    st.write(
        f"Match Score: **{result['score']}%**"
    )



    # ---------------- PROFILE STRENGTH ----------------


    if result["score"] >= 80:

        st.success(
            "🌟 Profile Strength: Excellent Match"
        )


    elif result["score"] >= 60:

        st.info(
            "🌟 Profile Strength: Good Foundation"
        )


    else:

        st.warning(
            "🌟 Profile Strength: Needs Improvement"
        )



    # ---------------- MATCHING SKILLS ----------------


    st.subheader(
        "✅ Matching Skills"
    )


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



    # ---------------- LEARNING PLAN ----------------


    st.subheader(
        "🛠 Personalized Growth Roadmap"
    )


    if result["learning_plan"]:


        for item in result["learning_plan"]:


            st.markdown(
                f"""
### ❌ {item['skill'].title()}

**Why it matters:**

{item['why']}

**Learning Topics:**
"""
            )


            for topic in item["learn"]:

                st.write(
                    "📘",
                    topic
                )


            st.divider()



    else:


        st.success(
            """
🎉 You already have the required skills!

Recommended next steps:

🚀 Build projects  
📚 Learn advanced concepts  
💼 Practice interviews
"""
        )