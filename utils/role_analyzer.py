from utils.career import recommend_careers
from utils.skill_gap import calculate_skill_gap


def analyze_role_match(skill_categories, target_role):

    # Get career scores
    careers = recommend_careers(skill_categories)


    for career in careers:

        if career["career"] == target_role:


            # Calculate missing skills
            missing_skills = calculate_skill_gap(
                skill_categories,
                target_role
            )


            # Determine profile strength
            score = career["score"]


            if score >= 80:
                strength = "Excellent Match"

            elif score >= 60:
                strength = "Good Foundation"

            else:
                strength = "Needs Improvement"



            # Extract missing skill names
            missing = []

            learning = []


            for skill in missing_skills:

                missing.append(
                    skill["name"]
                )


                learning.append(
                    {
                        "skill": skill["name"],
                        "why": skill["why"],
                        "learn": skill["learn"]
                    }
                )



            return {

                "role": target_role,

                "score": score,

                "strength": strength,


                "matched_skills": career[
                    "matched_skills"
                ],


                "missing_skills": missing,


                "learning_plan": learning

            }



    # If role not found

    return {

        "role": target_role,

        "score": 0,

        "strength": "No Match Found",

        "matched_skills": [],

        "missing_skills": [],

        "learning_plan": []

    }