FROM python:3.12-slim AS builder

# Copy uv binary from official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Install dependencies first (cached layer — only invalidated when pyproject.toml changes)
COPY pyproject.toml .
RUN uv pip install --system "mcp[cli]>=1.0.0" "pydantic>=2.0.0"

# Copy source and install the project package
COPY src/ src/
RUN uv pip install --system --no-deps .

# ── Runtime image ──────────────────────────────────────────────────────────────
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

ENV MCP_TRANSPORT=sse
ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

# Run as non-root
RUN useradd -r -u 1001 appuser
USER appuser

CMD ["python", "-m", "travel_mcp"]
