"""
Common helper functions.
"""

from pathlib import Path


def folder_exists(path: Path) -> bool:
    """
    Check whether a folder exists.
    """
    return path.exists()


def create_folder(path: Path):
    """
    Create folder if it does not exist.
    """
    path.mkdir(parents=True, exist_ok=True)


def format_sources(documents):

    sources = []

    for index, doc in enumerate(documents, start=1):

        sources.append(
            {
                "id": index,
                "content": doc.page_content
            }
        )

    return sources
