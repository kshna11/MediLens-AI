import streamlit as st

from rag.chatbot import ask_question

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🤖 MediLens AI Assistant")

st.write(
    """
Ask anything about your **uploaded medical report**.

The chatbot first analyzes your uploaded report and then combines it with
medical knowledge to provide personalized, easy-to-understand answers.
"""
)

st.divider()

# -------------------------------------------------
# Suggested Questions
# -------------------------------------------------
with st.expander("💡 Suggested Questions", expanded=False):

    st.markdown("""
- 📄 Summarize my report
- 📊 What are the abnormal values?
- 🩺 Am I at risk of diabetes?
- 🥗 What foods should I eat?
- 🏃 What lifestyle changes should I make?
- 💊 What precautions should I take?
- ❤️ Explain my cholesterol levels.
- 🧪 Is my potassium level normal?
- 🚶 What exercises are recommended for me?
""")

# -------------------------------------------------
# Chat History
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# Chat Input
# -------------------------------------------------
question = st.chat_input(
    "Type your medical question here..."
)

# -------------------------------------------------
# Process Question
# -------------------------------------------------
if question:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("🤖 Analyzing your medical report..."):

            answer = ask_question(question)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# -------------------------------------------------
# Bottom Section
# -------------------------------------------------
st.write("")

col1, col2 = st.columns([1, 5])

with col1:

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

with col2:

    st.info(
        "⚠ **Disclaimer:** This chatbot provides AI-generated information "
        "based on your uploaded medical report. "
        "The responses are for educational purposes only and should not "
        "replace professional medical advice."
    )