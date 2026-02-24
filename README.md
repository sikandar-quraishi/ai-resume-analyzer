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

- Python  
- Streamlit  
- Google Gemini (gemini-2.5-flash)  
- Streamlit Cloud (Deployment)

---

## 📂 Project Structure

```
ai-hr-tools/
│
├── app.py
├── README.md
└── .streamlit/
    └── secrets.toml
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

## 🌐 Live Deployment

Deployed using **Streamlit Cloud**.  
(Add your live app link here)

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

- HR Teams  
- Recruitment Agencies  
- Startups  
- Technical Hiring Teams  
- Talent Screening  

---

## 🔒 Security

- Secure API key using Streamlit secrets
- Safe JSON parsing
- Graceful handling of AI response errors

---

## 🚀 Future Improvements

- PDF Resume Upload Support
- Candidate Database
- Downloadable Reports
- Admin Dashboard
- Email Integration

---

## 👨‍💻 Author

Developed as an AI-powered recruitment automation solution using Streamlit and Google Gemini.
