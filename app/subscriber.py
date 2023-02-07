

import django
from sys import path
from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.core.mail import send_mail
from core.models import Recipe
import pika
import json




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
    print('[x] pricipio del proceso %r' %str(body[1]))
    recipe = Recipe.objects.create(body[0])
    # self._get_or_create_tags(tags, recipe)
    # self._get_or_create_ingredients(ingredients, recipe)
    print(recipe.firstName)
    subject = f"Tienes un nuevo mensaje de contacto de {recipe.firstName}  "

    message = f"Tienes un mensaje de  {recipe.firstName} su email es  {recipe.email}\n\n" \
                    f" su telefono es {recipe.Phone}\'s de la compañia {recipe.Company} comments: {recipe.Comment}"
    response = send_mail(subject, message,'nahuel.perugi@gmail.com',
                    ['nahuel.perugi@gmail.com'],fail_silently=False)

    print('[x] fin del proceso %r' %body)





channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()