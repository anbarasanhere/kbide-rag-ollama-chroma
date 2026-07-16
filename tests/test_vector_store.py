from config import settings
from rag.loader import DocumentLoader
from rag.chunker import Chunker

from services.embedding_service import EmbeddingService

from services.vector_service import VectorService


def main():

    print("=" * 60)
    print("TEST 4 : VECTOR DATABASE")
    print("=" * 60)

    loader = DocumentLoader(settings.DOCUMENT_PATH)

    docs = loader.load()

    chunker = Chunker()

    chunks = chunker.split(docs)

    embedding = EmbeddingService().get_embedding_model()

    vector_db = VectorService().create_vector_db(chunks)

    print("\nVector DB Created Successfully")

    print(f"Chunks Stored : {len(chunks)}")

    print("\nSUCCESS")


if __name__ == "__main__":
    main()