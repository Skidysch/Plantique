#!/bin/sh

# Wait for the PostgreSQL service to be ready
echo "Waiting for postgres..."
while ! nc -z postgres 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run migrations
alembic upgrade head

python FastAPI/api_v1/db_migration/script.py

# Start the FastAPI application
exec uvicorn FastAPI.main:app --host 0.0.0.0 --port 8000
