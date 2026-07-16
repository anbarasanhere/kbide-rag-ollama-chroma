"""
Chroma Vector Store.

Low-level wrapper around Chroma.
"""

from langchain_chroma import Chroma

from config import settings


class VectorStore:
    """
    Handles direct interaction with Chroma.
    """

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

    # -------------------------------------------------

    def create(self, chunks):

        return Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=str(settings.VECTOR_DB_PATH),
        )

    # -------------------------------------------------

    def load(self):

        return Chroma(
            persist_directory=str(settings.VECTOR_DB_PATH),
            embedding_function=self.embedding_model,
        )
