# KBIDE-AI: Localized Multi Agentic RAG Pipeline with ChromaDB & Ollama Orchestration

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-orange.svg)](https://ollama.com/)

An advanced, locally hosted Multi-Agent Retrieval-Augmented Generation (RAG) system designed to parse, index, and reason over technical process documentation (`.docx`) using structured agent orchestration.

<img width="3075" height="1507" alt="KBIDE-AI" src="https://github.com/user-attachments/assets/cd95d02e-8ba2-45e5-b695-a46bc4869664" />


[📑 Project Overview]
- KBIDE-AI is an intelligent, locally-hosted Multi-Agent Retrieval-Augmented Generation (RAG) framework designed to transform static technical process documentation into an interactive, context-aware knowledge base.

- Unlike traditional flat RAG pipelines, KBIDE-AI uses a decoupled, modular agentic architecture. It orchestrates a specialized team of agents (Router, Process, and Base agents) to intelligently analyze user queries, dynamically retrieve semantic chunks from a local vector database, and generate precise, compliance-driven responses using a local Large Language Model (LLM). This system is custom-built to process highly structured engineering or business documents (such as .docx process guides) while ensuring absolute data privacy by running entirely on local infrastructure.

[⚙️ How It Works]

- The system operates across three core execution phases: Data Ingestion, Intelligent Routing, and Contextual Generation.

1. Document Ingestion & Vectorization (The Offline Pipeline)
Parsing: The document_service.py targets the core process file (KBIDE_Process.docx). The pipeline utilizes a custom loader.py to extract raw text, tables, and structural elements.

Chunking: The splitter.py segments the text into mathematically optimal, overlapping text chunks to preserve contextual continuity.

Embedding & Storage: These chunks are converted into dense vector embeddings via the embedding_service.py and committed to a local, persistent Chroma DB instance.

2. Query Handling & Intelligent Routing (The Agentic Core)
The user submits a query through the Streamlit web chat interface (chat.py).

The Agent Manager and Agent Factory instantiate the required runtime components.

The Router Agent analyzes the intent of the incoming query to determine if it requires deep document retrieval, direct general assistance, or specific process execution, routing the task dynamically to the Process Agent.

3. Context Retrieval & Local Generation (The RAG Loop)
The Process Agent triggers the rag_service.py orchestrator.

The system uses retriever.py to perform a semantic similarity search across the local Chroma DB, pulling the exact document chunks relevant to the user's inquiry.

The prompt_service.py injects this retrieved context alongside strict operational constraints into the system prompt.

The final, hydrated prompt is passed to ollama_service.py, which executes inference against a local Ollama LLM. The generated response is streamed seamlessly back to the UI.

[🛠️ Tech Stack Used]

The project is built entirely on a modular, enterprise-grade Python stack prioritizing performance, local execution, and strict decoupling of concerns.

💻 Frontend & User Interface
Streamlit: Powers the responsive, state-managed Web UI, chat panels, and operational sidebar settings components.

🧠 Agent Orchestration & Core Logic
Custom Multi-Agent Framework: Built natively using clean OOP design patterns (base_agent.py, agent_factory.py, agent_manager.py) to bypass heavy, unpredictable third-party agent packages and optimize latency.

🔍 Data Engineering & RAG Pipeline
ChromaDB: A lightweight, high-performance vector database utilized for persistent local storage and fast semantic similarity indexing.

Python-Docx / Unstructured Parsers: Tailored file parsing mechanisms used within loader.py to correctly extract text layouts from Microsoft Word (.docx) frameworks.

HuggingFace Embeddings (via Ollama/Local Transformers): Generates high-fidelity vector representations of documentation text.

🚀 Inference & Model Delivery
Ollama: Manages containerized local LLM deployments (e.g., Llama 3, Mistral, or Phi-3), exposing an efficient local API for text generation without reliance on external cloud APIs.

🧪 Quality Assurance & Monitoring
Pytest: Drives the integrated verification engine (run_tests.py) across individual data loaders, vector lookups, and agent state machines.

Native Logging: Monitors execution metrics, token retrieval accuracy, and system warnings.
