def evaluate_answer(question, answer):

    answer_length = len(answer.split())


    if answer_length < 10:

        score = 4

        feedback = "Answer is too short. Add more technical explanation."

    elif answer_length < 30:

        score = 7

        feedback = "Good explanation. Add examples and concepts."

    else:

        score = 9

        feedback = "Excellent explanation with good details."


    return {
        "score": score,
        "feedback": feedback
    }