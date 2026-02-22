import streamlit as st
import requests
import os

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer (POC)")
st.write("Paste Job Description and Resume to get AI analysis")

# Hugging Face API
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"
HF_TOKEN = st.secrets["HF_TOKEN"]

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

output = query({
    "inputs": prompt,
    "parameters": {
        "max_length": 512,
        "temperature": 0.7
    }
})

if isinstance(output, list):
    result = output[0]["generated_text"]
    st.success("✅ Analysis Complete")
    st.markdown(result)

elif "error" in output:
    st.error(f"API Error: {output['error']}")

else:
    st.error("Unexpected response format")

# UI Layout
col1, col2 = st.columns(2)

with col1:
    job_desc = st.text_area("📄 Job Description", height=300)

with col2:
    resume = st.text_area("📑 Resume", height=300)

if st.button("Analyze Resume"):
    if job_desc and resume:
        with st.spinner("Analyzing with AI..."):

            prompt = f"""
            Compare the following resume with the job description.
            Give:
            1. Match percentage
            2. Missing skills
            3. Improvement suggestions

            Job Description:
            {job_desc}

            Resume:
            {resume}
            """

            output = query({
                "inputs": prompt,
                "parameters": {"max_length": 512}
            })

            if isinstance(output, list):
                result = output[0]["generated_text"]
                st.success("Analysis Complete!")
                st.write(result)
            else:
                st.error("Error from AI API")
    else:
        st.warning("Please fill both fields.")
