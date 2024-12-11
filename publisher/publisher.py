# Simple RabbitMQ publisher.

import os
import pika
from pika import DeliveryMode
from pika.exchange_type import ExchangeType

import serial
from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo

from threading import Lock
from queue import Queue, Empty

from PySide6.QtCore import QThread, Signal

amqp_url = os.environ['AMQP_URL']
print('URL: %s' % (amqp_url,))

# Подключение
parameters = pika.URLParameters(amqp_url)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange="test_exchange",
                         exchange_type=ExchangeType.direct,
                         durable=True)
channel.queue_declare(queue='standard',
                      durable=True)
channel.queue_bind(queue='standard', exchange='test_exchange', routing_key='standard_key')

print("Sending text message")
channel.basic_publish(
    'test_exchange', 'standard_key', 'Message to standard_key',
    pika.BasicProperties(content_type='text/plain',
                         delivery_mode=DeliveryMode.Transient))

connection.close()