from fastapi import FastAPI

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict

app = FastAPI()

# Loaded once at startup and kept in memory for all requests
model = load_model()


@app.get("/")
def welcome_root() -> dict[str, str]:
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict")
def predict_iris(request: PredictRequest) -> PredictResponse:
    features = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = predict(model, features)
    return PredictResponse(prediction=prediction)
