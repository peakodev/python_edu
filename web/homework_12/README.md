# Homework 12

## Description

The project is structured as follows:

- `requirements.txt`: This file lists the Python dependencies that need to be installed
- `migrations/`: alembic migrations
- `src/`: fastapi project folder
- `src/conf/config.py`: class with ability to get .env variables using pydantic_settings
- `src/database/`: folder with db connections and models
- `src/repository/`: folder with repositories scripts for users and contacts
- `src/routes/`: folder with routes for auth and contacts
- `src/schemas/`: folder with pydentic schemas
- `src/middleware/`: folder with middlewares
- `src/service/auth.py`: auth service with ability to hash password and JWT methods like access and refresh tokens
- `main.py`: fastapi entrypoint
- `tests/`: folder with tests
- `cleanup.sh`: Cleaned up __pycache__ directories and .pyc files.

## Prepare env

### Install libs 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the postgres in Docker container

Run docker compose

```bash
docker-compose up -d
```

Run migrations:

```bash
alembic upgrade head
```

Run server for testing

```bash
uvicorn main:app --host localhost --port 8008 --reload
```

### Tests

Run test:

```bash
pytest -v tests/
```

Run test coverage:

```bash
pytest -v --cov=src --cov-report=term-missing --cov-report=html tests/
```
