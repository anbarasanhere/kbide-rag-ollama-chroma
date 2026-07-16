from config import settings
from rag.loader import DocumentLoader


def main():

    print("=" * 60)
    print("TEST 1 : DOCUMENT LOADER")
    print("=" * 60)

    loader = DocumentLoader(settings.DOCUMENT_PATH)

    documents = loader.load()

    print(f"\nDocument Count : {len(documents)}")

    print("\nFirst 500 Characters:\n")

    print(documents[0].page_content[:500])

    print("\n\nSUCCESS")


if __name__ == "__main__":
    main()