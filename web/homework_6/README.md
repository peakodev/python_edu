# Homework 6

## Description

Work with database Postgres

The project is structured as follows:

- `queries/query_*.sql`: queries folder with prepared select sql scripts
- `main.py`: This is the main script for running the scripts with preinstalled queries
- `connection.py`: This file for connection to Postgres DB
- `migrate_schema.py`: script for creating schema in database
- `populate_data.py`: populate fake data into DB using Faker package
- `requirements.txt`: This file lists the Python dependencies that need to be installed
- `schema.sql`: SQL schema

## Running the postgres in Docker container

Run postgres in container

```bash
docker pull postgres
```

```bash
docker run --name homework-6-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:

```bash
python main.py <query_number> <param1> <param2>
```

There is also another way to run:

```bash
python main.py
```

Then you choose the query number from input and write the params