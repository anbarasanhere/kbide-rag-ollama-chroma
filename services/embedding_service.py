"""
Embedding Service.
"""

from langchain_ollama import OllamaEmbeddings
from config import settings
from utils.logger import logger


class EmbeddingService:
    """
    Creates embedding model.
    """

    def __init__(self):

        logger.info("Loading embedding model...")

        self.embedding = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL
        )

        logger.info("Embedding model loaded.")

    def get_embedding_model(self):
        """
        Return embedding model.
        """

        return self.embedding
