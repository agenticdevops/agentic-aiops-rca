# agentic-aiops-rca
Simple Root Cause Analysis Agent  for Kubernetes Pods in Pure Python and Streamlit


## Pre requisites 

  * Kubernetes Cluster with Kubectl configured on local machine to talk to it 
  * Prometheus 
  * Loki Configured with Promtail 
  * Local llama setup with some model e.g. mistral 
  * Python with ideall UV installed 


## Run this Project 

Setup local python env 

```
uv venv 
source .venv/bin/activate  
uv pip install -r requirements.txt
```

Then either run the app directly using 

```
python agentic_rca.py --pod vote --start 10m

```

[ Sample Output]: 

```
🔍 Analyzing pod: vote in the last 10m...
📈 Fetching metrics from Prometheus...
📄 Fetching logs from Loki...
🧠 Sending data to LLM for analysis...

📝 RCA Report:

 I'm an assistant and don't have direct access to your Kubernetes cluster or the logs/metrics you provided. However, I can help you analyze the information based on common signs of issues in a Kubernetes environment. Here's my analysis of the logs:

The log snippet you provided doesn't show any obvious errors or exceptions that could indicate an anomaly with the pod vote. It seems to be a normal start-up log message, but it's hard to tell without more context or seeing the entire log output.

However, if we look at some potential metrics to consider:

1. CPU Utilization: High CPU utilization could mean that your pod is overworked and might need additional resources, such as increasing the CPU request or limiting other resource-intensive tasks.

2. Memory Usage: Similarly, high memory usage could indicate that the pod requires more memory to function correctly. This can be addressed by adjusting the memory limits and requests for the pod.

3. Network traffic: Abnormal network traffic could suggest a problem with the application or potential security issues like DDoS attacks. Monitoring network traffic is crucial for identifying such anomalies.
# agentic-aiops-rca

4. Error rates: The absence of errors in your logs doesn't necessarily mean everything is okay. Check the system logs and any external monitoring tools to ensure that there are no hidden issues.

5. Pod restarts: A high number of pod restarts could indicate underlying issues with the deployment or the node hosting the pod, such as resource exhaustion, misconfiguration, or hardware failure.

6. Latency and throughput: Slower response times (latency) or reduced throughput could suggest application performance issues that need to be addressed.

Root Cause Analysis:
Without specific metrics, it's challenging to pinpoint the root cause of any anomalies in this scenario. However, based on the logs provided and the potential metrics listed above, here are some possible root causes:

1. Insufficient resources (CPU or memory) for the pod
2. Application performance issues (e.g., bottlenecks, code errors)
3. Network connectivity problems (internal or external)
4. Misconfiguration of the application, pod, or deployment
5. Hardware failures on the node hosting the pod
6. Security vulnerabilities or DDoS attacks affecting the application or network

Remediation Steps:
To address potential issues with your Kubernetes environment, consider these steps:

1. Monitor and adjust resource limits for your pods based on observed usage patterns.
2. Optimize application code to minimize performance bottlenecks and improve scalability.
3. Check network connectivity between pods, nodes, and external resources to ensure proper communication.
4. Validate the configuration of your applications, pods, and deployments to avoid misconfigurations that could lead to unexpected behavior.
5. Ensure that you have adequate hardware resources for your nodes and consider scaling horizontally if necessary.
6. Implement security measures such as network segmentation, intrusion detection/prevention systems (IDPS), and regular vulnerability scanning to protect against potential threats.

```

Or launch the streamlit UI with 

```

streamlit run app.py

```
