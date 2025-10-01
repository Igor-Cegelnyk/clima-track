FROM python:3.12-slim

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.0

RUN pip install poetry==${POETRY_VERSION}


WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root --only main

COPY ./app ./app


RUN chmod +x /app/app/entrypoint.sh

ENTRYPOINT ["/app/app/entrypoint.sh"]