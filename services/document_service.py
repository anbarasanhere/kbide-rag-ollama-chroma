"""
Document loading service.
"""

import streamlit as st

from rag.loader import DocumentLoader
from rag.chunker import Chunker


class DocumentService:

    def __init__(self, document_path):

        self.document_path = document_path

    @st.cache_resource
    def load_chunks(_self):

        loader = DocumentLoader(_self.document_path)

        documents = loader.load()

        chunker = Chunker()

        chunks = chunker.split(documents)

        return chunks