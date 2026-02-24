# 🚀 AI HR Tools Suite (Gemini Powered)

An intelligent **AI-powered HR automation web application** built using **Streamlit** and **Google Gemini AI**.

This platform helps recruiters automate and streamline hiring workflows efficiently.

---

## 🌟 Features

### 📄 Resume Analyzer
Compare a candidate's resume with a job description and get:

- 🎯 Match Score (0–100%)
- ✅ Matched Skills
- ❌ Missing Skills
- 📌 AI Recommendation
- 📊 Final Status (Shortlisted / On Hold / Rejected)

---

### 🎤 Interview Question Generator
Generate structured interview questions based on:

- Job Role
- Experience Level (Fresher / Mid-Level / Senior)

Includes:
- 5 Technical Questions  
- 3 Behavioral Questions  

---

### 📋 Job Description Generator
Automatically creates:

- Role Summary
- Key Responsibilities
- Required Skills
- Nice-to-Have Skills

---

## 🧠 Tech Stack

- **Python**  
  Used as the core programming language to handle application logic, API integration, and data processing.  

- **Streamlit**  
  Used to build the interactive web interface quickly without complex frontend frameworks.  
  It allows rapid development of user-friendly AI applications with minimal code.

- **Google Gemini (gemini-2.5-flash)**  
  Powers the AI capabilities of the application through prompt-based content generation.  
  It analyzes resumes, generates interview questions, and creates job descriptions intelligently.

- **Streamlit Cloud**  
  Used to deploy and host the application online for easy access.  
  It allows seamless integration with GitHub and automatic updates on code changes.

---

## 📂 Project Structure

```
ai-hr-tools/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-hr-tools.git
cd ai-hr-tools
```

### 2️⃣ Install Dependencies

```bash
pip install streamlit google-generativeai
```

### 3️⃣ Configure Gemini API Key

Create a file:

```
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

⚠️ Do NOT upload your API key to GitHub.

---

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

The app runs at:

```
http://localhost:8501
```

---

## 🌐 Live Demo

🔗 **Live App:** https://ai-resume-analyzer-mnhb6erjp4qwnhr7gepvjw.streamlit.app/

---

## 🖥️ Demo Flow

### Step 1 – Resume Analyzer
- Paste job description  
- Paste resume  
- Click Analyze Resume  
- Show match score and hiring decision  

### Step 2 – Interview Question Generator
- Enter role  
- Select experience  
- Generate questions  

### Step 3 – Job Description Generator
- Select role  
- Generate professional JD  

---

## 🎯 Use Cases

- Faster candidate screening for HR teams  
- Quick generation of professional job descriptions  
- Skill gap analysis between job roles and resumes  
- AI-assisted hiring decision support  
- Role-based technical and behavioural interview questions  

---

## 👨‍💻 Author

Developed as an AI-powered recruitment automation solution using Streamlit and Google Gemini.
