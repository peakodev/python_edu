# Homework 11

## Description

The project is structured as follows:

- `requirements.txt`: This file lists the Python dependencies that need to be installed

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
docker run --name pg_homework11 -e POSTGRES_PASSWORD=mysecretpassword -p 5552:5432 -d postgres
```

Run migrations:
```bash
alembic upgrade head
```

Run server for testing

```bash
uvicorn app.main:app --host localhost --port 8000 --reload
```