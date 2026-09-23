# AI Interview Preparation System

An AI-powered **Multimodal Adaptive Mock Interview System** developed using Python, Flask, Groq API, and MediaPipe. The platform simulates real technical interviews by generating role-specific questions, evaluating candidate responses, analyzing communication through audio and webcam input, and generating comprehensive performance reports.

The system combines Large Language Models (LLMs), speech processing, and computer vision to provide an interactive and intelligent interview preparation experience.

## 🚀 Key Features

### 1. AI-Based Question Generation
- Generates interview questions using Groq API.
- Supports multiple technical roles:
  - Software Developer
  - Frontend Developer
  - Backend Developer
  - Full Stack Developer
  - Machine Learning Engineer
  - Data Analyst
- Supports Easy, Medium, and Hard difficulty levels.
- Generates 10 questions per interview session.

### 2. Intelligent Answer Evaluation
Evaluates candidate answers using AI and six weighted parameters:

| Evaluation Parameter | Weight |
|---|---:|
| Technical Knowledge | 30% |
| Communication | 20% |
| Problem Solving | 15% |
| Confidence | 15% |
| Clarity | 10% |
| Overall Performance | 10% |
| **Total** | **100%** |

Provides:
- Performance scores
- Strengths and weaknesses
- Recommended study topics
- Interview readiness assessment

### 3. Speech Recognition and Audio Analysis
- Supports audio-based interview responses.
- Uses Groq-powered speech transcription.
- Converts spoken answers into text.
- Integrates audio processing for interview analysis.

### 4. Webcam-Based Facial and Communication Analysis
- Uses MediaPipe for facial landmark detection.
- Analyzes webcam-based visual indicators.
- Supports facial expression and communication analysis.
- Integrates visual analysis into the multimodal interview workflow.

### 5. Automated Interview Reports
- Generates comprehensive interview performance reports.
- Provides an overall performance summary.
- Highlights strengths and weaknesses.
- Recommends areas for improvement.
- Supports PDF report generation.

## 🧠 System Workflow

```text
       User Registration / Login
                 |
                 v
          Select Interview Role
                 |
                 v
       Choose Difficulty Level
                 |
                 v
        AI Question Generation
             (Groq API)
                 |
                 v
          Interview Session
                 |
        +--------+--------+
        |                 |
        v                 v
   Text Answers      Audio Answers
        |                 |
        |            Speech-to-Text
        |                 |
        +--------+--------+
                 |
                 v
        AI Answer Evaluation
                 |
                 v
       Webcam-Based Analysis
             (MediaPipe)
                 |
                 v
       Performance Assessment
                 |
                 v
        Final Interview Report
                 |
                 v
          PDF Report Export
```

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| AI Integration | Groq API |
| Language Models | LLM-based evaluation |
| Speech Recognition | Groq transcription |
| Audio Processing | Librosa, SoundDevice, SoundFile |
| Computer Vision | MediaPipe, OpenCV |
| Facial Analysis | MediaPipe Face Landmarker |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLAlchemy / SQLite |
| Data Visualization | Matplotlib |
| PDF Generation | PDF reporting library |

## 📁 Project Structure

```text
AI_Prep/
│
├── app.py
│
├── database/
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── routes/
│
├── services/
│   ├── answer_evaluator.py
│   ├── groq_service.py
│   ├── question_generator.py
│   │
│   ├── camera_analysis/
│   └── speech/
│
├── static/
│
├── templates/
│   ├── camera_analysis.html
│   ├── dashboard.html
│   ├── index.html
│   ├── interview.html
│   ├── login.html
│   ├── register.html
│   ├── report.html
│   └── role_selection.html
│
├── uploads/
├── reports/
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or compatible version
- Git
- Webcam
- Microphone
- Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/PrasoonDhiman/AI-Interview-Preparation-System.git
```

### 2. Navigate to the Project

```bash
cd AI-Interview-Preparation-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key
```

Never upload your actual `.env` file or API keys to GitHub.

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

## 🎯 Applications

- Technical interview preparation
- Placement training
- College and university training programs
- Skill assessment
- Communication improvement
- Mock interview practice
- Self-assessment and career preparation

## 🔮 Future Enhancements

- Adaptive question difficulty based on candidate performance.
- Advanced emotion and engagement analysis.
- Real-time interview feedback.
- Resume-based personalized interview questions.
- Multi-language interview support.
- Integration with job portals.
- Advanced candidate performance analytics.

## 🔐 Security and Privacy

- API credentials are stored using environment variables.
- User authentication protects individual accounts.
- Audio recordings and generated reports should be handled securely.
- Private user data and database files should not be published in the public repository.

## 👨‍💻 Developer

**Prasoon Kumar Dhiman**

B.Tech – Computer Science and Engineering

Government Post Graduate College, Dharamshala

---

⭐ If you find this project useful, consider giving the repository a star!