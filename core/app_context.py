"""
Application Context

Lazy-loaded service container.
"""

from typing import Any, Callable

from core.service_registry import ServiceType

from services.embedding_service import EmbeddingService
from services.ollama_services import OllamaService

from utils.logger import logger


class AppContext:
    """
    Singleton application context.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if getattr(self, "_initialized", False):
            return

        self._initialized = True

        self._services: dict[ServiceType, Any] = {}

        logger.info("Application Context Created")

    # ---------------------------------------------
    # Generic Service Loader
    # ---------------------------------------------

    def _resolve(
        self,
        service: ServiceType,
        factory: Callable[[], Any]
    ) -> Any:

        if service not in self._services:

            logger.info(f"Loading {service.value} service")

            self._services[service] = factory()

        return self._services[service]

    # ---------------------------------------------
    # LLM
    # ---------------------------------------------

    @property
    def llm(self) -> OllamaService:

        return self._resolve(
            ServiceType.LLM,
            OllamaService
        )

    # ---------------------------------------------
    # Embedding
    # ---------------------------------------------

    @property
    def embedding(self) -> EmbeddingService:

        return self._resolve(
            ServiceType.EMBEDDING,
            EmbeddingService
        )


context = AppContext()
