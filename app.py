import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.markdown("### Powered by OpenRouter Free LLM")

API_URL = "https://openrouter.ai/api/v1/chat/completions"

API_KEY = st.secrets["OPENROUTER_API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def analyze(job_desc, resume):

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "user",
                "content": f"""
Compare the resume with the job description and provide:

1. Match percentage
2. Missing skills
3. Strengths
4. Final recommendation

Job Description:
{job_desc}

Resume:
{resume}
"""
            }
        ],
        "max_tokens": 300
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": f"{response.status_code}: {response.text}"}

    return response.json()

col1, col2 = st.columns(2)

with col1:
    job_desc = st.text_area("📄 Job Description", height=300)

with col2:
    resume = st.text_area("📑 Resume", height=300)

if st.button("Analyze Resume"):

    if not job_desc or not resume:
        st.warning("⚠️ Please fill both fields.")
    else:
        with st.spinner("🤖 AI is analyzing..."):

            result = analyze(job_desc, resume)

            if "choices" in result:
                output = result["choices"][0]["message"]["content"]
                st.success("✅ Analysis Complete")
                st.write(output)
            else:
                st.error(result.get("error", "Unexpected error"))
