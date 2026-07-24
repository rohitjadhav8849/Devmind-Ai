<div align="center">

# 🧠 DevMind AI

### Enterprise Knowledge Intelligence Platform (Agentic RAG)

**Chat with your documents using natural language — grounded in real content, not hallucinated answers.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logoColor=white)
![Mistral](https://img.shields.io/badge/Mistral_7B-FF6B35?style=for-the-badge&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=for-the-badge&logoColor=white)

</div>

---

## 📖 Overview

**DevMind AI** is an enterprise-grade **Retrieval-Augmented Generation (RAG)** platform that lets users interact with their own documents using natural language. Instead of relying purely on an LLM's pre-trained knowledge — which often leads to hallucinated or generic answers — the system retrieves relevant information directly from uploaded documents and uses that context to generate accurate, document-grounded responses.

Users upload PDF documents, which are processed through a custom ingestion pipeline. The extracted text is split into manageable chunks, converted into vector embeddings using the **`BAAI/bge-small-en-v1.5`** embedding model, and stored in **Qdrant**, a vector database optimized for semantic search.

When a user asks a question, the app:
1. Generates an embedding for the query
2. Retrieves the most relevant document chunks from Qdrant via similarity search
3. Builds a contextual prompt from those chunks
4. Sends it to a locally hosted **Mistral 7B** model running through **Ollama**

The LLM then generates an answer grounded in the retrieved content — reducing hallucinations and improving accuracy, with no data ever leaving the server.

---

## 🏗️ Architecture

```
PDF Upload
     │
     ▼
Document Processing
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
(BAAI/bge-small-en-v1.5)
     │
     ▼
Qdrant Vector Database
     │
     ▼
User Query
     │
     ▼
Query Embedding
     │
     ▼
Semantic Search
     │
     ▼
Prompt Construction
     │
     ▼
Mistral 7B (Ollama)
     │
     ▼
AI Response
```

The backend follows a **modular, service-oriented architecture**:

| Service | Responsibility |
|---|---|
| Document Processor | Handles PDF parsing and text extraction |
| Embedding Service | Generates vector embeddings via Sentence Transformers |
| Retrieval Service | Performs semantic search against Qdrant |
| Prompt Builder | Constructs context-aware prompts from retrieved chunks |
| LLM Service | Interfaces with Mistral 7B via Ollama for response generation |

---

## 🛠️ Tech Stack

**Frontend**
- React
- Vite
- Axios
- CSS

**Backend**
- FastAPI
- Python
- Pydantic

**AI & RAG**
- Mistral 7B (via Ollama)
- Sentence Transformers
- `BAAI/bge-small-en-v1.5` embedding model
- Qdrant (vector database / semantic search)
- Prompt Engineering
- Retrieval-Augmented Generation (RAG)

---

## ✨ Key Features

- 📄 Upload and process PDF documents
- 🧩 Automatic document chunking and vector embedding generation
- 🔎 Semantic search using the Qdrant vector database
- 💬 Context-aware question answering powered by RAG
- 🖥️ Fully local LLM inference via Ollama + Mistral 7B — no external API calls
- ⚛️ Clean, conversational React chat interface
- 🧱 Modular, service-oriented backend architecture

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.com) installed locally with the `mistral` model pulled
- [Qdrant](https://qdrant.tech) running locally (via Docker) or a Qdrant Cloud instance

```bash
# Pull the Mistral model via Ollama
ollama pull mistral

# Run Qdrant locally via Docker
docker run -p 6333:6333 qdrant/qdrant
```

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure environment variables (Qdrant URL, Ollama host, etc.)
cp .env.example .env

# Run the FastAPI server
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The app should now be running at `http://localhost:5173` (frontend) with the API available at `http://localhost:8000`.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload` | Upload and process a PDF document |
| `POST` | `/query` | Ask a question and receive a context-grounded answer |
| `GET` | `/documents` | List all uploaded/processed documents |
| `GET` | `/health` | Health check for API and dependent services |

*(Adjust routes above to match your actual FastAPI route definitions.)*

---

## 🗺️ Roadmap

- [ ] Multi-document cross-referencing in a single query
- [ ] Support for `.docx` and `.txt` uploads
- [ ] Streaming responses (token-by-token) in the chat UI
- [ ] User authentication and per-user document isolation
- [ ] Conversation history and follow-up question handling
- [ ] Swap in larger/quantized models with configurable inference backends

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](../../issues) or open a PR.

---

## 📬 Contact

**Rohit Jadhav**
[LinkedIn](https://linkedin.com/in/rohit-jadhav-8bb77127a) • [GitHub](https://github.com/rohitjadhav8849)

---

<div align="center">

**⭐ If this project helped you, consider giving it a star!**

</div>