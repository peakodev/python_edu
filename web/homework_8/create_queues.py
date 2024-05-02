from db.connect_rabbit import create_queue

from db.conf import config

queue_send_email = config.get('RabbitMQ', 'queue_send_email')
queue_send_sms = config.get('RabbitMQ', 'queue_send_sms')

if __name__ == '__main__':
    create_queue(queue_send_email)
    create_queue(queue_send_sms)
    print('Queues created')
