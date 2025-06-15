import streamlit as st
import pandas as pd
import json

st.title("🛡️ Mini Cyber Range Simulator")
st.subheader("📊 Cleaned Log Table")

# Load logs
with open("cyber_range_logs.json") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

# ✅ Safely display only columns that exist
valid_fields = ["timestamp", "source_ip", "destination_ip", "event_type"]
available_fields = [field for field in valid_fields if field in df.columns]

if not df.empty and available_fields:
    st.dataframe(df[available_fields])
else:
    st.warning("Log file is empty or formatted incorrectly.")
