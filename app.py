import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.markdown("### Powered by Hugging Face Free Model")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-small"

HF_TOKEN = st.secrets["HF_TOKEN"]

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def query(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200
        }
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
Compare the resume with the job description.

Give:
1. Match percentage
2. Missing skills
3. Strengths
4. Recommendation

Job Description:
{job_desc}

Resume:
{resume}
"""

            output = query(prompt)

            if isinstance(output, list):
                result = output[0]["generated_text"]
                st.success("✅ Analysis Complete")
                st.write(result)

            elif "error" in output:
                st.error(f"❌ API Error: {output['error']}")

            else:
                st.error("❌ Unexpected API response.")
