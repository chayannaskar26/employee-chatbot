# 📄 Retrieval-Augmented Generation (RAG) Chatbot

An end-to-end **RAG (Retrieval-Augmented Generation) pipeline** built using **LangChain, OpenAI, and FAISS**, capable of answering questions from multiple PDF documents with high accuracy and contextual awareness.

---

## 🚀 Features

* 📂 Multi-PDF document ingestion
* ✂️ Intelligent text chunking
* 🔎 Hybrid retrieval (Dense + BM25)
* 🎯 Re-ranking layer for improved relevance
* 🧠 Query transformation (rewrite, multi-query)
<!-- * 💬 Conversational memory support -->
* ⚡ Fast semantic search using FAISS
* 🛡️ Hallucination reduction via grounded prompts

---

## 🏗️ Architecture

```
User Query
   ↓
Query Transformation (Rewrite / Multi-Query)
   ↓
Hybrid Retrieval (Dense + BM25)
   ↓
Top-K Documents
   ↓
Re-ranking Layer
   ↓
Context Injection
   ↓
LLM (OpenAI)
   ↓
Final Answer
```

---

## 🧠 Tech Stack

* **LangChain** – Orchestration framework
* **OpenAI (GPT + Embeddings)** – LLM & vector embeddings
* **FAISS** – Vector database
* **BM25** – Sparse retrieval
* **Sentence-Transformers** – Re-ranking (Cross-Encoder)
* **Python** – Core implementation

---

## 🧪 Example Queries

* “What is the mission and vision?”
* “Explain leave policy”
* “What are company ethics rules?”

---

## 📊 Improvements Over Basic RAG

| Feature        | Basic RAG  | This Project |
| -------------- | ---------- | ------------ |
| Retrieval      | Dense only | Hybrid       |
| Ranking        | None       | Re-ranking   |
| Query Handling | Raw        | Transformed  |
| Memory         | None       | Enabled      |
| Accuracy       | Medium     | High         |

---

## ⚠️ Limitations

* LLM-based re-ranking can be slow
* FAISS is in-memory (not distributed)
* No UI (can be extended with Streamlit/FastAPI)

---

## 🎯 Key Learnings

* Chunking strategy directly impacts retrieval quality
* Hybrid search improves recall significantly
* Re-ranking is critical for precision
* Query transformation bridges user intent gap
* Memory enables conversational intelligence

---

## 🤝 Contributing

Feel free to fork and improve the system.

---

## 📜 License

MIT License

---
