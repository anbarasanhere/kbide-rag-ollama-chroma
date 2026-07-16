from services.rag_service import RAGService

def main():

    print("=" * 60)
    print("RAG SERVICE TEST")
    print("=" * 60)

    rag = RAGService()

    while True:

        question = input("\nAsk a question ('exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = rag.answer(question)

        print("\n")
        print("=" * 60)
        print("ANSWER")
        print("=" * 60)

        print(answer)


if __name__ == "__main__":
    main()
