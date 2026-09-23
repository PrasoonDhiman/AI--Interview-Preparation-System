from flask import Flask, render_template, request, jsonify

from services.question_generator import generate_questions
from services.answer_evaluator import evaluate_interview

from services.speech.speech_to_text import process_audio
from services.speech.communication_analyzer import analyze_communication
from services.speech.llm_communication_evaluator import evaluate_communication

import os


app = Flask(__name__)


questions = []
answers = []
durations = []
communication_reports = []

current_question = 0


role_selected = ""
difficulty_selected = ""


UPLOAD_FOLDER = "uploads/audio"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/start")
def start():
    return render_template("role_selection.html")



@app.route("/interview", methods=["POST"])
def interview():

    global questions
    global answers
    global durations
    global communication_reports
    global current_question
    global role_selected
    global difficulty_selected


    role_selected = request.form.get("role")
    difficulty_selected = request.form.get("difficulty")


    questions = generate_questions(
        role_selected,
        difficulty_selected
    )


    answers = []
    durations = []
    communication_reports = []

    current_question = 0


    return render_template(
        "interview.html",
        question=questions[current_question],
        question_number=1,
        total_questions=len(questions)
    )



@app.route("/upload_audio", methods=["POST"])
def upload_audio():

    audio = request.files.get("audio")


    if not audio:
        return jsonify({
            "error": "No audio file received."
        }), 400



    file_path = os.path.join(
        UPLOAD_FOLDER,
        audio.filename
    )


    audio.save(file_path)


    result = process_audio(file_path)


    return jsonify(result)





@app.route("/submit", methods=["POST"])
def submit():

    global current_question
    global answers
    global questions
    global durations
    global communication_reports


    answer = request.form.get("answer")


    duration_value = request.form.get("duration")


    if duration_value:
        duration = float(duration_value)
    else:
        duration = 0



    answers.append(answer)

    durations.append(duration)



    # Basic communication metrics

    communication_report = analyze_communication(
        answer,
        duration
    )


    communication_reports.append(
        communication_report
    )



    current_question += 1



    # Final interview report

    if current_question >= len(questions):


        technical_report = evaluate_interview(
            questions,
            answers
        )



        # Convert communication data into readable text

        communication_text = ""


        for index, data in enumerate(communication_reports):

            communication_text += f"""

Answer {index + 1}

Duration:
{durations[index]} seconds

Communication Metrics:

{data}

----------------------------

"""



        final_communication_report = evaluate_communication(
            communication_text
        )


        print("\nFINAL COMMUNICATION REPORT")
        print(final_communication_report)



        return render_template(
            "report.html",
            report=technical_report,
            communication_report=final_communication_report
        )




    return render_template(
        "interview.html",
        question=questions[current_question],
        question_number=current_question + 1,
        total_questions=len(questions)
    )



@app.route("/camera-analysis")
def camera_analysis():
    return render_template("camera_analysis.html")

if __name__ == "__main__":
    app.run(debug=True)