# llm_interface.py
import subprocess
import json
import os

def analyze_with_llm(pod_name, metrics, logs):
    context = f"""
You are an expert in Kubernetes AIOps.
Analyze the following metrics and logs for pod {pod_name} and explain if there are any anomalies.
Suggest the probable root cause and possible remediation steps.

--- METRICS ---
{json.dumps(metrics, indent=2)}

--- LOGS ---
{chr(10).join(logs[:20])}
    """
    try:
        result = subprocess.run([
            "ollama", "run", os.getenv("OLLAMA_MODEL", "mistral")
        ], input=context.encode(), capture_output=True)
        return result.stdout.decode()
    except Exception as e:
        return f"Error talking to local LLM: {e}"

