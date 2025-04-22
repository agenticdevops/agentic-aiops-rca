import requests
import os
import time

def fetch_loki_logs(pod_name, duration):
    base_url = os.getenv("LOKI_URL", "http://localhost:3100")
    tenant_id = os.getenv("LOKI_TENANT_ID", "admin")

    # Convert 'duration' like '10m' to seconds (simple parsing)
    num = int(duration[:-1])
    unit = duration[-1]
    factor = {"s": 1, "m": 60, "h": 3600}
    seconds = num * factor.get(unit, 60)

    now = int(time.time() * 1e9)  # now in nanoseconds
    start = now - int(seconds * 1e9)

    query = f'{{pod="{pod_name}"}}'
    params = {
        "query": query,
        "limit": 100,
        "start": str(start),
        "end": str(now),
    }
    headers = {"X-Scope-OrgID": tenant_id}

    try:
        response = requests.get(f"{base_url}/loki/api/v1/query_range", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"🚨 Failed to fetch logs from Loki: {e}")
        return [f"Loki error: {e}"]

    streams = data.get("data", {}).get("result", [])
    logs = []
    for stream in streams:
        for entry in stream.get("values", []):
            logs.append(entry[1])
    return logs
