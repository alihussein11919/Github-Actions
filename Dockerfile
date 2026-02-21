# Base image
FROM python:3.10-slim

# Prevent Python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc sqlite3 && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (Docker caching optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Create dbt profile directory
RUN mkdir -p /root/.dbt

# Create dbt profiles.yml
RUN echo "\
dbt_project:\n\
  target: dev\n\
  outputs:\n\
    dev:\n\
      type: sqlite\n\
      threads: 1\n\
      database: main\n\
      schema: main\n\
      schemas_and_paths:\n\
        main: etl.db\n\
      schema_directory: .\n\
" > /root/.dbt/profiles.yml

# Default command: run full pipeline
CMD python etl.py && \
    pytest tests.py && \
    dbt run --project-dir dbt_project && \
    dbt test --project-dir dbt_project