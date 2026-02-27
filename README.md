## Self-Corrective Multi-Agent RAG System
📌 Project Overview

This project implements a Self-Corrective Multi-Agent Retrieval-Augmented Generation (RAG) system designed to improve answer accuracy through structured retrieval, evaluation, and correction mechanisms.

The system will integrate:

Hybrid Retrieval (Vector + BM25)

Multi-Agent Architecture

Self-Correction Loop

LangGraph-based Workflow Orchestration

FAISS Vector Store

This repository currently contains the environment setup and base project structure

## 📁 Project Structure
self-corrective-rag/
│
├── rag_env/
├── .env
├── .gitignore
├── requirements.txt
├── verify_setup.py
├── README.md
└── src/
    ├── retrieval/
    ├── agents/
    ├── graph/
    └── utils/

## 🛠 Installation & Setup

1. Clone the repository
2. Create virtual environment
3. Activate environment
4. Install dependencies
5. Add API key in .env

## 🧪 Environment Verification

Run:
python verify_setup.py

Expected Output:

LangChain: <version>
FAISS loaded successfully
BM25 loaded successfully
LangGraph loaded successfully
Environment setup working ✅

👩‍💻 Author
Akshayaa