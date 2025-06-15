import streamlit as st
import json

# Load log data
import pandas as pd

st.subheader("📄 Parsed Log Table")

with open("cyber_range_logs.json") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

if not df.empty and 'source_ip' in df.columns:
    st.dataframe(df[["timestamp", "source_ip", "alert_type", "risk_score", "action"]])
else:
    st.warning("Expected fields not found. Check your log format.")

st.title("🛡️ Mini Cyber Range Simulator")

st.header("📄 Log Viewer")
st.write("Review the simulated logs below:")
st.json(logs, expanded=False)

st.header("🧠 Detection Quiz")

# Define questions and expected answers
questions = {
    "What IP address attempted a brute force attack?": "10.0.0.15",
    "How many failed login attempts were made?": "20",
    "What IP address is exhibiting beaconing behavior?": "192.168.1.200",
    "What C2 IP is being contacted repeatedly?": "8.8.8.8",
    "What IP scanned multiple ports?": "172.16.0.9",
    "List 3 ports scanned by the attacker (comma-separated)": "21,22,23"
}

score = 0

with st.form("quiz_form"):
    user_answers = {}
    for question in questions:
        user_answers[question] = st.text_input(question)

    submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        st.subheader("📊 Results")
        for q, correct in questions.items():
            user = user_answers[q].strip().lower().replace(" ", "")
            expected = correct.lower().replace(" ", "")
            if expected in user:
                st.success(f"✅ {q}")
                score += 1
            else:
                st.error(f"❌ {q} (Expected: {correct})")

        st.write(f"### Final Score: {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
            st.success("🎉 Excellent job!")
        elif score >= len(questions) // 2:
            st.info("👍 Good effort. Review the log again for full points.")
        else:
            st.warning("📘 Keep practicing — check the log closely!")
