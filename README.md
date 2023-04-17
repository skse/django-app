# Django - DRF - Docker App
Example subscriptions app utilizing DRF, PostgreSQL &amp; Docker setup

## Description
This app provides a baseline setup of Django-DRF application using PostgreSQL DB.

Features:
- Docker Compose setup to spin the app, DB & execute API tests suite
- Postman collection of API tests profiled for Docker & Local setups
- Format & linting
- An openapi schema for clients generation
    
## Prerequisites
[Docker](https://www.docker.com/)

## Usage

    docker compose up -d web
    docker-compose run --rm web python3 manage.py migrate

## API tests

    docker compose up --exit-code-from cicd-api-tests

## Format & Lint

    isort . && black . && flake8