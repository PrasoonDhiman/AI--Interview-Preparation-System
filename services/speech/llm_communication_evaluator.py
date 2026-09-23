from services.groq_service import client



def evaluate_communication(communication_data):


    prompt = f"""

You are a professional interview communication coach.

Analyze the candidate's complete interview communication.

Here is the communication data:

{communication_data}


Generate a final communication analysis report.

The report MUST include:


1. Overall Communication Score (0-100)

2. Speaking Speed Analysis

3. Confidence Level

4. Clarity of Explanation

5. Vocabulary Usage

6. Grammar and Sentence Structure

7. Strengths

8. Weaknesses

9. Improvement Suggestions

10. Interview Communication Readiness Percentage


Give detailed but concise feedback.

Do not return an empty response.

"""


    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],



        temperature=0.5
    )


    return response.choices[0].message.content