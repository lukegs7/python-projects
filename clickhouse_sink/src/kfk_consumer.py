from kafka import KafkaConsumer


def func_consumer():
    # join a consumer group for dynamic partition assignment and offset commits
    consumer = KafkaConsumer('topic-aiops', bootstrap_servers=['192.168.0.104:9092'], auto_offset_reset='earliest')
    for msg in consumer:
        print(msg)


func_consumer()

