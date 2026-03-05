import ollama
import numpy as np

docs = [
    "Database connection timeout error",
    "User login successful",
    "Memory overflow detected in system",
    "Server started successfully"
]

# Create embeddings
doc_embeddings = [
    ollama.embeddings(model="nomic-embed-text", prompt=d)["embedding"]
    for d in docs
]

# Query
query = "database error"

query_embedding = ollama.embeddings(
    model="nomic-embed-text",
    prompt=query
)["embedding"]

# Similarity search
similarities = [
    np.dot(query_embedding, emb) for emb in doc_embeddings
]

best_doc = docs[similarities.index(max(similarities))]

print("Best match:", best_doc)