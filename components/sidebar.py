"""
Sidebar Component
Displays application information and controls.
"""

import streamlit as st
from config import settings
from services.vector_service import VectorService


class Sidebar:

    def __init__(self):

        self.vector_service = VectorService()

    # --------------------------------------------------------

    def render(self):

        with st.sidebar:

            st.title("🤖 KBIDE AI")

            st.caption("Version 1.0")

            st.divider()

            self._show_system_info()

            st.divider()

            self._show_database_info()

            st.divider()

            self._show_actions()

    # --------------------------------------------------------

    def _show_system_info(self):

        st.subheader("System")

        st.write(f"**Chat Model**")
        st.code(settings.CHAT_MODEL)

        st.write(f"**Embedding Model**")
        st.code(settings.EMBEDDING_MODEL)

    # --------------------------------------------------------

    def _show_database_info(self):

        st.subheader("Knowledge Base")

        try:

            db = self.vector_service.get_vector_db()

            chunk_count = db._collection.count()

            st.metric(
                label="Indexed Chunks",
                value=chunk_count
            )

            st.success("Knowledge Base Ready")

        except Exception:

            st.error("Knowledge Base Not Found")

    # --------------------------------------------------------

    def _show_actions(self):

        st.subheader("Actions")

        if st.session_state.get("messages"):

            if st.button(
                "🗑 Clear Conversation",
                use_container_width=True
            ):

                st.session_state.messages = []

                st.rerun()
