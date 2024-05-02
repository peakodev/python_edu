from faker import Faker

from db.connect_rabbit import connection
from db.conf import config
from db.models import Contact
from db.connect_mongo import connect as connect_mongo

queue_email = config.get('RabbitMQ', 'queue_send_email')
queue_sms = config.get('RabbitMQ', 'queue_send_sms')


def send_message(queue: str, message: str):
    conn = connection()
    channel = conn.channel()

    channel.basic_publish(exchange='', routing_key=queue, body=message.encode())
    print(f" [x] Sent '{message}'")
    conn.close()


def generate(count: int = 5):
    for _ in range(count):
        send_to_phone = fake.boolean()
        contact = Contact(
            fullname=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            send_to_phone=send_to_phone
        )
        contact.save()
        print(f'Contact {contact.email}, {contact.phone} saved with id {contact.id}')
        queue = queue_sms if send_to_phone else queue_email
        send_message(queue, str(contact.id))
        print(f'Message sent to {queue}')


if __name__ == '__main__':
    connect_mongo()
    fake = Faker()
    generate(10)
