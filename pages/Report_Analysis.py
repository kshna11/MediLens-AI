import hashlib
import streamlit as st

from ai.gemini_helper import generate_summary
from utils.pdf_reader import extract_text_from_pdf
from utils.pdf_generator import create_summary_pdf

from rag.pdf_loader import load_pdf
from rag.text_splitter import split_documents
from rag.vector_store import create_vector_store

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Medical Report Analysis",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "current_file_hash" not in st.session_state:
    st.session_state.current_file_hash = ""

if "vector_created" not in st.session_state:
    st.session_state.vector_created = False

if "summary" not in st.session_state:
    st.session_state.summary = ""

# -------------------------------------------------
# Title
# -------------------------------------------------
st.title("📄 Medical Report Analysis")

st.write(
    "Upload your medical report in PDF format and let MediLens AI generate an intelligent medical summary."
)

# -------------------------------------------------
# Upload PDF
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

# -------------------------------------------------
# Process Uploaded File
# -------------------------------------------------
if uploaded_file is not None:

    # ---------------------------------------------
    # Detect New File using SHA-256
    # ---------------------------------------------
    file_bytes = uploaded_file.getvalue()

    file_hash = hashlib.sha256(file_bytes).hexdigest()

    if file_hash != st.session_state.current_file_hash:

        st.session_state.current_file_hash = file_hash
        st.session_state.vector_created = False
        st.session_state.summary = ""

    # ---------------------------------------------
    # Save Uploaded PDF
    # ---------------------------------------------
    with open("reports/temp.pdf", "wb") as file:
        file.write(file_bytes)

    # ---------------------------------------------
    # Extract Text
    # ---------------------------------------------
    report_text = extract_text_from_pdf("reports/temp.pdf")

    # ---------------------------------------------
    # Create FAISS Vector Database
    # ---------------------------------------------
    if not st.session_state.vector_created:

        with st.spinner("📚 Creating Medical Knowledge Base..."):

            documents = load_pdf("reports/temp.pdf")

            chunks = split_documents(documents)

            create_vector_store(chunks)

            st.session_state.vector_created = True

        st.toast("📚 Medical Knowledge Base Ready")

    # ---------------------------------------------
    # AI Summary
    # ---------------------------------------------
    st.divider()

    st.subheader("🤖 AI Medical Report Summary")

    if not st.session_state.summary:

        with st.spinner("🤖 Analyzing Medical Report..."):

            st.session_state.summary = generate_summary(report_text)

        st.toast("🤖 AI Summary Generated")

    # ---------------------------------------------
    # Display Summary
    # ---------------------------------------------
    with st.container(border=True):

        st.markdown(st.session_state.summary)

    # ---------------------------------------------
    # Export Section
    # ---------------------------------------------
    st.divider()

    st.subheader("📥 Export Report")

    pdf_path = create_summary_pdf(st.session_state.summary)

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            label="📥 Download AI Summary (PDF)",
            data=pdf,
            file_name="AI_Medical_Summary.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# -------------------------------------------------
# No File Uploaded
# -------------------------------------------------
else:

    st.info(
        "📄 Upload a medical report to generate an AI-powered summary."
    )