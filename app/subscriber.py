

import django
from sys import path
from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.core.mail import send_mail
from core.models import Recipe
import pika
import json
from recipe import serializers
import codecs




connection = pika.BlockingConnection(pika.ConnectionParameters('rabbithost'))

channel = connection.channel()

channel.exchange_declare(exchange='info_exchange', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

#print("Subscriber queue_name =", queue_name)



channel.queue_bind(exchange='info_exchange', queue=queue_name, routing_key="info")
channel.queue_bind(exchange='info_exchange', queue=queue_name, routing_key="Warning")
channel.queue_bind(exchange='info_exchange', queue=queue_name, routing_key="Info")



def callback(ch, method, properties, body):
    strBody = codecs.decode(body, 'UTF-8')
    print('[x] pricipio del proceso')



    recipe = Recipe.objects.create(**json.loads(strBody))
    # self._get_or_create_tags(tags, recipe)
    # self._get_or_create_ingredients(ingredients, recipe)

    subject = f"Tienes un nuevo mensaje  de {recipe.firstName}  "

    message = f"te acaba de contactar {recipe.firstName} su informacion es la sigueinte  es: \n\n \
                - Mail: {recipe.email} \n \
                - Numero de contacto: {recipe.Phone} \n \
                - Compañia: {recipe.Company} \n \
                - Comentario: {recipe.Comment}"
    response = send_mail(subject, message,'nahuel.perugi@gmail.com',
                    ['nahuel.perugi@gmail.com'],fail_silently=False)

    print('[x] fin del proceso %r' %recipe.firstName)





channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()