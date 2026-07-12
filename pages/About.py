import streamlit as st

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("ℹ️ About MediLens AI")

st.write(
    """
**MediLens AI** is an intelligent healthcare assistant that combines
**Machine Learning**, **Google Gemini AI**, and
**Retrieval-Augmented Generation (RAG)** to assist users in
analyzing medical reports, predicting diabetes risk,
and answering medical questions.
"""
)

st.divider()

# -------------------------------------------------
# Project Overview
# -------------------------------------------------
st.header("📌 Project Overview")

st.info("""
MediLens AI helps users:

✅ Predict diabetes risk using Machine Learning.

✅ Analyze medical reports using Google Gemini AI.

✅ Ask intelligent questions based on uploaded reports.

✅ Receive personalized lifestyle recommendations.

✅ Download AI-generated medical summaries.
""")

st.divider()

# -------------------------------------------------
# Features
# -------------------------------------------------
st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🤖 Artificial Intelligence

- Google Gemini AI
- AI Medical Summary
- AI Medical Chatbot
- Personalized Recommendations
""")

    st.info("""
### 📄 Report Analysis

- PDF Upload
- Text Extraction
- AI Summary
- Download Summary as PDF
""")

with col2:

    st.warning("""
### 🩺 Disease Prediction

- Diabetes Prediction
- Random Forest Model
- Confidence Score
- Health Recommendations
""")

    st.error("""
### 💬 Medical Chatbot

- RAG Powered
- FAISS Vector Database
- Context-Aware Responses
- Medical Knowledge Integration
""")

st.divider()

# -------------------------------------------------
# Technology Stack
# -------------------------------------------------
st.header("🛠 Technology Stack")

st.markdown("""
- 🐍 Python
- 🎨 Streamlit
- 🤖 Google Gemini AI
- 🧠 LangChain
- 📚 FAISS
- 📄 PyPDF2
- 🤖 Scikit-learn
- 🔢 NumPy
- 🗂 Pickle
""")

st.divider()

# -------------------------------------------------
# Project Workflow
# -------------------------------------------------
st.header("⚙️ Project Workflow")

st.code("""
Medical Report
        │
        ▼
Upload PDF
        │
        ▼
Extract Text
        │
        ▼
Create FAISS Vector Database
        │
        ▼
Generate AI Summary
        │
        ▼
Medical Chatbot (RAG)
""")

st.divider()

# -------------------------------------------------
# Future Scope
# -------------------------------------------------
st.header("🔮 Future Scope")

st.markdown("""
- 🧠 Multi-disease prediction
- 🩺 Medicine recommendation
- 📱 Mobile application
- 🌐 Multi-language support
- ☁️ Cloud deployment
- 🏥 Hospital integration
""")

st.divider()

# -------------------------------------------------
# Developer
# -------------------------------------------------
st.header("👨‍💻 Developer")

st.success("""
**Krishna Jaiswal**

B.Tech - Data Science

Python | Machine Learning | Generative AI | RAG | Streamlit
""")

st.divider()

# -------------------------------------------------
# Disclaimer
# -------------------------------------------------
st.info(
    "⚠️ MediLens AI is intended for educational and informational purposes only. "
    "It should not replace professional medical advice, diagnosis, or treatment."
)