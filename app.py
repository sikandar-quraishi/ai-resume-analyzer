# import streamlit as st

# st.set_page_config(page_title="AI HR Tools Suite", layout="wide")

# st.title("🚀 AI HR Tools Suite (POC Project)")

# # ---------------------------------------------
# # Sidebar Navigation
# # ---------------------------------------------

# menu = st.sidebar.selectbox(
#     "Select AI Tool",
#     [
#         "Resume Analyzer",
#         "Interview Question Generator",
#         "Job Description Generator"
#     ]
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


# # =============================================
# # POC 1 - Resume Analyzer + Screening Dashboard
# # =============================================

# if menu == "Resume Analyzer":

#     st.header("📄 Resume Analyzer & Screening Dashboard")

#     col1, col2 = st.columns(2)

#     with col1:
#         job_desc = st.text_area("Job Description", height=250, key="job_desc")

#     with col2:
#         resume = st.text_area("Resume", height=250, key="resume")

#     if st.button("Analyze Resume", key="analyze_btn"):

#         if not job_desc or not resume:
#             st.warning("Please fill both fields.")
#         else:
#             match_percent, matched, missing = analyze_resume(job_desc, resume)

#             st.success("Analysis Complete")

#             st.markdown(f"# 🎯 Match Score: {match_percent}%")
#             st.progress(match_percent)

#             # Screening Logic
#             if match_percent >= 80:
#                 status = "Shortlisted"
#                 priority = "High"
#                 next_action = "Schedule Technical Interview"
#                 recommendation = "Strong candidate. Move to next round immediately."

#             elif match_percent >= 50:
#                 status = "On Hold"
#                 priority = "Medium"
#                 next_action = "Manual HR Review Required"
#                 recommendation = "Candidate meets partial requirements. Further evaluation needed."

#             else:
#                 status = "Rejected"
#                 priority = "Low"
#                 next_action = "Send Rejection Email"
#                 recommendation = "Candidate does not meet required criteria."

#             st.markdown("## 📊 Screening Dashboard")

#             colA, colB, colC = st.columns(3)
#             colA.metric("Screening Status", status)
#             colB.metric("Priority Level", priority)
#             colC.metric("Next Action", next_action)

#             st.markdown("### 🧠 Hiring Recommendation")
#             st.write(recommendation)

#             st.markdown("### ✅ Matching Skills")
#             if matched:
#                 for skill in matched:
#                     st.write(f"- {skill}")
#             else:
#                 st.write("No matching skills found.")

#             st.markdown("### ❌ Missing Skills")
#             if missing:
#                 for skill in missing:
#                     st.write(f"- {skill}")
#             else:
#                 st.write("No missing skills. Strong match!")


# # =============================================
# # POC 2 - Interview Question Generator
# # =============================================

# elif menu == "Interview Question Generator":

#     st.header("🎤 Interview Question Generator")

#     role = st.text_input("Enter Job Role (e.g., React Developer)", key="role_input")

#     experience = st.selectbox(
#         "Experience Level",
#         ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"],
#         key="experience_select"
#     )

#     if st.button("Generate Questions", key="generate_questions"):

#         if not role:
#             st.warning("Please enter job role.")
#         else:
#             st.success("Questions Generated")

#             st.markdown("## 🧠 Technical Questions")
#             st.write(f"1. Explain core concepts of {role}.")
#             st.write(f"2. What are best practices in {role}?")
#             st.write(f"3. Describe a challenging project in {role}.")
#             st.write(f"4. How do you optimize performance in {role}?")
#             st.write(f"5. What tools are commonly used in {role}?")

#             st.markdown("## 🤝 Behavioral Questions")
#             st.write("1. Describe a conflict you handled in a team.")
#             st.write("2. How do you manage deadlines?")
#             st.write("3. How do you keep learning new technologies?")


# # =============================================
# # POC 3 - Job Description Generator
# # =============================================

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
#         ],
#         key="jd_role"
#     )

#     experience = st.selectbox(
#         "Experience Level",
#         ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"],
#         key="jd_experience"
#     )

#     if st.button("Generate Job Description", key="generate_jd"):

#         st.success("Job Description Generated")

#         st.markdown(f"## 📌 {role} ({experience})")

#         st.markdown("### 🔹 Role Summary")
#         st.write(
#             f"We are looking for a skilled {role} with {experience} experience "
#             "to join our development team and build scalable, high-quality applications."
#         )

#         st.markdown("### 🔹 Key Responsibilities")
#         st.write("- Develop and maintain high-quality applications")
#         st.write("- Collaborate with cross-functional teams")
#         st.write("- Write clean and maintainable code")
#         st.write("- Participate in code reviews")
#         st.write("- Troubleshoot and debug applications")

#         st.markdown("### 🔹 Required Skills")
#         st.write("- Relevant technical stack knowledge")
#         st.write("- API development/integration")
#         st.write("- Database knowledge")
#         st.write("- Version control (Git)")

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
        "Job Description Generator",
        "Candidate Ranking System"
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
# 1️⃣ Resume Analyzer + Screening Dashboard
# =============================================

if menu == "Resume Analyzer":

    st.header("📄 Resume Analyzer & Screening Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        job_desc = st.text_area("Job Description", height=250, key="ra_job")

    with col2:
        resume = st.text_area("Resume", height=250, key="ra_resume")

    if st.button("Analyze Resume", key="ra_btn"):

        if not job_desc or not resume:
            st.warning("Please fill both fields.")
        else:
            match_percent, matched, missing = analyze_resume(job_desc, resume)

            st.success("Analysis Complete")

            st.markdown(f"# 🎯 Match Score: {match_percent}%")
            st.progress(match_percent)

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

            st.markdown("## 📊 Screening Dashboard")

            colA, colB, colC = st.columns(3)
            colA.metric("Screening Status", status)
            colB.metric("Priority Level", priority)
            colC.metric("Next Action", next_action)

            st.markdown("### 🧠 Hiring Recommendation")
            st.write(recommendation)

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


# =============================================
# 2️⃣ Interview Question Generator
# =============================================

elif menu == "Interview Question Generator":

    st.header("🎤 Interview Question Generator")

    role = st.text_input("Enter Job Role (e.g., React Developer)", key="iq_role")

    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"],
        key="iq_exp"
    )

    if st.button("Generate Questions", key="iq_btn"):

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
# 3️⃣ Job Description Generator
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
        ],
        key="jd_role"
    )

    experience = st.selectbox(
        "Experience Level",
        ["Fresher", "Mid-Level (2-5 years)", "Senior (5+ years)"],
        key="jd_exp"
    )

    if st.button("Generate Job Description", key="jd_btn"):

        st.success("Job Description Generated")

        st.markdown(f"## 📌 {role} ({experience})")

        st.markdown("### 🔹 Role Summary")
        st.write(
            f"We are looking for a skilled {role} with {experience} experience "
            "to join our development team and build scalable applications."
        )

        st.markdown("### 🔹 Key Responsibilities")
        st.write("- Develop and maintain applications")
        st.write("- Collaborate with teams")
        st.write("- Write clean code")
        st.write("- Participate in code reviews")

        st.markdown("### 🔹 Required Skills")
        st.write("- Relevant technical stack knowledge")
        st.write("- API development/integration")
        st.write("- Database knowledge")
        st.write("- Version control (Git)")

        st.markdown("### 🔹 Nice To Have")
        st.write("- Cloud knowledge (AWS/Azure)")
        st.write("- CI/CD understanding")
        st.write("- Docker knowledge")


# =============================================
# 4️⃣ Candidate Ranking System
# =============================================

elif menu == "Candidate Ranking System":

    st.header("🏆 Candidate Ranking Dashboard")

    job_desc = st.text_area("Enter Job Description", height=200, key="rank_job")

    num_candidates = st.number_input(
        "Number of Candidates",
        min_value=1,
        max_value=10,
        value=3,
        key="rank_num"
    )

    candidates = []

    for i in range(int(num_candidates)):
        st.markdown(f"### Candidate {i+1}")
        name = st.text_input(f"Candidate Name {i+1}", key=f"rank_name_{i}")
        resume = st.text_area(f"Resume {i+1}", height=150, key=f"rank_resume_{i}")
        candidates.append((name, resume))

    if st.button("Rank Candidates", key="rank_btn"):

        if not job_desc:
            st.warning("Please enter job description.")
        else:
            results = []

            for name, resume in candidates:
                if name and resume:
                    match_percent, _, _ = analyze_resume(job_desc, resume)

                    if match_percent >= 80:
                        status = "Shortlisted"
                    elif match_percent >= 50:
                        status = "On Hold"
                    else:
                        status = "Rejected"

                    results.append({
                        "Candidate": name,
                        "Match %": match_percent,
                        "Status": status
                    })

            if results:
                results = sorted(results, key=lambda x: x["Match %"], reverse=True)

                st.success("Ranking Complete")
                st.markdown("## 📊 Candidate Ranking")

                for idx, candidate in enumerate(results, start=1):
                    st.markdown(f"### 🥇 Rank {idx}: {candidate['Candidate']}")
                    st.write(f"Match Score: {candidate['Match %']}%")
                    st.write(f"Status: {candidate['Status']}")
                    st.markdown("---")
            else:
                st.warning("Please enter candidate details.")
