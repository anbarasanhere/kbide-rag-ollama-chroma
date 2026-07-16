"""
Ollama Service

Handles communication with the local LLM.
"""

from langchain_ollama import ChatOllama

from config import settings
from utils.logger import logger


class OllamaService:

    def __init__(self):

        logger.info("Initializing Ollama Service...")

        self.llm = ChatOllama(
            model=settings.CHAT_MODEL,
            temperature=0,
            num_predict=250,
            num_ctx=2048,
        )

    # -------------------------------------------------

    def invoke(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        content = response.content
        if isinstance(content, str):
            return content
        return str(content)
