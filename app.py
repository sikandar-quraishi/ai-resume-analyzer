import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.markdown("### Powered by Hugging Face Router API")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

HF_TOKEN = st.secrets["HF_TOKEN"]

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def query(prompt):
    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": f"Status Code {response.status_code}: {response.text}"}

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

            prompt = f"""
Act like a professional HR recruiter.

Compare the resume with the job description and provide:

1. Match Percentage
2. Missing Skills
3. Strengths
4. Final Recommendation

Job Description:
{job_desc}

Resume:
{resume}
"""

            output = query(prompt)

            if isinstance(output, list):
                result = output[0].get("generated_text", "")
                st.success("✅ Analysis Complete")
                st.write(result)

            elif "error" in output:
                st.error(f"❌ API Error: {output['error']}")

            else:
                st.error("❌ Unexpected response from API.")
