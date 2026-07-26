import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Main title
st.title("🚀 CareerPilot AI")

st.subheader("Your Personal AI Career Mentor")

st.write(
    """
    CareerPilot AI helps students and job seekers improve their career journey.

    Features coming soon:

    📄 Resume Analysis  
    🎯 Career Recommendations  
    📚 Skill Gap Analysis  
    🛣 Personalized Learning Roadmap  
    🎤 Interview Preparation  
    ✍ Cover Letter Generation
    """
)

st.divider()

st.info(
    "Upload your resume and let AI guide your career growth!"
)