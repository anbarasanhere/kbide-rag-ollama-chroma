import streamlit as st

from services.ollama_service import OllamaService

st.set_page_config(
    page_title="KBIDE AI",
    layout="wide"
)

st.title("🤖 KBIDE AI Assistant")

llm = OllamaService()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = llm.generate_response(prompt)

    # st.write(type(answer))
    # st.write(answer)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.sidebar:

        st.header("KBIDE AI")

        st.success("🟢 Ollama Connected")

        st.info("Model: qwen2.5:3b")

        st.divider()

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()