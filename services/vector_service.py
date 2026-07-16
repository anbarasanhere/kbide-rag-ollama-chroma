"""
Vector Service.
Responsible for creating and loading the Chroma database.
"""

from pathlib import Path
from config import settings

from rag.vector_store import VectorStore
from services.document_service import DocumentService
from services.embedding_service import EmbeddingService

from utils.logger import logger


class VectorService:

    def __init__(self):

        logger.info("Initializing Vector Service...")

        self.embedding = EmbeddingService().get_embedding_model()

        self.store = VectorStore(self.embedding)

    # -------------------------------------------------

    def exists(self) -> bool:

        '''Check whether a valid vector database exists.'''

        if not Path(settings.VECTOR_DB_PATH).exists():
            return False

        try:
            db = self.store.load()

            return db._collection.count() > 0

        except Exception:
            return False

    # -------------------------------------------------

    def load(self):

        logger.info("Loading existing Vector Database...")

        return self.store.load()

    # -------------------------------------------------

    def create(self):

        logger.info("Creating Vector Database...")

        document_service = DocumentService(
            settings.DOCUMENT_PATH
        )

        chunks = document_service.load_chunks()

        db = self.store.create(chunks)

        logger.info(f"Stored {len(chunks)} chunks.")

        return db

    # -------------------------------------------------

    def get_vector_db(self):

        if self.exists():

            logger.info("Loading existing Vector Database...")

            return self.load()

        logger.warning("Vector Database missing or empty.")

        logger.info("Creating new Vector Database...")

        return self.create()

    # -------------------------------------------------

    def rebuild(self):

        logger.warning("Rebuilding Vector Database...")

        import shutil

        shutil.rmtree(
            settings.VECTOR_DB_PATH,
            ignore_errors=True,
        )

        return self.create()

    def stats(self):

        db = self.get_vector_db()

        collection = db._collection

        return {
            "documents": collection.count(),
            "path": str(settings.VECTOR_DB_PATH),
            "embedding_model": settings.EMBEDDING_MODEL,
        }
