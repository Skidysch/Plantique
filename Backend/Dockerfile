FROM python:3.12.1-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
RUN apt-get update && apt-get install -y netcat-openbsd gcc

COPY . .
RUN chmod +x ./postgres_entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./postgres_entrypoint.sh"]