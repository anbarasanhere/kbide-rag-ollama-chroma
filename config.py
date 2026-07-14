"""
Application Configuration

Centralized configuration for KBIDE AI.
"""

from pathlib import Path


class Settings:
    """
    Application settings.
    """

    # =====================================================
    # Project Paths
    # =====================================================

    BASE_DIR = Path(__file__).resolve().parent

    DOCUMENTS_DIR = BASE_DIR / "documents"

    VECTOR_DB_PATH = BASE_DIR / "vector_db"

    PROMPTS_DIR = BASE_DIR / "prompts"

    LOG_DIR = BASE_DIR / "logs"

    # =====================================================
    # Files
    # =====================================================

    # Change this if your document name changes
    DOCUMENT_PATH = DOCUMENTS_DIR / "kbide.docx"

    PROMPT_PATH = PROMPTS_DIR / "system_prompt.txt"

    # =====================================================
    # Ollama Models
    # =====================================================

    CHAT_MODEL = "qwen2.5:3b"

    EMBEDDING_MODEL = "nomic-embed-text"

    # =====================================================
    # Chunking
    # =====================================================

    CHUNK_SIZE = 700

    CHUNK_OVERLAP = 100

    # =====================================================
    # Retrieval
    # =====================================================

    TOP_K = 2

    # =====================================================
    # Streamlit
    # =====================================================

    APP_TITLE = "KBIDE AI Assistant"

    PAGE_ICON = "🤖"

    LAYOUT = "wide"

    # =====================================================
    # Logging
    # =====================================================

    LOG_LEVEL = "INFO"


settings = Settings()
