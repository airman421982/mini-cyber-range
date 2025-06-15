# 🛡️ Mini Cyber Range Simulator

This is a lightweight, self-contained cyber range simulator built for SOC analyst training, interview readiness, and Booz Allen demonstration.

## 🚀 Features

- Simulated attack scenarios (brute force, malware beaconing, port scanning)
- Pre-generated log file in JSON format
- Built-in quiz to test detection accuracy
- Auto-scoring with feedback
- Streamlit dashboard for interactive use

## 📂 Files

| File | Description |
|------|-------------|
| `cyber_range_logs.json` | Sample log data for all attack scenarios |
| `cyber_range_dashboard.py` | Streamlit app to view logs and take quiz |
| `cyber_range_quiz.py` | Command-line version of the quiz |

## 📦 Requirements

```bash
pip install streamlit
```

## ▶️ Run the Dashboard

```bash
streamlit run cyber_range_dashboard.py
```

## 🎯 Purpose

This project demonstrates how security analysts can be trained using simulated logs and guided detection questions. It supports Booz Allen's mission to:
- Accelerate analyst onboarding
- Train with threat-informed defense techniques
- Support Zero Trust and cyber workforce development

## 👤 Author

**Cedrick Gordon**  
Cybersecurity Specialist | U.S. Navy Veteran  
GitHub: [airman421982](https://github.com/airman421982)
