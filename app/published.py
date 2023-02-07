
## emisor de datos

import pika
import sys
import json

def PublishRabittMQ(info):

    print(info)
    connection = pika.BlockingConnection(pika.ConnectionParameters('myhost'))

    channel = connection.channel()

    channel.exchange_declare(exchange = 'info_exchange', exchange_type='direct')




    channel.basic_publish(exchange='info_exchange', routing_key='info', body=json.dumps(info))



    connection.close()

