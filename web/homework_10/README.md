# Homework 10

## Description

Using django framework make a site like http://quotes.toscrape.com/

The project is structured as follows:

- `myquotes/`: django project
- `myquotes/quotes`: django application for authors and quotes CRUD
- `myquotes/users`: django application for auth (login/signup/logout)
- `config.py`: get conf variable from .env
- `migrate_data/connect_mongo.py`: prepare connection to Mongo DB from homework 9
- `migrate_data/models.py`: Author and Quotes Document model for mongoengine from homework 9
- `requirements.txt`: This file lists the Python dependencies that need to be installed

## Prepare env

### Install libs 

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running the postgres in Docker container

```bash
docker-compose up -d
```

```bash
cd myquotes
py manage.py migrate
py manage.py createsuperuser
py ../migrate.py
```

```bash
py manage.py runserver
```