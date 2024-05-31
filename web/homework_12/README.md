# Homework 12

## Description

The project is structured as follows:

- `requirements.txt`: This file lists the Python dependencies that need to be installed
- `conf/config.py`: class with ability to get .env variables using pydantic_settings
- `migrations/`: alembic migrations
- `src/`: fastapi project folder
- `src/database/`: folder with db connections and models
- `src/repository/`: folder with repositories scripts for users and contacts
- `src/routes/`: folder with routes for auth and contacts
- `src/schemas/`: folder with pydentic schemas
- `src/service/auth.py`: auth service with ability to hash password and JWT methods like access and refresh tokens
- `main.py`: fastapi entrypoint

## Prepare env

### Install libs 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the postgres in Docker container

Run postgres in container

```bash
docker pull postgres
```

```bash
docker run --name pg_homework12 -e POSTGRES_PASSWORD=mysecretpassword -p 5552:5432 -d postgres
```

Init first migration if not created before
```bash
alembic revision --autogenerate -m "Init"
```

Run migrations:
```bash
alembic upgrade head
```

Run server for testing

```bash
uvicorn main:app --host localhost --port 8000 --reload
```