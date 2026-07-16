"""
Prompt Service:
Loads and prepares prompts for the LLM.
"""

from pathlib import Path

from config import settings
from utils.logger import logger


class PromptService:
    """
    Handles prompt loading and formatting.
    """

    def __init__(self):

        logger.info("Initializing Prompt Service...")

        self.template = self._load_prompt()

    # -------------------------------------------------

    def _load_prompt(self) -> str:

        path = Path(settings.PROMPT_PATH)

        if not path.exists():

            raise FileNotFoundError(
                f"Prompt file not found: {path}"
            )

        logger.info("System prompt loaded.")

        return path.read_text(
            encoding="utf-8"
        )

    # -------------------------------------------------

    def build_prompt(
        self,
        question: str,
        context: str
    ) -> str:

        prompt = self.template.format(

            question=question,

            context=context

        )

        return prompt
