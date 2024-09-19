FROM python:3.10-slim

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

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
