import ollama
import numpy as np

# Sample log database
logs = [
"ERROR: Unable to connect to authentication service",
"WARNING: Disk usage exceeded 90%",
"INFO: User login successful",
"ERROR: Database connection timeout"
]

# Step 1: Create embeddings for logs
log_embeddings = [
    ollama.embeddings(model="nomic-embed-text", prompt=log)["embedding"]
    for log in logs
]

# Step 2: User query
query = "database connection error"

query_embedding = ollama.embeddings(
    model="nomic-embed-text",
    prompt=query
)["embedding"]

# Step 3: Find most similar log
similarities = [
    np.dot(query_embedding, emb) for emb in log_embeddings
]

best_log = logs[similarities.index(max(similarities))]

print("\nRetrieved Log:")
print(best_log)

# Step 4: Send to LLM for explanation
response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": f"Explain this system log error and possible fix:\n{best_log}"
        }
    ]
)

print("\nAI Analysis:")
print(response["message"]["content"])