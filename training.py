from typing import Any

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

MODEL_PATH = "model.joblib"


def load_data() -> tuple[Any, Any]:
    """Load iris features (X) and class labels (y)."""
    features, labels = load_iris(return_X_y=True)
    return features, labels


def train_model(features: Any, labels: Any) -> LogisticRegression:
    """Train a logistic regression classifier."""
    model = LogisticRegression(max_iter=200)
    model.fit(features, labels)
    return model


def save_model(model: LogisticRegression, model_path: str = MODEL_PATH) -> None:
    """Serialize the trained model to disk."""
    joblib.dump(model, model_path)


if __name__ == "__main__":
    features, labels = load_data()
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )
    model = train_model(train_features, train_labels)
    accuracy = model.score(test_features, test_labels)
    print(f"Test accuracy: {accuracy:.2f}")
    save_model(model)
    print(f"Model saved to {MODEL_PATH}")
