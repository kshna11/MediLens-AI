import pandas as pd
import joblib
from ml.data_loader import load_data

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



def replace_invalid_values(df):
    """
    Replace medically impossible zero values with
    the median value of each column.
    """

    columns = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI"
    ]

    for col in columns:

        median = df[col].median()

        df[col] = df[col].replace(0, median)

    print("\nInvalid values replaced successfully!\n")

    return df


def split_features_target(df):
    """
    Separate input features and target variable.
    """

    # Input Features
    X = df.drop("Outcome", axis=1)

    # Target Variable
    y = df["Outcome"]

    print("\nFeatures Shape :", X.shape)
    print("Target Shape   :", y.shape)

    return X, y


def split_dataset(X, y):
    """
    Split the dataset into training and testing sets.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    print("\nDataset Split Successfully!\n")

    print("Training Features :", X_train.shape)
    print("Testing Features  :", X_test.shape)
    print("Training Target   :", y_train.shape)
    print("Testing Target    :", y_test.shape)

    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):
    """
    Scale the training and testing features.
    """

    scaler = StandardScaler()

    # Learn from training data and transform it
    X_train = scaler.fit_transform(X_train)

    # Transform test data using same scaler
    X_test = scaler.transform(X_test)

    print("\nFeature Scaling Completed Successfully!")

    return X_train, X_test, scaler


def save_scaler(scaler):
    """
    Save the trained scaler.
    """

    joblib.dump(scaler, "models/scaler.pkl")

    print("\nScaler saved successfully!")




def main():

    # Load dataset
    df = load_data("data/diabetes.csv")

    # Replace invalid values
    df = replace_invalid_values(df)

    # Split Features & Target
    X, y = split_features_target(df)

    # Train-Test Split
    X_train, X_test, y_train, y_test = split_dataset(X, y)
    
    X_train, X_test, scaler = scale_features(
    X_train,
    X_test
    )
    
    # Save Scaler
    save_scaler(scaler)
    print("\nPreprocessing Completed Successfully!")

    
    
if __name__ == "__main__":
    main()