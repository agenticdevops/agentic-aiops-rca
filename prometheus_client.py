# prometheus_client_.py
import requests
import os

def fetch_prometheus_metrics(pod_name, duration):
    base_url = os.getenv("PROM_URL", "http://localhost:9090")
    query = f'rate(container_cpu_usage_seconds_total{{pod="{pod_name}"}}[{duration}])'
    response = requests.get(f"{base_url}/api/v1/query", params={"query": query})
    data = response.json()
    return data.get("data", {}).get("result", [])


