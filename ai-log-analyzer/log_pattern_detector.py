import ssl
ssl._create_default_https_context = ssl._create_unverified_context


from sentence_transformers import SentenceTransformer
from sklearn.cluster import DBSCAN
import numpy as np

# Step 1: Sample logs
logs = [
    "User login successful",
    "User login successful",
    "User login successful",
    "ERROR: database connection refused",
    "ERROR: database connection refused",
    "Memory allocation failure",
    "Segmentation fault"
]

# Step 2: Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3: Convert logs into embeddings
embeddings = model.encode(logs)

# Step 4: Cluster logs
clustering = DBSCAN(eps=0.5, min_samples=2).fit(embeddings)

labels = clustering.labels_

clusters = {}

print("\n🔎 Log Analysis Result\n")

# Step 5: Detect clusters and anomalies
for log, label in zip(logs, labels):

    if label == -1:
        print(f"⚠️ Anomaly Detected → {log}")
    else:
        if label not in clusters:
            clusters[label] = []

        clusters[label].append(log)

# Step 6: Print clusters
print("\n📦 Log Clusters\n")

for cluster_id, cluster_logs in clusters.items():
    print(f"Cluster {cluster_id}")
    for log in cluster_logs:
        print("  ", log)