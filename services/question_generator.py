from services.groq_service import client


def generate_questions(role, difficulty):

    prompt = f"""
    You are a senior technical interviewer.

    Generate EXACTLY 10 interview questions.

    Role:
    {role}

    Difficulty:
    {difficulty}

    Requirements:
    - Return ONLY the questions.
    - No introductions.
    - No conclusions.
    - 10 questions only.
    - No answers.
    - Suitable for freshers.
    - Number the questions from 1 to 10.
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

    response = completion.choices[0].message.content

    questions = []

    for line in response.split("\n"):

        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Keep only numbered questions
        if line.startswith(
            ("1.", "2.", "3.", "4.", "5.",
             "6.", "7.", "8.", "9.", "10.")
        ):
            questions.append(line)

    return questions