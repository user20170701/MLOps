# Official uv image with Python 3.12 preinstalled
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Compile .py to bytecode for faster startup
ENV UV_COMPILE_BYTECODE=1
# Copy files from cache instead of hardlinking (required with cache mounts)
ENV UV_LINK_MODE=copy

# Install dependencies first, in a separate layer, for better build caching
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copy application code and model
ADD . /app

# Use the virtualenv created by uv sync directly
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
