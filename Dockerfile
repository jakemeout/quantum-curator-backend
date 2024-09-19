# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install a specific version of Poetry
RUN pip install --no-cache-dir poetry==1.5.1

# Copy only the dependency files
COPY pyproject.toml poetry.lock ./

# Set environment variable to prevent virtualenv creation
ENV POETRY_VIRTUALENVS_CREATE=false

# Install project dependencies
RUN poetry install --no-interaction --no-ansi --verbose

# Copy the rest of the application code
COPY . .

# Expose port (if needed)
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "your_application_entrypoint"]
