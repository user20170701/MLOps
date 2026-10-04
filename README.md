# MLOps

**English** | [Polski](README.pl.md)

MLOps course project: serving an ML model with FastAPI and Docker.

## Lab 1: Introduction to MLOps

The application exposes a REST API with a model that classifies iris species
(setosa, versicolor, virginica) based on 4 flower measurements.

## Tools

- **uv**: dependency management (`pyproject.toml`, `uv.lock`)
- **pre-commit**: Ruff (linter and formatter) and Xenon (code complexity)
- **pydantic-settings** and `.env` files: configuration for dev, test and prod environments
- **sops** and GPG: secrets encryption (`secrets.yaml`)
- **FastAPI**: web server with `/`, `/health` and `/predict` endpoints
- **pytest**: configuration and API tests
- **Docker** and Docker Compose: application containerization

## Project structure

| File / directory | Description |
|---|---|
| `training.py` | trains the model and saves it to `model.joblib` |
| `inference.py` | loads the model and runs predictions |
| `app.py` | FastAPI server |
| `api/models/` | Pydantic request and response models |
| `settings.py`, `main.py` | configuration and secrets loading |
| `config/` | `.env` files for each environment |
| `tests/` | tests |

## Usage

Install dependencies:

```bash
uv sync
```

Train the model:

```bash
uv run python training.py
```

Run the server locally (API docs: http://localhost:8000/docs):

```bash
uv run uvicorn app:app --reload --port 8000
```

Run tests:

```bash
uv run pytest tests -rP
```

Run with Docker:

```bash
docker compose up
```

## Example request

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

Response:

```json
{"prediction": "setosa"}
```
