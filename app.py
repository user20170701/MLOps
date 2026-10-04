from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome_root() -> dict[str, str]:
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
