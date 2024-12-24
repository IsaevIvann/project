FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip install poetry && \
    pip uninstall setuptools -y && \
    pip install --no-build-isolation 'setuptools<72.0.0'

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . /app/

ENV PYTHONPATH="${PYTHONPATH}:/app/src"