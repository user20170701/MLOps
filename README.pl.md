# MLOps

[English](README.md) | **Polski**

Projekt do kursu MLOps: serwowanie modelu ML z FastAPI i Dockerem.

## Lab 1: wprowadzenie do MLOps

Aplikacja udostępnia przez REST API model klasyfikujący gatunek irysa
(setosa, versicolor, virginica) na podstawie 4 wymiarów kwiatu.

## Narzędzia

- **uv**: zarządzanie zależnościami (`pyproject.toml`, `uv.lock`)
- **pre-commit**: Ruff (linter i formatter) oraz Xenon (złożoność kodu)
- **pydantic-settings** i pliki `.env`: konfiguracja dla środowisk dev, test i prod
- **sops** i GPG: szyfrowanie sekretów (`secrets.yaml`)
- **FastAPI**: serwer z endpointami `/`, `/health` i `/predict`
- **pytest**: testy konfiguracji i API
- **Docker** i Docker Compose: konteneryzacja aplikacji

## Struktura projektu

| Plik / katalog | Opis |
|---|---|
| `training.py` | trenuje model i zapisuje go do `model.joblib` |
| `inference.py` | wczytuje model i wykonuje predykcję |
| `app.py` | serwer FastAPI |
| `api/models/` | modele Pydantic żądania i odpowiedzi |
| `settings.py`, `main.py` | wczytywanie konfiguracji i sekretów |
| `config/` | pliki `.env` dla środowisk |
| `tests/` | testy |

## Uruchomienie

Instalacja zależności:

```bash
uv sync
```

Trening modelu:

```bash
uv run python training.py
```

Serwer lokalnie (dokumentacja API: http://localhost:8000/docs):

```bash
uv run uvicorn app:app --reload --port 8000
```

Testy:

```bash
uv run pytest tests -rP
```

Docker:

```bash
docker compose up
```

## Przykładowe zapytanie

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

Odpowiedź:

```json
{"prediction": "setosa"}
```
