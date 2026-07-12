import joblib


def load_model(model_path):
    """
    Load the trained ML model.
    """

    return joblib.load(model_path)


def load_scaler(scaler_path):
    """
    Load the trained scaler.
    """

    return joblib.load(scaler_path)


def predict(model, scaler, user_input):
    """
    Predict diabetes for user input.
    """

    scaled_input = scaler.transform([user_input])

    prediction = model.predict(scaled_input)

    probability = model.predict_proba(scaled_input)

    return prediction[0], probability[0]