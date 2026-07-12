import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="MediLens AI",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------------------------
# Hero Section
# -------------------------------------------------
col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/logo.png", width=120)

with col2:
    st.markdown("# 🧠 MediLens AI")
    st.markdown("### AI-Powered Healthcare Assistant")
    st.write(
        "An intelligent healthcare platform powered by **Machine Learning**, "
        "**Google Gemini AI**, and **Retrieval-Augmented Generation (RAG)**."
    )

st.divider()

# -------------------------------------------------
# Introduction
# -------------------------------------------------
st.markdown("""
Welcome to **MediLens AI** 👋

Our platform helps users analyze medical reports, predict disease risk,
and ask intelligent health-related questions using AI.

### 🚀 Key Features

- 🤖 Machine Learning Disease Prediction
- 📄 AI Medical Report Analysis
- 💬 RAG-based Medical Chatbot
- 🧠 Google Gemini AI Integration
""")

st.divider()

# -------------------------------------------------
# Feature Cards
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    st.info("""
## 📊 Disease Prediction

✔ Diabetes Risk Prediction

✔ Random Forest ML Model

✔ Instant Risk Analysis
""")

    st.success("""
## 📄 Report Analysis

✔ Upload Medical Reports

✔ AI Generated Summary

✔ PDF Text Extraction
""")

with col2:

    st.warning("""
## 💬 Medical Chatbot

✔ Ask Questions About Reports

✔ RAG Powered Responses

✔ Personalized Medical Guidance
""")

    st.error("""
## ⚙️ Technologies Used

✔ Python

✔ LangChain

✔ Google Gemini AI
""")

st.divider()

# -------------------------------------------------
# Project Workflow
# -------------------------------------------------
st.subheader("🚀 Project Workflow")

st.code("""
📄 Upload Medical Report
            │
            ▼
📖 Extract PDF Text
            │
            ▼
🧩 Split into Text Chunks
            │
            ▼
🗂 Create FAISS Vector Database
            │
            ▼
🤖 Generate AI Summary
            │
            ▼
💬 Ask Questions to AI Chatbot
""")

st.divider()

# -------------------------------------------------
# Project Highlights
# -------------------------------------------------
st.subheader("✨ Why MediLens AI?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🩺 Disease Prediction", "✔")

with col2:
    st.metric("📄 Report Analysis", "✔")

with col3:
    st.metric("💬 AI Chatbot", "✔")

with col4:
    st.metric("🤖 Gemini AI", "Integrated")

st.divider()

# -------------------------------------------------
# Footer
# -------------------------------------------------
