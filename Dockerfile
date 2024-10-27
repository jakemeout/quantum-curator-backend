FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install a specific version of Poetry
RUN pip install --no-cache-dir poetry==1.5.1

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Set environment variable to prevent virtualenv creation
ENV POETRY_VIRTUALENVS_CREATE=false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --verbose

# Copy application code
COPY . .

# Debug: List files in /app
RUN ls -la /app

# Expose port
EXPOSE 8000

# Command to run the application with more verbose output
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug"]