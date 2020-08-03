import json
import time
from kafka import KafkaProducer


def kpi_produce():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    for _ in range(1):
        data = {'kpi_key': 'kpi.dashboard1.a', 'timestamp': int(time.time() * 1000), 'value': 0.123}
        print(data)
        producer.send(topic='kpi_source', value=data)
    producer.flush()
    producer.close()


if __name__ == '__main__':
    kpi_produce()
