import streamlit as st
import io

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter



# ==================================================
# PDF GENERATOR
# ==================================================

def generate_pdf():

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=18,
        spaceAfter=20
    )


    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10
    )


    normal_style = styles["Normal"]


    content = []


    # ---------------- TITLE ----------------

    content.append(
        Paragraph(
            "CareerPilot-AI Career Report",
            title_style
        )
    )



    # ---------------- SKILLS ----------------

    content.append(
        Paragraph(
            "Your Skills",
            heading_style
        )
    )


    for category, skill_list in skills.items():

        content.append(
            Paragraph(
                category,
                normal_style
            )
        )


        content.append(
            Paragraph(
                ", ".join(skill_list),
                normal_style
            )
        )


        content.append(
            Spacer(1,10)
        )



    # ---------------- ATS SCORE ----------------

    content.append(
        Paragraph(
            "ATS Score",
            heading_style
        )
    )


    content.append(
        Paragraph(
            f"Resume Score: {ats_score}/100",
            normal_style
        )
    )



    # ---------------- CAREER RECOMMENDATIONS ----------------

    content.append(
        Paragraph(
            "Recommended Careers",
            heading_style
        )
    )


    career_data = [
        [
            "Career",
            "Match Score"
        ]
    ]


    for career in career_results:

        career_data.append(
            [
                career["career"],
                f"{career['score']}%"
            ]
        )


    career_table = Table(
        career_data,
        colWidths=[250,100]
    )


    career_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    None
                ),

                (
                    "ALIGN",
                    (1,1),
                    (-1,-1),
                    "CENTER"
                )
            ]
        )
    )


    content.append(
        career_table
    )



    # ---------------- TARGET ROLE ----------------


    if "target_role_result" in st.session_state:


        result = st.session_state["target_role_result"]


        content.append(
            Paragraph(
                "Target Role Analysis",
                heading_style
            )
        )


        content.append(
            Paragraph(
                f"""
                Role: {result['role']}<br/>
                Match Score: {result['score']}%<br/>
                Profile Strength: {result['strength']}
                """,
                normal_style
            )
        )



        # Strengths

        content.append(
            Paragraph(
                "Your Strengths",
                heading_style
            )
        )


        for skill in result["matched_skills"]:

            content.append(
                Paragraph(
                    skill.title(),
                    normal_style
                )
            )



        # Skill Gap

        content.append(
            Paragraph(
                "Skills To Improve",
                heading_style
            )
        )


        if result["missing_skills"]:

            for skill in result["missing_skills"]:

                content.append(
                    Paragraph(
                        skill.title(),
                        normal_style
                    )
                )

        else:

            content.append(
                Paragraph(
                    "No skill gaps found",
                    normal_style
                )
            )



    # ---------------- LEARNING PROGRESS ----------------


    if "roadmap_progress" in st.session_state:


        content.append(
            Paragraph(
                "Learning Progress",
                heading_style
            )
        )


        for role, completed in st.session_state["roadmap_progress"].items():

            content.append(
                Paragraph(
                    f"{role}: Completed {len(completed)} skills",
                    normal_style
                )
            )



    doc.build(content)


    buffer.seek(0)

    return buffer





# ==================================================
# PAGE UI
# ==================================================


st.title("📄 CareerPilot-AI Report")


st.write(
    "Generate your personalized career analysis report."
)



# Check resume upload

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload your resume in Resume Analyzer first."
    )

    st.stop()



skills = st.session_state["user_skills"]



ats_score = st.session_state.get(
    "ats_score",
    0
)



career_results = st.session_state.get(
    "career_results",
    []
)



# ---------------- DISPLAY SKILLS ----------------


st.subheader(
    "🧠 Your Skills"
)


for category, skill_list in skills.items():

    st.write(
        f"### {category}"
    )


    for skill in skill_list:

        st.write(
            "✅",
            skill.title()
        )



st.divider()



# ---------------- ATS ----------------


st.subheader(
    "🎯 ATS Score"
)


st.write(
    f"Resume Score: **{ats_score}/100**"
)



st.divider()



# ---------------- CAREERS ----------------


st.subheader(
    "🚀 Recommended Careers"
)


for career in career_results:

    st.write(
        f"### {career['career']}"
    )


    st.write(
        f"Match Score: **{career['score']}%**"
    )



st.divider()



# ---------------- TARGET ROLE ----------------


if "target_role_result" in st.session_state:


    result = st.session_state["target_role_result"]


    st.subheader(
        "🎯 Target Role Analysis"
    )


    st.write(
        f"Role: **{result['role']}**"
    )


    st.write(
        f"Match Score: **{result['score']}%**"
    )


    st.write(
        f"Profile Strength: **{result['strength']}**"
    )



    st.subheader(
        "💪 Your Strengths"
    )


    for skill in result["matched_skills"]:

        st.write(
            "✅",
            skill.title()
        )



    st.subheader(
        "📚 Skill Gap Analysis"
    )


    if result["missing_skills"]:

        for skill in result["missing_skills"]:

            st.write(
                "❌",
                skill.title()
            )

    else:

        st.success(
            "No skill gaps found"
        )



# ---------------- DOWNLOAD ----------------


st.divider()


st.subheader(
    "📥 Download Report"
)


pdf = generate_pdf()


st.download_button(
    label="Download CareerPilot-AI Report PDF",
    data=pdf,
    file_name="CareerPilot_AI_Report.pdf",
    mime="application/pdf"
)


st.success(
    "🎉 Your CareerPilot-AI report is ready!"
)