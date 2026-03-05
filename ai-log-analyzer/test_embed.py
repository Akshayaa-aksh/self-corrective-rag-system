import ollama

response = ollama.embeddings(
    model="nomic-embed-text",
    prompt="Error: database connection timeout"
)

print(len(response["embedding"]))