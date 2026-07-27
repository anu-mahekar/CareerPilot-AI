import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.ats import calculate_ats_score
from utils.skills import extract_skills
from utils.career import recommend_careers


st.title("📄 Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)


if uploaded_file:

    st.success("Resume uploaded successfully!")


    # ---------------- EXTRACT TEXT ----------------

    resume_text = extract_text_from_pdf(uploaded_file)



    # ---------------- ATS SCORE ----------------

    ats_score = calculate_ats_score(resume_text)


    st.subheader("🎯 ATS Score")


    st.progress(
        ats_score / 100
    )


    st.write(
        f"Your Resume Score: **{ats_score}/100**"
    )



    # ---------------- SKILL EXTRACTION ----------------

    skills = extract_skills(resume_text)


    # Save skills for other pages

    st.session_state["user_skills"] = skills

    st.session_state["resume_text"] = resume_text



    st.subheader("🧠 Skills Analysis")


    for category, skill_list in skills.items():

        if skill_list:

            st.write(
                f"### {category}"
            )


            for skill in skill_list:

                st.write(
                    "✅",
                    skill.title()
                )


    st.divider()



    # ---------------- CAREER RECOMMENDATION ----------------


    career_results = recommend_careers(skills)


    st.subheader("🎯 Recommended Careers")

    st.write(
    "Based on your resume skills, these careers are recommended:"
    )


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

    # ---------------- RESUME TEXT ----------------


    st.subheader(
        "📄 Extracted Resume Text"
    )


    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )