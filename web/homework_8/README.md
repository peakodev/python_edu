# Homework 8

## Description

Work with database Mongo, Redis for cache and RabbitMQ for messaging email

The project is structured as follows:

- `db/authors.json`: json with authors
- `db/quotes.json`: json with quotes
- `db/config.ini`: config file with database connections credentials
- `db/conf.py`: get conf variable from config.ini
- `db/connect_mongo.py`: prepare connection to Mongo DB
- `db/connect_redis.py`: prepare connection to Redis DB
- `db/connect_rabbit.py`: prepare connection to RabbitMQ
- `db/seed.py`: populate DB with data from authors.json and quotes.json
- `db/models.py`: Author and Quotes Document model for mongoengine
- `search.py`: script that uses the MongoEngine ORM to interact with MongoDB database
- `consumer_email.py`: consume messages to rabbitmq that emulata sent emails
- `consumer_sms.py`: consume messages to rabbitmq that emulata sent emails
- `producer.py`: create messages to rabbitmq
- `create_queues.py`: create RabbitMQ queues (send_email and send_sms)
- `requirements.txt`: This file lists the Python dependencies that need to be installed
- `db/config.ini.tmp`: Temp file with examples how ini should looks like

## Running the postgres in Docker container

### Prepare env

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run redis in container

```bash
docker pull redis
```

```bash
docker run --name home8-redis-cache -d -p 6699:6379 redis
```

### Run rabbitmq in container

```bash
docker pull rabbitmq:3.13-management
```

```bash
docker run -d --name home8-rabbitmq -p 5677:5672 -p 15677:15672 rabbitmq:3.13-management
```