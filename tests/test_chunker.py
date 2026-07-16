from config import settings
from rag.loader import DocumentLoader
from rag.chunker import Chunker


def main():
    print("=" * 60)
    print("TEST 2 : DOCUMENT CHUNKING")
    print("=" * 60)

    loader = DocumentLoader(settings.DOCUMENT_PATH)

    docs = loader.load()

    chunker = Chunker()

    chunks = chunker.split(docs)

    print(f"\nTotal Chunks : {len(chunks)}")

    print("\nFirst Chunk\n")

    print(chunks[0].page_content)

    print("\nSUCCESS")


if __name__ == "__main__":
    main()