"""
Chat Component
"""

import streamlit as st

from services.rag_service import RAGService


class ChatComponent:

    def __init__(self):

        self.rag = RAGService()

        if "messages" not in st.session_state:
            st.session_state.messages = []

    # ---------------------------------------------------

    def render(self):

        st.title("🤖 KBIDE AI Assistant")

        self.show_welcome()

        self.show_history()

        self.handle_user_input()

    # ---------------------------------------------------

    def show_welcome(self):

        if len(st.session_state.messages) == 0:

            st.info(
                """
Welcome to KBIDE AI!

Ask any question related to your KBIDE Process Document.

Example Questions:

• What is Phantom AV?

• How do I create a project?

• How do I import PLC?

• How do I download the project?
"""
            )

    # ---------------------------------------------------

    def show_history(self):

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

    # ---------------------------------------------------

    def handle_user_input(self):

        question = st.chat_input(
            "Ask KBIDE AI..."
        )

        if not question:
            return

        self.process_question(question)

    # ---------------------------------------------------

    def process_question(self, question):

        # Display User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # Generate Answer

        with st.chat_message("assistant"):

            with st.spinner(
                "Searching KBIDE knowledge base..."
            ):

                try:

                    answer = self.rag.answer(question)

                except Exception as ex:

                    answer = f"Error:\n\n{ex}"

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
