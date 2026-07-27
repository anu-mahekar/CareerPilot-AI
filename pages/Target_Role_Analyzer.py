import streamlit as st

from utils.role_analyzer import analyze_role_match


st.title("🎯 Target Role Analyzer")


st.write(
    "Analyze your resume skills against your desired career role."
)



# ---------------- CHECK RESUME SKILLS ----------------

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.info(
        "Go to Resume Analyzer → Upload PDF → "
        "Wait until skills are detected → Come back here."
    )

    st.stop()



skills = st.session_state["user_skills"]



# ---------------- TARGET ROLE SELECTION ----------------


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



# ---------------- ANALYZE BUTTON ----------------


if st.button("Analyze Role"):


    result = analyze_role_match(
        skills,
        target_role
    )
        # Save result for Career Report
    st.session_state["target_role_result"] = result


    # ---------------- ROLE RESULT ----------------


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



    # ---------------- PROFILE STRENGTH ----------------


    if result["strength"] == "Excellent Match":

        st.success(
            f"🌟 Profile Strength: {result['strength']}"
        )


    elif result["strength"] == "Good Foundation":

        st.info(
            f"🌟 Profile Strength: {result['strength']}"
        )


    else:

        st.warning(
            f"🌟 Profile Strength: {result['strength']}"
        )



    # ---------------- CAREER SUMMARY ----------------


    st.subheader(
        "🚀 Career Recommendation Summary"
    )


    matched = ", ".join(
        skill.title()
        for skill in result["matched_skills"]
    )


    if result["score"] >= 80:


        st.success(
            f"""
Your resume shows a strong alignment with the **{result['role']}** role.

✅ Your current strengths:

{matched}

🎯 Focus Areas:

- Improve missing technical skills
- Build role-specific projects
- Prepare interview concepts
- Strengthen practical experience
"""
        )


    elif result["score"] >= 60:


        st.info(
            f"""
You have a good foundation for the **{result['role']}** role.

✅ Current Strengths:

{matched}

Recommended Actions:

- Complete missing skill areas
- Create 2-3 projects
- Practice real-world problems
- Improve portfolio visibility
"""
        )


    else:


        st.warning(
            f"""
Your current profile needs improvement for the **{result['role']}** role.

Start by:

- Learning required technologies
- Building beginner projects
- Improving your resume with relevant skills
"""
        )



    # ---------------- MATCHING SKILLS ----------------


    st.subheader(
        "✅ Your Strengths"
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



    # ---------------- ROADMAP ----------------


    st.subheader(
        "🛠️ Personalized Growth Roadmap"
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
🎉 You have all required skills!


### Recommended Next Steps:

🚀 Build 2-3 projects related to this role

📚 Learn advanced concepts and best practices

☁️ Explore deployment and cloud technologies

💼 Practice role-specific interview questions
"""
        )