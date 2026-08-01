import streamlit as st
from datetime import datetime


st.title("✍ Cover Letter Generator")

st.write(
    "Generate a personalized cover letter using your resume skills and target role."
)


# Check resume data

if "user_skills" not in st.session_state:

    st.warning(
        "Please upload and analyze your resume first."
    )

    st.stop()



skills = st.session_state["user_skills"]


# Flatten skills

all_skills = []

for category, skill_list in skills.items():

    for skill in skill_list:

        all_skills.append(skill.title())



# User Inputs

st.subheader("📝 Job Details")


company = st.text_input(
    "Company Name",
    placeholder="Example: Google"
)


role = st.text_input(
    "Job Role",
    value=st.session_state.get(
        "selected_role",
        "AI Engineer"
    )
)


job_description = st.text_area(
    "Job Description (Optional)",
    placeholder="Paste job requirements here..."
)



# Generate Button

if st.button("🚀 Generate Cover Letter"):


    name = st.session_state.get(
        "name",
        "Anusha"
    )


    skill_text = ", ".join(
        all_skills[:10]
    )


    cover_letter = f"""

Dear Hiring Manager,


I am excited to apply for the position of {role} at {company}.


I am currently pursuing my Bachelor's degree in Artificial Intelligence and Machine Learning and have hands-on experience in developing AI-driven applications and machine learning solutions.


My technical skills include {skill_text}. I have worked on projects involving machine learning, data analysis, computer vision, and web-based AI applications.


Through my academic projects, I have gained practical experience in Python, machine learning frameworks, data processing, and developing end-to-end solutions. I am passionate about applying artificial intelligence to solve real-world problems and continuously improving my technical skills.


I believe my combination of AI knowledge, problem-solving ability, and project experience makes me a strong candidate for this role.


Thank you for considering my application. I look forward to the opportunity to discuss how my skills and enthusiasm can contribute to {company}.


Sincerely,

{name}

"""


    st.session_state["cover_letter"] = cover_letter



# Display

if "cover_letter" in st.session_state:


    st.divider()

    st.subheader(
        "📄 Generated Cover Letter"
    )


    st.text_area(
        "Cover Letter",
        st.session_state["cover_letter"],
        height=400
    )


    st.download_button(
        label="📥 Download Cover Letter",
        data=st.session_state["cover_letter"],
        file_name="CareerPilot_Cover_Letter.txt",
        mime="text/plain"
    )


    st.success(
        "🎉 Cover letter generated successfully!"
    )