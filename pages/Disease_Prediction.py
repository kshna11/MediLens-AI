import streamlit as st
import numpy as np

from ml.predictor import (
    load_model,
    load_scaler,
    predict
)

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------------------------
# Load Model
# -------------------------------------------------
model = load_model("models/diabetes_model.pkl")
scaler = load_scaler("models/scaler.pkl")

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🧠 Diabetes Risk Prediction")

st.write(
    "Enter the patient's clinical information below to predict the risk of diabetes using our Machine Learning model."
)

st.divider()

# -------------------------------------------------
# Input Form
# -------------------------------------------------
with st.container(border=True):

    st.subheader("📝 Patient Information")

    col1, col2 = st.columns(2)

    with col1:

        pregnancies = st.number_input(
            "Pregnancies",
            0, 20, 1
        )

        glucose = st.number_input(
            "Glucose",
            0, 250, 120
        )

        blood_pressure = st.number_input(
            "Blood Pressure",
            0, 150, 70
        )

        skin = st.number_input(
            "Skin Thickness",
            0, 100, 20
        )

    with col2:

        insulin = st.number_input(
            "Insulin",
            0, 900, 80
        )

        bmi = st.number_input(
            "BMI",
            0.0, 70.0, 30.0
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function",
            0.0, 3.0, 0.5
        )

        age = st.number_input(
            "Age",
            1, 120, 30
        )

    predict_btn = st.button(
        "🩺 Predict Diabetes Risk",
        use_container_width=True
    )

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if predict_btn:

    with st.spinner("🧠 Running Machine Learning Model..."):

        user_input = np.array([
            pregnancies,
            glucose,
            blood_pressure,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ])

        prediction, probability = predict(
            model,
            scaler,
            user_input
        )

    confidence = max(probability) * 100

    st.divider()

    st.subheader("🩺 Prediction Result")

    if prediction == 1:

        st.error("🔴 **High Risk of Diabetes**")

    else:

        st.success("🟢 **Low Risk of Diabetes**")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)

    st.divider()

    st.subheader("💡 Health Recommendations")

    if prediction == 1:

        st.warning("""
- 🥗 Reduce sugar intake.

- 🚶 Exercise at least 30 minutes daily.

- ⚖ Maintain a healthy body weight.

- 💧 Stay hydrated.

- 🩺 Consult a healthcare professional.

- 📅 Monitor blood glucose regularly.
""")

    else:

        st.success("""
- 🥗 Maintain a balanced diet.

- 🚶 Continue regular exercise.

- 💧 Drink plenty of water.

- 😴 Get adequate sleep.

- 🩺 Schedule routine health checkups.
""")

    st.divider()

    st.subheader("📋 Patient Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Pregnancies", pregnancies)
        st.metric("Glucose", glucose)
        st.metric("Blood Pressure", blood_pressure)
        st.metric("Skin Thickness", skin)

    with col2:

        st.metric("Insulin", insulin)
        st.metric("BMI", bmi)
        st.metric("Diabetes Pedigree", dpf)
        st.metric("Age", age)

    st.divider()

    st.info(
        "⚠ **Disclaimer:** This prediction is generated using a Machine Learning model and is intended for educational purposes only. It should not replace professional medical advice or diagnosis."
    )