import pika
import pickle

from wearable_entity import WearableDevice


def get_connection(key):
    conn = pika.BlockingConnection(pika.ConnectionParameters("34.146.240.199"))
    channel = conn.channel()
    max_priority = 10

    channel.queue_declare(queue=key, arguments={"x-max-priority": max_priority})

    return channel


def send_object(channel, key, obj, priority=1):
    channel.basic_publish(
        exchange='',
        routing_key=key,
        body=pickle.dumps(obj),
        properties=pika.BasicProperties(priority=priority)
    )


def send_msg(channel, key, msg):
    channel.basic_publish(
        exchange='',
        routing_key=key,
        body=msg
    )
