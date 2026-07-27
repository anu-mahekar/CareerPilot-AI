def evaluate_answer(question, answer):

    keywords = {

        "machine learning": [
            "data",
            "algorithm",
            "model",
            "training",
            "prediction",
            "patterns"
        ],

        "artificial intelligence": [
            "machine",
            "human",
            "intelligence",
            "decision",
            "automation"
        ],

        "nlp": [
            "text",
            "language",
            "processing",
            "token",
            "model"
        ],

        "neural networks": [
            "neurons",
            "layers",
            "weights",
            "activation",
            "training"
        ],

        "sql": [
            "database",
            "query",
            "table",
            "join",
            "data"
        ]

    }


    question_lower = question.lower()

    answer_lower = answer.lower()



    matched_keywords = []

    missing_keywords = []



    selected_keywords = []



    for topic, words in keywords.items():

        if topic in question_lower:

            selected_keywords = words

            break



    if selected_keywords:


        for word in selected_keywords:

            if word in answer_lower:

                matched_keywords.append(word)

            else:

                missing_keywords.append(word)



        score = int(
            (len(matched_keywords) /
            len(selected_keywords)) * 10
        )


    else:

        if len(answer.split()) > 30:

            score = 8

        elif len(answer.split()) > 10:

            score = 6

        else:

            score = 4



    if score >= 8:

        feedback = "Excellent answer with good technical coverage."


    elif score >= 5:

        feedback = "Good answer. Add more technical concepts."


    else:

        feedback = "Answer needs more explanation and examples."



    return {

        "score": score,

        "feedback": feedback,

        "covered": matched_keywords,

        "missing": missing_keywords

    }