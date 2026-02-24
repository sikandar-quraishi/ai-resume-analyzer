import streamlit as st
import google.generativeai as genai
import json
import re

# ------------------------------------------------
# CONFIGURATION
# ------------------------------------------------

st.set_page_config(page_title="AI HR Tools Suite", layout="wide")

# Configure Gemini API
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    st.error("Gemini API Key not configured properly.", e)
    st.stop()

# ------------------------------------------------
# COMMON LLM FUNCTION
# ------------------------------------------------

def call_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"


# ------------------------------------------------
# JSON SAFE PARSER
# ------------------------------------------------

def extract_json(text):
    try:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return None
    except:
        return None


# ------------------------------------------------
# APP TITLE
# ------------------------------------------------

st.title("🚀 AI HR Tools Suite (Gemini Powered)")

menu = st.sidebar.selectbox(
    "Select AI Tool",
    [
        "Resume Analyzer",
        "Interview Question Generator",
        "Job Description Generator"
    ]
)

# =====================================================
# 1️⃣ Resume Analyzer
# =====================================================

if menu == "Resume Analyzer":

    st.header("📄 AI Resume Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        job_desc = st.text_area("Job Description", height=300)

    with col2:
        resume = st.text_area("Candidate Resume", height=300)

    if st.button("Analyze Resume"):

        if not job_desc or not resume:
            st.warning("Please fill both fields.")
        else:
            with st.spinner("Analyzing Resume with AI..."):

                prompt = f"""
                You are an expert HR AI.

                Compare the following job description and resume.

                Return response STRICTLY in JSON format:

                {{
                    "match_score": number (0-100),
                    "matched_skills": [],
                    "missing_skills": [],
                    "recommendation": "",
                    "status": "Shortlisted / On Hold / Rejected"
                }}

                Job Description:
                {job_desc}

                Resume:
                {resume}
                """

                result = call_llm(prompt)
                data = extract_json(result)

                if data:

                    st.success("Analysis Complete")

                    st.markdown(f"# 🎯 Match Score: {data['match_score']}%")
                    st.progress(int(data["match_score"]))

                    colA, colB = st.columns(2)
                    colA.metric("Status", data["status"])
                    colB.metric("Recommendation", data["recommendation"])

                    st.markdown("### ✅ Matched Skills")
                    for skill in data["matched_skills"]:
                        st.write(f"- {skill}")

                    st.markdown("### ❌ Missing Skills")
                    for skill in data["missing_skills"]:
                        st.write(f"- {skill}")

                else:
                    st.error("AI returned unexpected format.")
                    st.write(result)


# =====================================================
# 2️⃣ Interview Question Generator
# =====================================================

elif menu == "Interview Question Generator":

    st.header("🎤 AI Interview Question Generator")

    role = st.text_input("Enter Job Role")
    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"]
    )

    if st.button("Generate Questions"):

        if not role:
            st.warning("Please enter job role.")
        else:
            with st.spinner("Generating Questions..."):

                prompt = f"""
                Generate interview questions for:

                Role: {role}
                Experience Level: {experience}

                Provide:
                - 5 Technical Questions
                - 3 Behavioral Questions
                """

                result = call_llm(prompt)
                st.success("Questions Generated")
                st.markdown(result)


# =====================================================
# 3️⃣ Job Description Generator
# =====================================================

elif menu == "Job Description Generator":

    st.header("📋 AI Job Description Generator")

    role = st.selectbox(
        "Select Job Role",
        [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Python Developer",
            "Node.js Developer"
        ]
    )

    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"]
    )

    if st.button("Generate Job Description"):

        with st.spinner("Generating Job Description..."):

            prompt = f"""
            Create a professional job description.

            Role: {role}
            Experience Level: {experience}

            Include:
            - Role Summary
            - Key Responsibilities
            - Required Skills
            - Nice to Have
            """

            result = call_llm(prompt)
            st.success("Job Description Generated")
            st.markdown(result)

