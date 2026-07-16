"""
RAG Service

Coordinates retrieval, prompt creation and LLM generation.
"""
import time
from rag.retriever import Retriever
from services.ollama_service import OllamaService
from services.prompt_service import PromptService

from utils.logger import logger


class RAGService:

    def __init__(self):

        logger.info("Initializing RAG Service...")

        self.retriever = Retriever()

        self.prompt_service = PromptService()

        self.llm = OllamaService()

    # -------------------------------------------------

    def answer(self, question: str) -> str:
        """
        Generate an answer using Retrieval-Augmented Generation.
        """

        total_start = time.perf_counter()

        # -----------------------------
        retrieval_start = time.perf_counter()

        context = self.retriever.get_context(question)

        retrieval_time = time.perf_counter() - retrieval_start

        if not context.strip():
            return "I couldn't find that information in the KBIDE process document."

        # -----------------------------
        prompt_start = time.perf_counter()

        prompt = self.prompt_service.build_prompt(
            question=question,
            context=context
        )

        prompt_time = time.perf_counter() - prompt_start

        # -----------------------------
        llm_start = time.perf_counter()

        answer = self.llm.invoke(prompt)

        llm_time = time.perf_counter() - llm_start

        total_time = time.perf_counter() - total_start

        print("\n" + "=" * 50)
        print("PERFORMANCE")
        print("=" * 50)
        print(f"Retrieval Time : {retrieval_time:.2f} sec")
        print(f"Prompt Time    : {prompt_time:.2f} sec")
        print(f"LLM Time       : {llm_time:.2f} sec")
        print(f"Total Time     : {total_time:.2f} sec")
        print("=" * 50 + "\n")

        return answer
