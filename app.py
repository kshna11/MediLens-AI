import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MediLens AI",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Sidebar Branding
# -----------------------------
st.sidebar.markdown(
    """
# 🧠 MediLens AI

### AI Healthcare Assistant
"""
)

st.sidebar.divider()

# -----------------------------
# Pages
# -----------------------------
home = st.Page(
    "pages/Home.py",
    title="Home",
    icon="🏠"
)

prediction = st.Page(
    "pages/Disease_Prediction.py",
    title="Disease Prediction",
    icon="🧠"
)

report = st.Page(
    "pages/Report_Analysis.py",
    title="Report Analysis",
    icon="📄"
)

chatbot = st.Page(
    "pages/Medical_Chatbot.py",
    title="Medical Chatbot",
    icon="💬"
)

about = st.Page(
    "pages/About.py",
    title="About",
    icon="ℹ️"
)

# -----------------------------
# Navigation
# -----------------------------
pg = st.navigation(
    [
        home,
        prediction,
        report,
        chatbot,
        about
    ]
)

# -----------------------------
# Run App
# -----------------------------
pg.run()