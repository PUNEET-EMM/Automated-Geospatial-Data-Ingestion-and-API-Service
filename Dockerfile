# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install cron, PostgreSQL client, and other necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends cron postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application folder and data ingestion script
COPY app /app/app
COPY app/data_ingestion.py /app/data_ingestion.py

# Add the cron job configuration file
COPY crontab /etc/cron.d/data-ingestion-cron

# Set permissions and register the cron job
RUN chmod 0644 /etc/cron.d/data-ingestion-cron && \
    crontab /etc/cron.d/data-ingestion-cron

# Expose the FastAPI app's port
EXPOSE 8000

# Environment variables for database and GeoJSON URL
ENV DATABASE_URL="postgresql://postgres:SimplePass!2024@db:5432/geo_database"
ENV GEOJSON_URL="https://file.notion.so/f/f/9301458a-f465-42d3-80eb-7c09bae15034/282d7ed4-5168-4e77-91be-59906c19f9f3/Map_(10).geojson?table=block&id=655f6883-c12c-4503-bd82-157ea8ee1571&spaceId=9301458a-f465-42d3-80eb-7c09bae15034&expirationTimestamp=1733508000000&signature=pxNn_GtkzVZ3wnwKnwbCrWJnIfBqEgnvVEEnb3WqdQs&downloadName=karnataka.geojson"

# Command to ensure the app initializes before starting cron
CMD ["sh", "-c", "until pg_isready -h db -p 5432 -U postgres; do echo 'Waiting for database...'; sleep 2; done; uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload & sleep 10 && cron -f"]
