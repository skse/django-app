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
* [Docker](https://www.docker.com/)
* [Postman](https://www.postman.com/downloads/) &ast;

&ast; optional

## Usage
Copy `.env.example` to `.env`. Make appropriate config changes if you like (`SECRET_KEY` in particular)

Then

    docker compose up -d web
    docker-compose run --rm web python3 manage.py migrate

Finally,

`docker compose down` to shut down all networks & containers

`docker compose up -d` will spin app & run api tests as a side action

## API tests

    docker compose up cicd-api-tests

Or, if you wish to run/edit calls locally, you can import `./api-tests` folder to [Postman](https://www.postman.com/downloads/) & select `Local` environment 

## Format & Lint &ast; 

    isort . && black . && flake8

&ast; currently, requires local installation of ^^ packages