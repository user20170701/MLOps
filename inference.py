import joblib
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "model.joblib"
IRIS_CLASS_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(model_path: str = MODEL_PATH) -> LogisticRegression:
    """Load the trained model from disk."""
    return joblib.load(model_path)


def predict(model: LogisticRegression, features: list[float]) -> str:
    """Predict the iris species for a single sample of 4 features."""
    class_index = model.predict([features])[0]
    return IRIS_CLASS_NAMES[class_index]
