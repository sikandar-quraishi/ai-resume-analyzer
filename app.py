import streamlit as st
import requests

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.markdown("### Powered by Hugging Face Free Model")

# -------------------------------
# API Configuration
# -------------------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

# Get token safely from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# -------------------------------
# API Function
# -------------------------------
def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# -------------------------------
# UI Layout
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    job_desc = st.text_area("📄 Job Description", height=300)

with col2:
    resume = st.text_area("📑 Resume", height=300)

# -------------------------------
# Button Action
# -------------------------------
if st.button("Analyze Resume"):

    if not job_desc or not resume:
        st.warning("⚠️ Please fill both fields.")
    else:
        with st.spinner("🤖 AI is analyzing..."):

            prompt = f"""
            Act like a professional HR recruiter.

            Compare the resume with the job description and provide:

            1. Match Percentage (in %)
            2. Missing Skills
            3. Strengths
            4. Final Recommendation (short)

            Job Description:
            {job_desc}

            Resume:
            {resume}
            """

            output = query({
                "inputs": prompt,
                "parameters": {
                    "max_length": 512,
                    "temperature": 0.7
                }
            })

            # -------------------------------
            # Handle Response
            # -------------------------------
            if isinstance(output, list) and "generated_text" in output[0]:
                result = output[0]["generated_text"]
                st.success("✅ Analysis Complete")
                st.markdown(result)

            elif "error" in output:
                st.error(f"❌ API Error: {output['error']}")

            else:
                st.error("❌ Unexpected API response. Try again.")
