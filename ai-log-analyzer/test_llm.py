import ollama

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": "Explain RAG in one sentence"}]
)

print(response["message"]["content"])