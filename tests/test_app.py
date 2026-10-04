from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_returns_welcome_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_setosa_for_setosa_sample() -> None:
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert response.json() == {"prediction": "setosa"}


def test_predict_rejects_invalid_input() -> None:
    response = client.post("/predict", json={"sepal_length": "abc"})

    assert response.status_code == 422
