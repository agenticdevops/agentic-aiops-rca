# agentic_rca.py
import argparse
from dotenv import load_dotenv
import os
from prometheus_client import fetch_prometheus_metrics
from loki_client import fetch_loki_logs
from llm_interface import analyze_with_llm


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Agentic AIOps RCA Assistant")
    parser.add_argument("--pod", required=True, help="Target Pod Name")
    parser.add_argument("--start", default="10m", help="Time window to look back (e.g., 10m, 1h)")
    args = parser.parse_args()

    print(f"🔍 Analyzing pod: {args.pod} in the last {args.start}...")

    print("📈 Fetching metrics from Prometheus...")
    metrics = fetch_prometheus_metrics(args.pod, args.start)

    print("📄 Fetching logs from Loki...")
    logs = fetch_loki_logs(args.pod, args.start)

    print("🧠 Sending data to LLM for analysis...")
    rca_report = analyze_with_llm(args.pod, metrics, logs)

    print("\n📝 RCA Report:\n")
    print(rca_report)


if __name__ == "__main__":
    main()

