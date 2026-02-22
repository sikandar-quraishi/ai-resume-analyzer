# # import streamlit as st
# # import re

# # st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# # st.title("🚀 AI Resume Analyzer (POC)")
# # st.markdown("### AI-Powered Resume Matching System")

# # def extract_skills(text):
# #     # Simple skill extraction (customize if needed)
# #     common_skills = [
# #         "react", "javascript", "redux", "rest", "api",
# #         "node", "typescript", "git", "html", "css",
# #         "python", "django", "sql", "aws", "docker"
# #     ]
    
# #     found = []
# #     text_lower = text.lower()
    
# #     for skill in common_skills:
# #         if skill in text_lower:
# #             found.append(skill.capitalize())
    
# #     return set(found)

# # def analyze_resume(job_desc, resume):
# #     job_skills = extract_skills(job_desc)
# #     resume_skills = extract_skills(resume)
    
# #     matched = job_skills.intersection(resume_skills)
# #     missing = job_skills.difference(resume_skills)
    
# #     if len(job_skills) == 0:
# #         match_percent = 0
# #     else:
# #         match_percent = int((len(matched) / len(job_skills)) * 100)
    
# #     return match_percent, matched, missing

# # col1, col2 = st.columns(2)

# # with col1:
# #     job_desc = st.text_area("📄 Job Description", height=300)

# # with col2:
# #     resume = st.text_area("📑 Resume", height=300)

# # if st.button("Analyze Resume"):
# #     if not job_desc or not resume:
# #         st.warning("⚠️ Please fill both fields.")
# #     else:
# #         match_percent, matched, missing = analyze_resume(job_desc, resume)
        
# #         st.success("✅ Analysis Complete")
        
# #         st.markdown(f"## 🎯 Match Score: {match_percent}%")
        
# #         st.markdown("### ✅ Matching Skills")
# #         if matched:
# #             for skill in matched:
# #                 st.write(f"- {skill}")
# #         else:
# #             st.write("No matching skills found.")
        
# #         st.markdown("### ❌ Missing Skills")
# #         if missing:
# #             for skill in missing:
# #                 st.write(f"- {skill}")
# #         else:
# #             st.write("No missing skills. Great match!")
        
# #         st.markdown("### 🧠 AI Recommendation")
# #         if match_percent > 80:
# #             st.write("Strong candidate. Highly recommended.")
# #         elif match_percent > 50:
# #             st.write("Moderate match. Consider shortlisting.")
# #         else:
# #             st.write("Low match. Needs skill improvement.")



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

# # ---------------------------------------------
# # POC 3 - Job Description Generator
# # ---------------------------------------------

# elif menu == "Job Description Generator":

#     st.header("📋 Job Description Generator")

#     role = st.selectbox(
#         "Select Job Role",
#         [
#             "Frontend Developer",
#             "Backend Developer",
#             "Full Stack Developer",
#             "Python Developer",
#             "Node.js Developer"
#         ]
#     )

#     experience = st.selectbox(
#         "Experience Level",
#         ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"]
#     )

#     if st.button("Generate Job Description"):

#         st.success("Job Description Generated")

#         st.markdown(f"## 📌 {role} ({experience})")

#         st.markdown("### 🔹 Role Summary")
#         st.write(f"We are looking for a skilled {role} with {experience} experience to join our development team and build scalable, high-quality applications.")

#         st.markdown("### 🔹 Key Responsibilities")
#         st.write("- Develop and maintain high-quality applications")
#         st.write("- Collaborate with cross-functional teams")
#         st.write("- Write clean and maintainable code")
#         st.write("- Participate in code reviews")
#         st.write("- Troubleshoot and debug applications")

#         st.markdown("### 🔹 Required Skills")

#         if role == "Frontend Developer":
#             st.write("- React / JavaScript")
#             st.write("- HTML / CSS")
#             st.write("- REST API integration")
#             st.write("- Git")

#         elif role == "Backend Developer":
#             st.write("- Server-side programming")
#             st.write("- REST API development")
#             st.write("- Database management")
#             st.write("- Authentication & authorization")

#         elif role == "Full Stack Developer":
#             st.write("- Frontend + Backend technologies")
#             st.write("- API development")
#             st.write("- Database knowledge")
#             st.write("- Deployment experience")

#         elif role == "Python Developer":
#             st.write("- Python programming")
#             st.write("- Django / Flask")
#             st.write("- SQL")
#             st.write("- REST APIs")

#         elif role == "Node.js Developer":
#             st.write("- Node.js")
#             st.write("- Express.js")
#             st.write("- MongoDB / SQL")
#             st.write("- API development")

#         st.markdown("### 🔹 Nice To Have")
#         st.write("- Cloud knowledge (AWS / Azure)")
#         st.write("- CI/CD understanding")
#         st.write("- Docker / Containerization")



import streamlit as st

st.set_page_config(page_title="AI HR Tools Suite", layout="wide")

st.title("🚀 AI HR Tools Suite (POC Project)")

# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------

menu = st.sidebar.selectbox(
    "Select AI Tool",
    [
        "Resume Analyzer",
        "Interview Question Generator",
        "Job Description Generator"
    ]
)

# ---------------------------------------------
# COMMON SKILL LOGIC
# ---------------------------------------------

def extract_skills(text):
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


# =============================================
# POC 1 - Resume Analyzer
# =============================================

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
                st.write("No missing skills. Strong match!")

            st.markdown("### 🧠 Recommendation")

            if match_percent > 80:
                st.success("Strong candidate. Highly recommended.")
            elif match_percent > 50:
                st.info("Moderate match. Consider shortlisting.")
            else:
                st.error("Low match. Needs skill improvement.")


# =============================================
# POC 2 - Interview Question Generator
# =============================================

elif menu == "Interview Question Generator":

    st.header("🎤 Interview Question Generator")

    role = st.text_input("Enter Job Role (e.g., React Developer)")

    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"]
    )

    if st.button("Generate Questions"):

        if not role:
            st.warning("Please enter job role.")
        else:
            st.success("Questions Generated")

            st.markdown("## 🧠 Technical Questions")

            st.write(f"1. Explain core concepts of {role}.")
            st.write(f"2. What are best practices in {role}?")
            st.write(f"3. Describe a challenging project in {role}.")
            st.write(f"4. How do you optimize performance in {role}?")
            st.write(f"5. What tools are commonly used in {role}?")

            st.markdown("## 🤝 Behavioral Questions")

            st.write("1. Describe a conflict you handled in a team.")
            st.write("2. How do you manage deadlines?")
            st.write("3. How do you keep learning new technologies?")


# =============================================
# POC 3 - Job Description Generator
# =============================================

elif menu == "Job Description Generator":

    st.header("📋 Job Description Generator")

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

        st.success("Job Description Generated")

        st.markdown(f"## 📌 {role} ({experience})")

        st.markdown("### 🔹 Role Summary")
        st.write(
            f"We are looking for a skilled {role} with {experience} experience "
            "to join our development team and build scalable, high-quality applications."
        )

        st.markdown("### 🔹 Key Responsibilities")
        st.write("- Develop and maintain high-quality applications")
        st.write("- Collaborate with cross-functional teams")
        st.write("- Write clean and maintainable code")
        st.write("- Participate in code reviews")
        st.write("- Troubleshoot and debug applications")

        st.markdown("### 🔹 Required Skills")

        if role == "Frontend Developer":
            st.write("- React / JavaScript")
            st.write("- HTML / CSS")
            st.write("- REST API integration")
            st.write("- Git")

        elif role == "Backend Developer":
            st.write("- Server-side programming")
            st.write("- REST API development")
            st.write("- Database management")
            st.write("- Authentication & authorization")

        elif role == "Full Stack Developer":
            st.write("- Frontend + Backend technologies")
            st.write("- API development")
            st.write("- Database knowledge")
            st.write("- Deployment experience")

        elif role == "Python Developer":
            st.write("- Python programming")
            st.write("- Django / Flask")
            st.write("- SQL")
            st.write("- REST APIs")

        elif role == "Node.js Developer":
            st.write("- Node.js")
            st.write("- Express.js")
            st.write("- MongoDB / SQL")
            st.write("- API development")

        st.markdown("### 🔹 Nice To Have")
        st.write("- Cloud knowledge (AWS / Azure)")
        st.write("- CI/CD understanding")
        st.write("- Docker / Containerization")

# =============================================
# POC 1 - Resume Analyzer + Screening Dashboard
# =============================================

if menu == "Resume Analyzer":

    st.header("📄 Resume Analyzer & Screening Dashboard")

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

            # ---------------- SCORE DISPLAY ----------------
            st.markdown(f"# 🎯 Match Score: {match_percent}%")
            st.progress(match_percent)

            # ---------------- SCREENING LOGIC ----------------
            if match_percent >= 80:
                status = "Shortlisted"
                priority = "High"
                next_action = "Schedule Technical Interview"
                recommendation = "Strong candidate. Move to next round immediately."

            elif match_percent >= 50:
                status = "On Hold"
                priority = "Medium"
                next_action = "Manual HR Review Required"
                recommendation = "Candidate meets partial requirements. Further evaluation needed."

            else:
                status = "Rejected"
                priority = "Low"
                next_action = "Send Rejection Email"
                recommendation = "Candidate does not meet required criteria."

            # ---------------- DASHBOARD DISPLAY ----------------
            st.markdown("## 📊 Screening Dashboard")

            colA, colB, colC = st.columns(3)

            colA.metric("Screening Status", status)
            colB.metric("Priority Level", priority)
            colC.metric("Next Action", next_action)

            st.markdown("### 🧠 Hiring Recommendation")
            st.write(recommendation)

            # ---------------- SKILL BREAKDOWN ----------------
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
                st.write("No missing skills. Strong match!")
