import ollama

query = "database connection error"

retrieved_log = "ERROR: Unable to connect to authentication service"

prompt = f"""
You are a retrieval grader.

User query:
{query}

Retrieved log:
{retrieved_log}

Determine if the retrieved log is relevant to the query.

Respond with ONLY one word:
YES
or
NO
"""

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": prompt}]
)

print(response["message"]["content"])