# Sample RabbitMQ receiver.

import os
import pika
from pika.exchange_type import ExchangeType

def on_message(chan, method_frame, header_frame, body):
    """Called when a message is received. Log message and ack it."""
    print(f'Delivery properties: {method_frame}, message metadata: {header_frame}')
    print(f'Message body: {body}')
    chan.basic_ack(delivery_tag=method_frame.delivery_tag)

def main():
    """Main method."""
    amqp_url = os.environ['AMQP_URL']
    print('URL: %s' % (amqp_url,))
    parameters = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.exchange_declare(exchange="test_exchange",
                         exchange_type=ExchangeType.direct,
                         durable=True)
    # durable=True - сохранение на диск очереди RabitMQ для дальнейшей передачи в случае возобновлении работы
    channel.queue_declare(queue='standard',
                        durable=True)
    channel.queue_bind(queue='standard', exchange='test_exchange', routing_key='standard_key')
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume('standard', on_message)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    connection.close()


if __name__ == '__main__':
    main()
    