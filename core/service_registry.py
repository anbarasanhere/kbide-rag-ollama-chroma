"""
Service Registry

Defines all available application services.
"""

from enum import Enum


class ServiceType(str, Enum):
    """
    Application service identifiers.
    """

    LLM = "llm"

    EMBEDDING = "embedding"

    VECTOR = "vector"

    DOCUMENT = "document"

    RETRIEVER = "retriever"

    RAG = "rag"

    KNOWLEDGE_AGENT = "knowledge_agent"
