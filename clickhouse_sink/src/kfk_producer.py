import json
import time
from kafka import KafkaProducer


def func_producer():
    producer = KafkaProducer(bootstrap_servers='192.168.0.104:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    data = {'timestamp': int(time.time() * 1000), 'value': 1.0123}
    for _ in range(5):
        print(data)
        producer.send('topic-aiops', data)


func_producer()
