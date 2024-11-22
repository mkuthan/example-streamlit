FROM python:3.12-slim-bookworm AS base

#
# Stage 1: Build stage
#
FROM base as builder

# Install and configure uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 

WORKDIR /app

# Copy project dependencies to get stable layer
COPY pyproject.toml uv.lock ./
RUN uv sync  --no-install-project --frozen --no-dev

# Copy project files separately to avoid rebuilding on every file change
COPY app.py ./
COPY example ./example
COPY .streamlit ./.streamlit
RUN uv sync --frozen --no-dev

#
# Stage 2: Runtime stage
#
FROM base

WORKDIR /app

COPY --from=builder /app ./

RUN useradd -m appuser
RUN chown -R appuser:appuser ./

USER appuser

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]