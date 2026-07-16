"""
Retriever Module
Handles document retrieval from the vector database.
"""

from config import settings
from services.vector_service import VectorService
from utils.logger import logger


class Retriever:
    """
    Retrieves relevant chunks from the vector database.
    """

    def __init__(self):

        logger.info("Initializing Retriever...")

        self.vector_db = VectorService().get_vector_db()

        self.retriever = self.vector_db.as_retriever(

            search_kwargs={
                "k": settings.TOP_K
            }

        )

    # -----------------------------------------------------

    def search(self, query: str):

        logger.info(f"Searching for: {query}")

        documents = self.retriever.invoke(query)

        logger.info(f"Retrieved {len(documents)} chunks.")

        return documents

    # -----------------------------------------------------

    def search_with_scores(self, query: str):
        """
        Retrieve documents with similarity scores.
        Useful for debugging and future UI enhancements.
        """

        logger.info(f"Searching with scores: {query}")

        results = self.vector_db.similarity_search_with_score(
            query,
            k=settings.TOP_K
        )

        return results

    def get_context(self, query: str) -> str:
        """
        Return retrieved chunks as a single formatted string.
        """

        documents = self.search(query)

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        return context
