# Enterprise Knowledge Base RAG Assistant
## Overview


# Designed and implemented an end-to-end Retrieval-Augmented Generation (RAG) pipeline using LangChain, Ollama, and ChromaDB for intelligent enterprise document search.
# Developed an automated document ingestion pipeline supporting semantic chunking, embedding generation, metadata extraction, and persistent vector storage for efficient retrieval.
# Integrated locally hosted LLMs through Ollama, eliminating dependency on cloud APIs and ensuring complete privacy of confidential organizational documents.
Implemented semantic similarity search using vector embeddings to retrieve contextually relevant knowledge before response generation, significantly improving answer accuracy over standalone LLM responses.
Engineered modular components for document preprocessing, embedding generation, vector indexing, retrieval, prompt construction, and response generation following scalable software engineering principles.
Built configurable prompt engineering workflows to reduce hallucinations and improve factual grounding by injecting retrieved contextual information into LLM prompts.
Designed persistent vector database architecture using ChromaDB, enabling incremental knowledge base updates without rebuilding embeddings.
Optimized retrieval latency through efficient chunking strategies and Top-K semantic retrieval, enabling near real-time document question answering.

- Knowledge Agent
- Troubleshooting Agent
- Rule Explanation Agent

### Technology Stack

- Python
- Streamlit
- ollama
- Langchain
- ChromaDB

### Questions can be asked

1. What is Phantom AV?
2. Who is KE and what they do ?
3. Explain the types of BIOS ?
4. How many tabs SCM file contains ?
5. Explain all the stages of KBIDE

### Technology Used

| Category         | Technologies                         |
| ---------------- | ------------------------------------ |
| Programming      | Python                               |
| LLM Framework    | LangChain                            |
| Local LLM        | Ollama                               |
| Vector Database  | ChromaDB                             |
| Embedding Models | Ollama Embeddings / Local Embeddings |
| AI Technique     | Retrieval-Augmented Generation (RAG) |
| Retrieval        | Semantic Vector Search               |
| Prompting        | Context Injection                    |
| Storage          | Persistent Vector Store              |
| Deployment       | Local Offline Environment            |
