from langchain import __version__
from langgraph.graph import StateGraph
import faiss
from rank_bm25 import BM25Okapi
from dotenv import load_dotenv
import os

load_dotenv()

print("LangChain:", __version__)
print("FAISS loaded successfully")
print("BM25 loaded successfully")
print("LangGraph loaded successfully")
print("Environment setup working ✅")