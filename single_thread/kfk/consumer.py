import json
from kafka import KafkaConsumer


def kpi_consumer():
    topics = ['kpi_sink']
    consumer = KafkaConsumer(*topics, bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')
    for msg in consumer:
        data=json.loads(msg.value)
        print(data['kpi_key'],type(data['kpi_key']))
        print(data['timestamp'],type(data['timestamp']))
        print(data['value'],type(data['value']))
        print(data['lower'],type(data['lower']))
        print(data['upper'],type(data['upper']))
        print(data['score'],type(data['score']))
        print(data['anomaly'],type(data['anomaly']))


if __name__ == '__main__':
    kpi_consumer()
