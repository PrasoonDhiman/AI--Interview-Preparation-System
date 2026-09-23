from services.groq_service import client


def evaluate_interview(questions, answers):

    prompt = f"""
    You are a senior technical interviewer.

    Evaluate the candidate's performance.

    QUESTIONS:

    {questions}


    ANSWERS:

    {answers}


    Give scores for:

    Technical Knowledge (30)
    Communication Skills (20)
    Problem Solving (15)
    Confidence (15)
    Clarity (10)
    Overall Performance (10)

    Also provide:

    - Strengths
    - Weaknesses
    - Suggested Topics to Study
    - Interview Readiness Percentage
    - Placement Readiness Percentage

    Give the total score out of 100.

    """

    completion = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[

            {
                "role": "user",
                "content": prompt
            }

        ]

    )

    return completion.choices[0].message.content