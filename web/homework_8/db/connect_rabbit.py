from pika import PlainCredentials, BlockingConnection, ConnectionParameters

from db.conf import config


def connection():
    credentials = PlainCredentials(
        config.get('RabbitMQ', 'user'),
        config.get('RabbitMQ', 'passwd'))
    params = ConnectionParameters(
        host=config.get('RabbitMQ', 'host'),
        port=config.get('RabbitMQ', 'port'),
        credentials=credentials)
    connection = BlockingConnection(params)

    return connection


def create_queue(queue: str):
    conn = connection()
    channel = conn.channel()
    channel.queue_declare(queue=queue)

    conn.close()
