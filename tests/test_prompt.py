from rag.retriever import Retriever
from services.prompt_service import PromptService


def main():

    print("=" * 60)
    print("PROMPT SERVICE TEST")
    print("=" * 60)

    question = input("\nQuestion: ")

    retriever = Retriever()

    context = retriever.get_context(question)

    prompt_service = PromptService()

    prompt = prompt_service.build_prompt(

        question=question,

        context=context

    )

    print("\n")
    print("=" * 60)
    print("FINAL PROMPT")
    print("=" * 60)

    print(prompt)

    print("\nSUCCESS")


if __name__ == "__main__":
    main()
