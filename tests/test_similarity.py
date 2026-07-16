from rag.retriever import Retriever

def main():

    print("=" * 60)
    print("SIMILARITY TEST")
    print("=" * 60)

    retriever = Retriever()

    query = input("Question: ")

    results = retriever.search_with_scores(query)

    for index, (doc, score) in enumerate(results, start=1):

        print("\n")
        print("=" * 50)

        print(f"Chunk {index}")

        print(f"Score : {score:.4f}")

        print()

        print(doc.page_content[:300])


if __name__ == "__main__":
    main()
