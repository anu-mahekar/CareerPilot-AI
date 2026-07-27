def calculate_readiness(
    ats_score,
    role_match,
    roadmap_progress,
    interview_progress
):

    readiness_score = (
        (ats_score * 0.30) +
        (role_match * 0.30) +
        (roadmap_progress * 0.25) +
        (interview_progress * 0.15)
    )

    return round(readiness_score)