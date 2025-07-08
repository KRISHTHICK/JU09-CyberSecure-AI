# JU09-CyberSecure-AI
GEN AI

CyberSecure AI – Smart Policy & Threat Detector for Enterprises
🔐 What It Does
CyberSecure AI helps organizations understand and validate their cybersecurity policies, documents, and logs using AI. It can:

Review security policy documents (PDF, DOCX)

Detect missing sections (e.g., password policy, access control)

Analyze firewall/system logs to flag anomalies

Suggest improvements aligned with NIST, ISO, or GDPR

⚙️ Key Features
Feature	Description
📤 Upload Security Docs	Accept security policy files or compliance reports
📚 Policy Coverage Check	Ensures policy includes items like encryption, backup, access control, etc.
🧠 AI Summary & Risk Gaps	LLM explains policy in plain English and flags missing or weak parts
🧾 Log Analysis Module	Upload logs (CSV/TXT), detect suspicious IPs, ports, login failures
📌 Suggest Compliance Improvements	Aligns with NIST, GDPR, ISO 27001, etc.
📉 Risk Score & Heatmap	Shows overall system health or compliance status

🧱 Tech Stack
Layer	Tool
UI	Streamlit
LLM	Ollama (LLaMA3) or GPT-4
Log Parsing	Python (regex, pandas)
Policy Check	Rule-based + AI summary
Visualization	Plotly or matplotlib (for heatmaps)
Optional Cloud	Azure/AWS/GCP for hosting or secure file storage

# 🛡️ CyberSecure AI – Smart Policy & Log Analyzer

CyberSecure AI helps IT teams analyze cybersecurity policy documents and system logs using LLMs to find risks, gaps, and anomalies.

## 🔍 Features

### 1. Policy Analyzer
- Upload security policy (TXT or PDF)
- Summarize contents
- Identify missing topics (e.g., access control, encryption)
- Suggest compliance improvements (e.g., NIST)

### 2. Log Analyzer
- Upload log CSV with IP, Event, Port
- Detect anomalies (failed login bursts, port scans)
- Generate risk alerts and summaries

---

## 🚀 Run the App

```bash
git clone https://github.com/yourusername/cybersecure-ai.git
cd cybersecure-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
