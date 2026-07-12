import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from ml.data_loader import load_data
from ml.preprocessing import (
    replace_invalid_values,
    split_features_target,
    split_dataset,
    scale_features
)
from ml.evaluator import evaluate_model


def train_models(X_train, X_test, y_train, y_test):
    """
    Train and compare multiple ML models.
    """

    models = {

        "Logistic Regression": LogisticRegression(),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            random_state=42
        )

    }

    results = []

    best_model = None
    best_accuracy = 0
    best_f1 = 0
    best_model_name = ""

    for name, model in models.items():

        model.fit(X_train, y_train)

        accuracy, precision, recall, f1 = evaluate_model(
            model,
            X_test,
            y_test
        )

        results.append([
            name,
            accuracy,
            precision,
            recall,
            f1
        ])

        if (
            accuracy > best_accuracy or
            (accuracy == best_accuracy and f1 > best_f1)
        ):

            best_accuracy = accuracy
            best_f1 = f1
            best_model = model
            best_model_name = name

    results_df = pd.DataFrame(
        results,
        columns=[
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ]
    )

    print("\n========== MODEL COMPARISON ==========\n")
    print(results_df.to_string(index=False))
    
    print("\n========== BEST MODEL ==========\n")
    print(f"Model    : {best_model_name}")
    print(f"Accuracy : {best_accuracy:.4f}")
    print(f"F1 Score : {best_f1:.4f}")

    return best_model


def save_model(model):

    joblib.dump(
        model,
        "models/diabetes_model.pkl"
    )

    print("\nBest model saved successfully!")
    
    
def main():

    # Load Dataset
    df = load_data("data/diabetes.csv")

    # Preprocessing
    df = replace_invalid_values(df)

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = split_dataset(
        X,
        y
    )

    X_train, X_test, scaler = scale_features(
        X_train,
        X_test
    )

    # Train Models
    best_model = train_models(
        X_train,
        X_test,
        y_train,
        y_test
    )

    # Save Best Model
    save_model(best_model)

    print("\nTraining Pipeline Completed Successfully!")
    
    
if __name__ == "__main__":
    main()