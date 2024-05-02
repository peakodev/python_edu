import sys

from db.connect_rabbit import connection
from db.conf import config
from db.models import Contact
from db.connect_mongo import connect as connect_mongo

queue = config.get('RabbitMQ', 'queue_send_sms')


def main():
    conn = connection()
    channel = conn.channel()

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        connect_mongo()
        contact = Contact.objects(id=body.decode()).first()
        if not contact:
            print(f'Contact {body.decode()} not found')
            return
        if not contact.send_to_phone:
            print('Wrong queue. This message should be conusmed by consumer_email.py')
            return
        if contact.is_sent:
            print(f'SMS to {contact.phone} already sent')
            return
        contact.is_sent = True
        print(f'SMS to {contact.phone} sent')
        contact.save()

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for SMS messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
