# this file will contain the configuration settings for the application
from pathlib import Path

BASE_DIR = Path(__file__).parent

DOCUMENTS_DIR = BASE_DIR / "documents"

VECTOR_DB_DIR = BASE_DIR / "vector_db"

PROMPTS_DIR = BASE_DIR / "prompts"

ASSETS_DIR = BASE_DIR / "assets"