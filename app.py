import streamlit as st
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.markdown("### AI-Powered Resume Matching System")

def extract_skills(text):
    # Simple skill extraction (customize if needed)
    common_skills = [
        "react", "javascript", "redux", "rest", "api",
        "node", "typescript", "git", "html", "css",
        "python", "django", "sql", "aws", "docker"
    ]
    
    found = []
    text_lower = text.lower()
    
    for skill in common_skills:
        if skill in text_lower:
            found.append(skill.capitalize())
    
    return set(found)

def analyze_resume(job_desc, resume):
    job_skills = extract_skills(job_desc)
    resume_skills = extract_skills(resume)
    
    matched = job_skills.intersection(resume_skills)
    missing = job_skills.difference(resume_skills)
    
    if len(job_skills) == 0:
        match_percent = 0
    else:
        match_percent = int((len(matched) / len(job_skills)) * 100)
    
    return match_percent, matched, missing

col1, col2 = st.columns(2)

with col1:
    job_desc = st.text_area("📄 Job Description", height=300)

with col2:
    resume = st.text_area("📑 Resume", height=300)

if st.button("Analyze Resume"):
    if not job_desc or not resume:
        st.warning("⚠️ Please fill both fields.")
    else:
        match_percent, matched, missing = analyze_resume(job_desc, resume)
        
        st.success("✅ Analysis Complete")
        
        st.markdown(f"## 🎯 Match Score: {match_percent}%")
        
        st.markdown("### ✅ Matching Skills")
        if matched:
            for skill in matched:
                st.write(f"- {skill}")
        else:
            st.write("No matching skills found.")
        
        st.markdown("### ❌ Missing Skills")
        if missing:
            for skill in missing:
                st.write(f"- {skill}")
        else:
            st.write("No missing skills. Great match!")
        
        st.markdown("### 🧠 AI Recommendation")
        if match_percent > 80:
            st.write("Strong candidate. Highly recommended.")
        elif match_percent > 50:
            st.write("Moderate match. Consider shortlisting.")
        else:
            st.write("Low match. Needs skill improvement.")
