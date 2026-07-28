import streamlit as st
import os

from utils.pdf_parser import extract_text_from_pdf
from utils.ats import calculate_ats_score
from utils.skills import extract_skills
from utils.career import recommend_careers

from database.db_operations import (
    save_user,
    save_skill
)


st.title("📄 Resume Analyzer")


uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)



if uploaded_file:


    st.success(
        "Resume uploaded successfully!"
    )



    # ---------------- EXTRACT TEXT ----------------


    resume_text = extract_text_from_pdf(
        uploaded_file
    )



    if not resume_text:

        st.error(
            "Could not extract text from resume."
        )

        st.stop()



    # ---------------- ATS SCORE ----------------


    ats_score = calculate_ats_score(
        resume_text
    )



    # ---------------- SAVE USER ----------------
    st.write(
        "Current Session User:",
        st.session_state.get("user_id", "No user")
    )

    if "user_id" not in st.session_state:


        user_id = save_user(

            name="User",

            email="user@gmail.com",

            resume_name=uploaded_file.name,

            ats_score=ats_score

        )
        st.write("Created User ID:", user_id)

        st.session_state["user_id"] = user_id



        # Save permanently

        os.makedirs(
            "database",
            exist_ok=True
        )


        with open(
            "database/current_user.txt",
            "w"
        ) as f:

            f.write(
                str(user_id)
            )



    else:


        user_id = st.session_state["user_id"]




    # Store ATS


    st.session_state["ats_score"] = ats_score



    # ---------------- ATS DISPLAY ----------------


    st.subheader(
        "🎯 ATS Score"
    )



    st.progress(
        ats_score / 100
    )



    st.metric(
        "Resume Score",
        f"{ats_score}/100"
    )



    st.divider()



    # ---------------- SKILL EXTRACTION ----------------


    skills = extract_skills(
        resume_text
    )



    # Save skills


    if "skills_saved_for_resume" not in st.session_state:


        for category, skill_list in skills.items():


            for skill in skill_list:


                save_skill(

                    user_id,

                    category,

                    skill

                )


        st.session_state["skills_saved_for_resume"] = True



    # Save for pages


    st.session_state["user_skills"] = skills

    st.session_state["resume_text"] = resume_text



    # ---------------- SKILL DISPLAY ----------------


    st.subheader(
        "🧠 Skills Analysis"
    )



    total_skills = 0



    for category, skill_list in skills.items():


        if skill_list:


            st.markdown(
                f"### {category}"
            )


            for skill in skill_list:


                total_skills += 1


                st.write(
                    "✅",
                    skill.title()
                )



    st.info(
        f"Total Skills Detected: {total_skills}"
    )



    st.divider()



    # ---------------- CAREER RECOMMENDATION ----------------


    career_results = recommend_careers(
        skills
    )



    st.session_state["career_results"] = career_results



    st.subheader(
        "🎯 Recommended Careers"
    )



    for career in career_results:


        st.markdown(
            f"### {career['career']}"
        )


        st.progress(

            career["score"]/100

        )


        st.write(

            f"Match Score: **{career['score']}%**"

        )


        st.write(

            "Matched Skills:",

            ", ".join(
                career["matched_skills"]
            )

        )


        st.divider()



    # ---------------- TEXT ----------------


    st.subheader(
        "📄 Extracted Resume Text"
    )


    st.text_area(

        "Resume Content",

        resume_text,

        height=300

    )