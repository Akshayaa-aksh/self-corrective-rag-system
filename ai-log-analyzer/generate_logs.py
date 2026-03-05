import random

logs = []

patterns = [
"INFO: User login successful",
"INFO: API request completed",
"INFO: Session created successfully",
"WARNING: Disk usage exceeded 90%",
"WARNING: CPU usage exceeded 80%",
"WARNING: High latency detected",
"ERROR: Database connection timeout",
"ERROR: Database connection refused",
"ERROR: Redis connection refused",
"ERROR: Unable to connect to authentication service",
"ERROR: Network timeout while calling payment API",
"ERROR: Memory allocation failure",
"CRITICAL: Segmentation fault detected",
"ERROR: API gateway returned 502",
"ERROR: Failed to write to disk"
]

# generate 600 logs
for i in range(1000):
    log = random.choice(patterns)
    logs.append(log)

with open("ai-log-analyzer/logs.txt", "w") as f:
    for log in logs:
        f.write(log + "\n")

print("1000 logs generated successfully!")