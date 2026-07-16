from rag.retriever import Retriever

def main():

    print("=" * 60)
    print("RETRIEVER TEST")
    print("=" * 60)

    retriever = Retriever()

    query = input("\nEnter Question: ")

    docs = retriever.search(query)

    print("\n")
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)

    for index, doc in enumerate(docs, start=1):

        print(f"\nChunk {index}")
        print("-" * 40)

        print(doc.page_content[:500])

    print("\nSUCCESS")


if __name__ == "__main__":
    main()
