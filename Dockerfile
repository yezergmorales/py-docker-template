ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files and keeps output unbuffered
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

# Define API_KEY as build argument and environment variable
# ARG API_KEY
# ENV API_KEY=${API_KEY}

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Create non-privileged user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-install-project --no-dev

# Switch to the non-privileged user to run the application.
USER appuser

COPY --chown=appuser:appuser ./src ./src

EXPOSE 8000

CMD ["uvicorn", "src.my_package.main:app", "--host", "0.0.0.0", "--port", "8000"]
