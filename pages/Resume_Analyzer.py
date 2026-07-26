import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.ats import calculate_ats_score
from utils.skills import extract_skills
from utils.career import recommend_careers
from utils.skill_gap import calculate_skill_gap


st.title("📄 Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)


if uploaded_file:

    st.success("Resume uploaded successfully!")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(uploaded_file)


    # ---------------- ATS SCORE ----------------

    ats_score = calculate_ats_score(resume_text)

    st.subheader("🎯 ATS Score")

    st.progress(ats_score / 100)

    st.write(
        f"Your Resume Score: **{ats_score}/100**"
    )


    # ---------------- SKILL EXTRACTION ----------------
    skills = extract_skills(resume_text)
    

    # Save skills for other pages
    st.session_state["user_skills"] = skills


    st.subheader("🧠 Skills Analysis")


    for category, skill_list in skills.items():

        if skill_list:

            st.write(f"### {category}")

            for skill in skill_list:
                st.write("✅", skill.title())

    st.divider()


    # ---------------- CAREER RECOMMENDATION ----------------

    career_results = recommend_careers(skills)


    st.subheader("🎯 Recommended Careers")


    for career in career_results:

        st.write(
            f"### {career['career']}"
        )

        st.progress(
            career["score"] / 100
        )

        st.write(
            f"Match Score: **{career['score']}%**"
        )

        st.write(
            "Matched Skills:",
            ", ".join(career["matched_skills"])
        )

        st.divider()



    # ---------------- SKILL GAP ANALYSIS ----------------

    st.subheader("📊 Skill Gap Analysis")


    if career_results:

        selected_career = career_results[0]["career"]


        missing_skills = calculate_skill_gap(
            skills,
            selected_career
        )


        st.write(
            f"Target Role: **{selected_career}**"
        )


        if missing_skills:

            st.write("Skills to Improve:")

            for skill in missing_skills:
                st.write(
                    "❌",
                    skill.title()
                )

        else:

            st.success(
                "You have all required skills!"
            )



    st.divider()


    # ---------------- RESUME TEXT ----------------

    st.subheader("📄 Extracted Resume Text")


    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )