# app.py – CyberSecure AI: Smart Policy & Threat Detector

import streamlit as st
import pandas as pd
import ollama
import re

# --- Security Policy Text Review ---
def extract_text_from_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        import fitz  # PyMuPDF
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    else:
        return ""

# --- Prompt Builder for LLM ---
def build_policy_prompt(text):
    prompt = f"""
You are a cybersecurity auditor assistant. Analyze the following policy and:
1. Summarize its content
2. Check for coverage of topics: Access Control, Encryption, Backup, Incident Response, Physical Security, Compliance
3. Identify missing/weak areas
4. Recommend 3 improvements
5. Output in JSON with keys: Summary, Missing Topics, Weak Points, Recommendations

Policy:
{text[:3000]}
"""
    return prompt

# --- Log Anomaly Detector ---
def analyze_logs(df):
    anomalies = []
    if 'IP' in df.columns:
        common_failures = df[df['Event'].str.contains("failed", case=False)]
        failed_logins = common_failures['IP'].value_counts().to_dict()
        for ip, count in failed_logins.items():
            if count > 5:
                anomalies.append(f"High number of failed logins from IP: {ip} ({count} times)")
    if 'Port' in df.columns:
        scan_ips = df['Port'].value_counts().to_dict()
        if max(scan_ips.values()) > 10:
            anomalies.append("Suspicious port scan activity detected")
    return anomalies

# --- LLM Query Function ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit App ---
st.set_page_config(page_title="CyberSecure AI", layout="wide")
st.title("🛡️ CyberSecure AI – Policy & Log Analyzer")

st.sidebar.header("Choose Analysis Type")
mode = st.sidebar.radio("Select:", ["Security Policy Review", "Log File Analysis"])

if mode == "Security Policy Review":
    uploaded_policy = st.file_uploader("Upload Security Policy Document (TXT or PDF)", type=["txt", "pdf"])
    if uploaded_policy:
        with st.spinner("Processing document..."):
            raw_text = extract_text_from_uploaded_file(uploaded_policy)
            prompt = build_policy_prompt(raw_text)
            result = query_llm(prompt)
            st.markdown("### 🧾 Policy Summary & Risk Analysis")
            st.code(result, language='json')
else:
    uploaded_log = st.file_uploader("Upload Log File (CSV with columns: IP, Event, Port)", type=["csv"])
    if uploaded_log:
        df = pd.read_csv(uploaded_log)
        st.markdown("### 📊 Log Preview")
        st.dataframe(df.head())
        if st.button("🔍 Analyze Logs"):
            with st.spinner("Analyzing logs for anomalies..."):
                findings = analyze_logs(df)
                if findings:
                    st.markdown("### 🚨 Anomaly Report")
                    for f in findings:
                        st.warning(f)
                else:
                    st.success("No major anomalies detected.")
