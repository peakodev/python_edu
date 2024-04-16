# Class 7 Alembic

## Description

Work with sqlalchemy and alembic

The project is structured as follows:

- `models.py`: models Note, Record and Tag with relationship

## Running the postgres in Docker container

Run postgres in container

```bash
docker pull postgres
```

```bash
docker run --name class7 -e POSTGRES_PASSWORD=mysecretpassword -p 5551:5432 -d postgres
```

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Alembic

Init

```bash
alembic init alembic
```

Fix alembic.ini

```ini
sqlalchemy.url = postgresql://postgres:mysecretpassword@localhost:5541/class7
```

Change alembic/env.py

```py
from ..models import Base

target_metadata = Base.metadata
```

Create database in Postgress: loginc and create class7 DB

First revision 

```bash
alembic revision --autogenerate -m 'Init'
```

Upgrade migration

```bash
alembic upgrade head
```