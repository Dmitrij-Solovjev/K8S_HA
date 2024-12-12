# Simple RabbitMQ publisher.

import os
import pika
from pika import DeliveryMode
from pika.exchange_type import ExchangeType

import serial
from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo
import time

from threading import Lock
from queue import Queue, Empty

from PySide6.QtCore import QThread, Signal


def main():
    amqp_url = os.environ['AMQP_URL']
    print('URL: %s' % (amqp_url,))

    # Подключение
    parameters = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()


    # Этот метод создает обмен, если он еще не существует, и если обмен
    # существует, проверяет, что он принадлежит к правильному и ожидаемому классу.
    channel.exchange_declare(exchange="test_exchange",
                         exchange_type=ExchangeType.direct,
                         durable=True)

    # Объявите очередь, создайте ее, если необходимо.
    channel.queue_declare(queue='standard',
                      durable=True)
    
    # Привязать очередь к указанному обмену
    channel.queue_bind(queue='standard', exchange='test_exchange', routing_key='standard_key')

    print("Sending custom text message")
    try:
        counter = 0
        while True:
            channel.basic_publish(
                'test_exchange', 'standard_key', 'Message to standard_key with number {' + str(counter) + '}',
                pika.BasicProperties(content_type='text/plain',
                                 delivery_mode=DeliveryMode.Transient))
            #     Transient = 1 - вариант ненадежной доставки
            #    Persistent = 2  - вариант надежной доставки
            # Вместе с durable=True Persistent = 2 сохранится на жесткий диск
            counter+=5
            time.sleep(5)
    except:
        connection.close()

if __name__ == '__main__':
    main()