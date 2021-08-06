import pika
import pickle
import time

import dbtools
from wearable_entity import WearableDevice


def receive_priority(key):
    conn = pika.BlockingConnection(pika.ConnectionParameters(host="34.146.240.199"))
    channel = conn.channel()

    max_priority = 10
    channel.queue_declare(queue=key, arguments={"x-max-priority": max_priority})

    db = dbtools.get_database()

    def callback(ch, method, properties, body):
        device = pickle.loads(body)
        body_status = device.body_status
        send_status = dbtools.write_indicator(db, device)
        print(device.uid, time.strftime("%Y-%m-%d %H:%M:%S", device.time), device.body_status, send_status)

        channel.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue=key,
        on_message_callback=callback,
        auto_ack=False
    )

    channel.start_consuming()


receive_priority("beta")
