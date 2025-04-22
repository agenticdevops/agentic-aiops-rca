import streamlit as st
import subprocess
import json
from prometheus_client import fetch_prometheus_metrics
from loki_client import fetch_loki_logs
from llm_interface import analyze_with_llm
import os

# Load .env
from dotenv import load_dotenv
load_dotenv()

# Get pods from kubectl
@st.cache_data(ttl=30)
def get_pods():
    try:
        output = subprocess.check_output(["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=NAME:.metadata.name"]).decode().splitlines()
        return output
    except Exception as e:
        return [f"Error fetching pods: {e}"]

st.title("🔍 Agentic AIOps RCA Explorer")

pods = get_pods()
selected_pod = st.selectbox("Select Pod", pods)

time_window = st.selectbox("Lookback Window", ["5m", "10m", "30m", "1h"], index=1)

if st.button("Run RCA"):
    with st.spinner("Fetching metrics..."):
        metrics = fetch_prometheus_metrics(selected_pod, time_window)
    with st.spinner("Fetching logs..."):
        logs = fetch_loki_logs(selected_pod, time_window)

    with st.expander("📈 Raw Metrics"):
        st.json(metrics)

    with st.expander("📄 Raw Logs"):
        st.text("\n".join(logs[:50]))

    with st.spinner("Analyzing with LLM..."):
        rca_report = analyze_with_llm(selected_pod, metrics, logs)

    st.subheader("🧠 RCA Report")
    st.markdown(f"```markdown\n{rca_report}\n```")
