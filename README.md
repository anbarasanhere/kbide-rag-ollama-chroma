# KBIDE-AI: Multi-Agent Knowledge Orchestration Framework

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

[KBIDE_Process.docx] ──> Ingestion & Embedding ──> [Chroma DB]
                                                        │
[User Query] ──> [Router Agent] ──> [Process Agent] ────┤ (Context Retrieval)
                                        │
                                  [Ollama LLM] ──> [Streamlit UI Response]


graph TD
    %% Style Definitions
    classDef ui fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef agent fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px;
    classDef service fill:#e0f7fa,stroke:#006064,stroke-width:2px;
    classDef storage fill:#f5f5f5,stroke:#212121,stroke-width:2px;
    classDef utility fill:#ffffff,stroke:#9e9e9e,stroke-width:1px,stroke-dasharray: 5 5;

    %% --- USER INTERFACE LAYER ---
    subgraph UI [USER INTERFACE Streamlit]
        app[app.py<br>Entry Point]
        sidebar[sidebar.py]
        chat[chat.py<br>Chat Interface]
    end

    %% --- AGENT ORCHESTRATION LAYER ---
    subgraph Orchestration [AGENT ORCHESTRATION]
        manager[agent_manager.py]
        factory[agent_factory.py]
        router[router_agent.py]
        process[process_agent.py]
        base[base_agent.py]
    end

    %% --- SERVICES & RAG LAYER ---
    subgraph Services [SERVICES & LOGIC]
        doc_svc[document_service.py]
        embed_svc[embedding_service.py]
        vector_svc[vector_service.py]
        ollama_svc[ollama_service.py]
        prompt_svc[prompt_service.py]
        
        subgraph RAG [RAG System]
            rag_svc[rag_service.py<br>Orchestrator]
            loader[loader.py]
            splitter[splitter.py]
            retriever[retriever.py]
        end
    end

    %% --- DATA & STORAGE LAYER ---
    subgraph Storage [DATA & STORAGE]
        docx[(documents/<br>KBIDE_Process.docx)]
        ollama_llm[Ollama LLM]
        chroma[(vector_db/<br>Chroma Persistent Storage)]
    end

    %% --- UTILITY & MAINTENANCE ---
    subgraph Utility [Utility & Maintenance]
        config[config.py]
        rebuild[rebuild_vector_db.py]
        tests[run_tests.py]
    end

    %% --- FLOW RELATIONSHIPS ---
    
    %% UI to Orchestration
    app --> manager
    app --- sidebar
    app --- chat
    chat -->|User Query| router
    chat -->|User Query| process

    %% Agent Internal Routing
    manager -->|Manage instances| factory
    factory --> router
    factory --> process
    factory --> base
    router -->|Call to agents| process
    router --> base

    %% Agents to Services
    process --> doc_svc
    process --> ollama_svc
    base --> rag_svc

    %% Services to Data/Storage
    docx --> doc_svc
    vector_svc --> chroma
    ollama_svc --> ollama_llm

    %% RAG Internal & Database Mapping
    rag_svc --> loader
    rag_svc --> splitter
    rag_svc --> retriever
    
    loader --> chroma
    splitter --> chroma
    retriever --> chroma

    %% Utilities
    rebuild --> chroma

    %% Response Loop
    rag_svc -->|Agent Response / Information Flow| chat

    %% Assigning styles
    class app,sidebar,chat ui;
    class manager,factory,router,process,base agent;
    class doc_svc,embed_svc,vector_svc,ollama_svc,prompt_svc,rag_svc,loader,splitter,retriever service;
    class docx,ollama_llm,chroma storage;
    class config,rebuild,tests utility;
