def calculate_readiness(
    ats_score=0,
    role_match=0,
    roadmap_progress=0,
    interview_progress=0
):

    # Avoid None values
    ats_score = ats_score or 0
    role_match = role_match or 0
    roadmap_progress = roadmap_progress or 0
    interview_progress = interview_progress or 0


    readiness_score = (
        (ats_score * 0.30) +
        (role_match * 0.30) +
        (roadmap_progress * 0.25) +
        (interview_progress * 0.15)
    )


    return round(readiness_score)