# import streamlit as st
# import re

# st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# st.title("🚀 AI Resume Analyzer (POC)")
# st.markdown("### AI-Powered Resume Matching System")

# def extract_skills(text):
#     # Simple skill extraction (customize if needed)
#     common_skills = [
#         "react", "javascript", "redux", "rest", "api",
#         "node", "typescript", "git", "html", "css",
#         "python", "django", "sql", "aws", "docker"
#     ]
    
#     found = []
#     text_lower = text.lower()
    
#     for skill in common_skills:
#         if skill in text_lower:
#             found.append(skill.capitalize())
    
#     return set(found)

# def analyze_resume(job_desc, resume):
#     job_skills = extract_skills(job_desc)
#     resume_skills = extract_skills(resume)
    
#     matched = job_skills.intersection(resume_skills)
#     missing = job_skills.difference(resume_skills)
    
#     if len(job_skills) == 0:
#         match_percent = 0
#     else:
#         match_percent = int((len(matched) / len(job_skills)) * 100)
    
#     return match_percent, matched, missing

# col1, col2 = st.columns(2)

# with col1:
#     job_desc = st.text_area("📄 Job Description", height=300)

# with col2:
#     resume = st.text_area("📑 Resume", height=300)

# if st.button("Analyze Resume"):
#     if not job_desc or not resume:
#         st.warning("⚠️ Please fill both fields.")
#     else:
#         match_percent, matched, missing = analyze_resume(job_desc, resume)
        
#         st.success("✅ Analysis Complete")
        
#         st.markdown(f"## 🎯 Match Score: {match_percent}%")
        
#         st.markdown("### ✅ Matching Skills")
#         if matched:
#             for skill in matched:
#                 st.write(f"- {skill}")
#         else:
#             st.write("No matching skills found.")
        
#         st.markdown("### ❌ Missing Skills")
#         if missing:
#             for skill in missing:
#                 st.write(f"- {skill}")
#         else:
#             st.write("No missing skills. Great match!")
        
#         st.markdown("### 🧠 AI Recommendation")
#         if match_percent > 80:
#             st.write("Strong candidate. Highly recommended.")
#         elif match_percent > 50:
#             st.write("Moderate match. Consider shortlisting.")
#         else:
#             st.write("Low match. Needs skill improvement.")



# import streamlit as st

# st.set_page_config(page_title="AI HR Tools Suite", layout="wide")

# st.title("🚀 AI HR Tools Suite (POC Project)")

# # Sidebar Navigation
# menu = st.sidebar.selectbox(
#     "Select AI Tool",
#     ["Resume Analyzer", "Interview Question Generator"]
# )

# # ---------------------------------------------
# # COMMON SKILL LOGIC
# # ---------------------------------------------

# def extract_skills(text):
#     common_skills = [
#         "react", "javascript", "redux", "rest", "api",
#         "node", "typescript", "git", "html", "css",
#         "python", "django", "sql", "aws", "docker"
#     ]

#     found = []
#     text_lower = text.lower()

#     for skill in common_skills:
#         if skill in text_lower:
#             found.append(skill.capitalize())

#     return set(found)


# def analyze_resume(job_desc, resume):
#     job_skills = extract_skills(job_desc)
#     resume_skills = extract_skills(resume)

#     matched = job_skills.intersection(resume_skills)
#     missing = job_skills.difference(resume_skills)

#     if len(job_skills) == 0:
#         match_percent = 0
#     else:
#         match_percent = int((len(matched) / len(job_skills)) * 100)

#     return match_percent, matched, missing


# # ---------------------------------------------
# # POC 1 - Resume Analyzer
# # ---------------------------------------------

# if menu == "Resume Analyzer":

#     st.header("📄 Resume Analyzer")

#     col1, col2 = st.columns(2)

#     with col1:
#         job_desc = st.text_area("Job Description", height=250)

#     with col2:
#         resume = st.text_area("Resume", height=250)

#     if st.button("Analyze Resume"):
#         if not job_desc or not resume:
#             st.warning("Please fill both fields.")
#         else:
#             match_percent, matched, missing = analyze_resume(job_desc, resume)

#             st.success("Analysis Complete")
#             st.markdown(f"## 🎯 Match Score: {match_percent}%")

#             st.markdown("### ✅ Matching Skills")
#             for skill in matched:
#                 st.write(f"- {skill}")

#             st.markdown("### ❌ Missing Skills")
#             for skill in missing:
#                 st.write(f"- {skill}")

#             st.markdown("### 🧠 Recommendation")

#             if match_percent > 80:
#                 st.success("Strong candidate. Highly recommended.")
#             elif match_percent > 50:
#                 st.info("Moderate match. Consider shortlisting.")
#             else:
#                 st.error("Low match. Needs skill improvement.")


# # ---------------------------------------------
# # POC 2 - Interview Question Generator
# # ---------------------------------------------

# elif menu == "Interview Question Generator":

#     st.header("🎤 Interview Question Generator")

#     role = st.text_input("Enter Job Role (e.g., React Developer)")
#     experience = st.selectbox(
#         "Experience Level",
#         ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"]
#     )

#     if st.button("Generate Questions"):

#         if not role:
#             st.warning("Please enter job role.")
#         else:
#             st.success("Questions Generated")

#             st.markdown("### 🧠 Technical Questions")

#             st.write(f"1. Explain core concepts of {role}.")
#             st.write(f"2. What are best practices in {role}?")
#             st.write(f"3. Describe a challenging project in {role}.")
#             st.write(f"4. How do you optimize performance in {role}?")
#             st.write(f"5. What tools are commonly used in {role}?")

#             st.markdown("### 🤝 Behavioral Questions")

#             st.write("1. Describe a conflict you handled in a team.")
#             st.write("2. How do you manage deadlines?")
#             st.write("3. How do you keep learning new technologies?")

import streamlit as st

st.set_page_config(page_title="AI HR Tools Suite", layout="wide")

st.title("🚀 AI HR Tools Suite (POC Project)")

menu = st.sidebar.selectbox(
    "Select AI Tool",
    ["Resume Analyzer", "Interview Question Generator"]
)

# ---------------------------------------------
# COMMON SKILL LOGIC
# ---------------------------------------------

common_skills = [
    "react", "javascript", "redux", "rest", "api",
    "node", "typescript", "git", "html", "css",
    "python", "django", "sql", "aws", "docker"
]

def extract_skills(text):
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

# ---------------------------------------------
# POC 1 - Resume Analyzer
# ---------------------------------------------

if menu == "Resume Analyzer":

    st.header("📄 Resume Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        job_desc = st.text_area("Job Description", height=250)

    with col2:
        resume = st.text_area("Resume", height=250)

    if st.button("Analyze Resume"):
        if not job_desc or not resume:
            st.warning("Please fill both fields.")
        else:
            match_percent, matched, missing = analyze_resume(job_desc, resume)

            st.success("Analysis Complete")
            st.markdown(f"## 🎯 Match Score: {match_percent}%")

            st.markdown("### ✅ Matching Skills")
            for skill in matched:
                st.write(f"- {skill}")

            st.markdown("### ❌ Missing Skills")
            for skill in missing:
                st.write(f"- {skill}")

            st.markdown("### 🧠 Recommendation")

            if match_percent > 80:
                st.success("Strong candidate. Highly recommended.")
            elif match_percent > 50:
                st.info("Moderate match. Consider shortlisting.")
            else:
                st.error("Low match. Needs skill improvement.")


# ---------------------------------------------
# POC 2 - Interview Question + Answer Evaluator
# ---------------------------------------------

elif menu == "Interview Question Generator":

    st.header("🎤 Interview Question Generator + Answer Evaluator")

    role = st.text_input("Enter Job Role (e.g., React Developer)")

    if st.button("Generate Question"):

        if not role:
            st.warning("Please enter job role.")
        else:
            st.success("Question Generated")

            # Sample React Question Template
            question = f"What is Virtual DOM in {role} and how does it improve performance?"
            expected_keywords = ["virtual dom", "real dom", "diff", "performance", "update"]

            st.markdown("### 🧠 Technical Question")
            st.write(question)

            st.markdown("### ✅ Expected Key Concepts (For HR Reference)")
            for word in expected_keywords:
                st.write(f"- {word.capitalize()}")

            # Store expected keywords in session
            st.session_state.expected_keywords = expected_keywords
            st.session_state.question_generated = True

    # Answer Evaluation Section
    if st.session_state.get("question_generated"):

        st.markdown("### ✍️ Enter Candidate Answer")
        candidate_answer = st.text_area("Candidate Answer", height=200)

        if st.button("Evaluate Answer"):

            if not candidate_answer:
                st.warning("Please enter candidate answer.")
            else:
                answer_lower = candidate_answer.lower()
                expected_keywords = st.session_state.expected_keywords

                matched = [kw for kw in expected_keywords if kw in answer_lower]
                score = int((len(matched) / len(expected_keywords)) * 100)

                st.markdown(f"## 🎯 Answer Score: {score}%")

                st.markdown("### ✅ Concepts Covered")
                for m in matched:
                    st.write(f"- {m}")

                missing = set(expected_keywords) - set(matched)

                st.markdown("### ❌ Missing Concepts")
                for m in missing:
                    st.write(f"- {m}")

                if score > 80:
                    st.success("Strong Technical Understanding")
                elif score > 50:
                    st.info("Moderate Understanding")
                else:
                    st.error("Needs Improvement")
