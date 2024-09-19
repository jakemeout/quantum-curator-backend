FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only dependency files first
COPY pyproject.toml poetry.lock ./

# Install dependencies with verbose output
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --verbose

# Copy the rest of the application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
