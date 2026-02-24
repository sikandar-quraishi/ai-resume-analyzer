🚀 AI HR Tools Suite (Gemini Powered)

An intelligent HR automation web app built using Streamlit and Google Gemini AI that helps recruiters:

📄 Analyze resumes against job descriptions

🎤 Generate interview questions

📋 Create professional job descriptions

Built for fast, smart, AI-powered hiring workflows.

🧠 Powered By

🐍 Python

⚡ Streamlit

🤖 Google Gemini (gemini-2.5-flash)

✨ Features
1️⃣ Resume Analyzer

Compare a candidate resume with a job description and get:

🎯 Match Score (0–100%)

✅ Matched Skills

❌ Missing Skills

📌 AI Recommendation

📊 Final Status (Shortlisted / On Hold / Rejected)

Perfect for quick screening during recruitment.

2️⃣ Interview Question Generator

Generate:

5 Technical Questions

3 Behavioral Questions

Based on:

Job Role

Experience Level (Fresher / Mid-Level / Senior)

Great for structured interview preparation.

3️⃣ Job Description Generator

Automatically creates:

Role Summary

Key Responsibilities

Required Skills

Nice to Have

Helps HR teams quickly draft professional JDs.

📦 Project Structure
ai-hr-tools/
│
├── app.py
├── README.md
└── .streamlit/
    └── secrets.toml
🔑 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-hr-tools.git
cd ai-hr-tools
2️⃣ Install Dependencies
pip install streamlit google-generativeai
3️⃣ Add Gemini API Key

Create a file:

.streamlit/secrets.toml

Add:

GEMINI_API_KEY = "your_api_key_here"

You can get your API key from Google AI Studio.

4️⃣ Run the App
streamlit run app.py

App will run at:

http://localhost:8501
🖥️ Demo Flow (For Presentation)

Here’s a smooth demo flow you can follow:

🔹 Step 1 – Resume Analyzer

Paste a sample job description

Paste a sample resume

Click Analyze Resume

Show:

Match Score

Skill comparison

Status decision

👉 Explain how this reduces manual screening time.

🔹 Step 2 – Interview Question Generator

Enter role: "Python Developer"

Select experience: "Mid-Level"

Generate questions

Highlight technical + behavioral separation

👉 Explain structured interview benefits.

🔹 Step 3 – Job Description Generator

Select role

Select experience level

Generate JD

👉 Show how it speeds up HR documentation.

🎯 Use Cases

HR Teams

Recruitment Agencies

Startup Hiring

Technical Screening Automation

Internal Talent Evaluation

🔒 Error Handling

API key validation

Safe JSON parsing

Graceful failure if AI response format changes

🚀 Future Improvements

PDF resume upload support

Candidate database storage

Email integration

Admin dashboard

Download report as PDF

Multi-model support

🧑‍💻 Author

Developed as an AI-powered HR automation solution using Streamlit + Gemini.
