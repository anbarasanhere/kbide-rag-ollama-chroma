# KBIDE-AI: Multi-Agent Knowledge Orchestration Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-orange.svg)](https://ollama.com/)

An advanced, locally hosted Multi-Agent Retrieval-Augmented Generation (RAG) system designed to parse, index, and reason over technical process documentation (`.docx`) using structured agent orchestration.

<img width="3075" height="1507" alt="KBIDE-AI" src="https://github.com/user-attachments/assets/cd95d02e-8ba2-45e5-b695-a46bc4869664" />

📑 Project Overview
KBIDE-AI is an intelligent, locally-hosted Multi-Agent Retrieval-Augmented Generation (RAG) framework designed to transform static technical process documentation into an interactive, context-aware knowledge base.

Unlike traditional flat RAG pipelines, KBIDE-AI uses a decoupled, modular agentic architecture. It orchestrates a specialized team of agents (Router, Process, and Base agents) to intelligently analyze user queries, dynamically retrieve semantic chunks from a local vector database, and generate precise, compliance-driven responses using a local Large Language Model (LLM). This system is custom-built to process highly structured engineering or business documents (such as .docx process guides) while ensuring absolute data privacy by running entirely on local infrastructure.
