FROM python:3.12-slim-trixie

# 1. Install uv
COPY --from=ghcr.io/astral-sh/uv:0.7.3 /uv /uvx /bin/

WORKDIR /app
ADD . /app

# 2. Install the google-adk package globally in the container 
RUN uv pip install google-adk --system

# 3. Install your specific project dependencies
RUN uv pip install -r pyproject.toml --system

EXPOSE 8000

# Tells the ADK web server to listen to external requests
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]